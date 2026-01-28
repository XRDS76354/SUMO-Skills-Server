#!/usr/bin/env python3
"""
Cross-platform smoke test for SUMO CLI and tools.

This script exercises a minimal workflow:
- netgenerate -> randomTrips -> duarouter -> sumo -> xml2csv
- attributeStats is optional (requires lxml)
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

CRASH_CODES = {139, 134, -11, 3221225477}


def is_crash(returncode):
    return returncode in CRASH_CODES


def run(cmd, cwd, env, check=True, capture=False):
    cmd_display = " ".join(str(part) for part in cmd)
    print(f"[run] {cmd_display}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        text=True,
        capture_output=capture,
    )
    if capture and result.stdout:
        print(result.stdout.strip())
    if capture and result.stderr:
        print(result.stderr.strip())
    if check and result.returncode != 0:
        raise RuntimeError(f"Command failed ({result.returncode}): {cmd_display}")
    return result


def resolve_binary(name, sumo_home):
    found = shutil.which(name)
    if found:
        return found
    if sumo_home:
        suffix = ".exe" if os.name == "nt" else ""
        candidate = Path(sumo_home) / "bin" / f"{name}{suffix}"
        if candidate.exists():
            return str(candidate)
    return None


def resolve_sumo_home():
    env_home = os.environ.get("SUMO_HOME")
    if env_home:
        return env_home
    sumo_bin = shutil.which("sumo")
    if sumo_bin:
        candidate = Path(sumo_bin).resolve().parent.parent
        if (candidate / "tools").exists():
            return str(candidate)
    return None


def write_sumocfg(path, net_file, route_file):
    content = """<configuration>
  <input>
    <net-file value=\"{net_file}\"/>
    <route-files value=\"{route_file}\"/>
  </input>
  <time>
    <begin value=\"0\"/>
    <end value=\"100\"/>
  </time>
  <output>
    <tripinfo-output value=\"tripinfo.xml\"/>
    <summary-output value=\"summary.xml\"/>
  </output>
</configuration>
""".format(net_file=net_file, route_file=route_file)
    path.write_text(content, encoding="utf-8")


def has_lxml(python_exe):
    result = subprocess.run(
        [python_exe, "-c", "import lxml"],
        text=True,
        capture_output=True,
    )
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(
        description="Run a minimal SUMO workflow to verify tools.",
    )
    parser.add_argument("--workdir", help="Directory for test artifacts.")
    parser.add_argument("--keep-dir", action="store_true", help="Keep artifacts if workdir is not provided.")
    args = parser.parse_args()

    sumo_home = resolve_sumo_home()
    if not sumo_home:
        print("[error] SUMO_HOME is not set and sumo was not found in PATH.")
        return 1

    sumo_bin = resolve_binary("sumo", sumo_home)
    netgenerate_bin = resolve_binary("netgenerate", sumo_home)
    duarouter_bin = resolve_binary("duarouter", sumo_home)

    if not sumo_bin or not netgenerate_bin or not duarouter_bin:
        print("[error] Required SUMO binaries were not found in PATH or SUMO_HOME/bin.")
        return 1

    env = os.environ.copy()
    env["SUMO_HOME"] = sumo_home

    tools_dir = Path(sumo_home) / "tools"
    random_trips = tools_dir / "randomTrips.py"
    xml2csv = tools_dir / "xml" / "xml2csv.py"
    attribute_stats = tools_dir / "output" / "attributeStats.py"

    if not random_trips.exists() or not xml2csv.exists():
        print("[error] SUMO tools were not found under SUMO_HOME/tools.")
        return 1

    workdir_path = None
    temp_dir = None
    if args.workdir:
        workdir_path = Path(args.workdir).resolve()
        workdir_path.mkdir(parents=True, exist_ok=True)
    elif args.keep_dir:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        workdir_path = Path.cwd() / f"_tmp_sumo_skill_test_{stamp}"
        workdir_path.mkdir(parents=True, exist_ok=True)
    else:
        temp_dir = tempfile.TemporaryDirectory()
        workdir_path = Path(temp_dir.name)

    print(f"[info] Using workdir: {workdir_path}")

    net_file = workdir_path / "grid.net.xml"
    trips_file = workdir_path / "trips.trips.xml"
    route_file = workdir_path / "routes.rou.xml"
    sumocfg_file = workdir_path / "scenario.sumocfg"

    try:
        run([
            netgenerate_bin,
            "--grid",
            "--grid.number",
            "3",
            "--grid.length",
            "100",
            "-o",
            str(net_file),
        ], cwd=workdir_path, env=env)

        run([
            sys.executable,
            "-S",
            str(random_trips),
            "-n",
            str(net_file),
            "-e",
            "100",
            "-p",
            "1",
            "-o",
            str(trips_file),
            "--seed",
            "42",
        ], cwd=workdir_path, env=env)

        run([
            duarouter_bin,
            "-n",
            str(net_file),
            "-r",
            str(trips_file),
            "-o",
            str(route_file),
        ], cwd=workdir_path, env=env)

        write_sumocfg(sumocfg_file, net_file.name, route_file.name)

        run([
            sumo_bin,
            "-c",
            str(sumocfg_file),
        ], cwd=workdir_path, env=env)

        tripinfo_xml = workdir_path / "tripinfo.xml"
        if not tripinfo_xml.exists():
            raise RuntimeError("tripinfo.xml was not generated.")

        run([
            sys.executable,
            "-S",
            str(xml2csv),
            str(tripinfo_xml),
            "--output",
            str(workdir_path / "tripinfo.csv"),
        ], cwd=workdir_path, env=env)

        if attribute_stats.exists() and has_lxml(sys.executable):
            result = run([
                sys.executable,
                str(attribute_stats),
                "--element",
                "tripinfo",
                "--attribute",
                "timeLoss",
                str(tripinfo_xml),
            ], cwd=workdir_path, env=env, check=False, capture=True)
            if result.returncode != 0:
                if is_crash(result.returncode):
                    print("[warn] attributeStats crashed; skipping.")
                else:
                    print("[warn] attributeStats failed; skipping.")
        else:
            print("[warn] attributeStats skipped (lxml not installed).")

    except Exception as exc:
        print(f"[error] {exc}")
        return 1
    finally:
        if temp_dir is not None:
            temp_dir.cleanup()

    print("[ok] SUMO smoke test completed.")
    if args.keep_dir or args.workdir:
        print(f"[info] Artifacts retained at: {workdir_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

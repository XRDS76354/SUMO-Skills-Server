# SUMO-Skills: AI-Oriented SUMO Skill Library

<div align="center">
  <br />
  <p align="center">
    <a href="#"><img src="https://img.shields.io/badge/Status-Active-success" alt="Status" /></a>
    <a href="https://www.eclipse.org/sumo/"><img src="https://img.shields.io/badge/SUMO-1.20+-blue" alt="SUMO" /></a>
    <a href="#"><img src="https://img.shields.io/badge/Python-3.10+-blue" alt="Python" /></a>
    <a href="#"><img src="https://img.shields.io/badge/License-MIT-green" alt="License" /></a>
    <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey" alt="Platform" />
  </p>
</div>

中文文档: [README_CN.md](README_CN.md)

`SUMO-Skills` is a specialized skill set for **AI coding assistants** working on SUMO tasks.  
It is not a new simulation engine and not a Python SDK. Instead, it packages common SUMO work into reusable skill modules (`SKILL.md + references`) so assistants can produce more reliable, executable solutions.

## What Is SUMO-Skills

You can think of it as an operating layer for traffic simulation tasks:

- Unified task decomposition: from setup and network creation to simulation and analysis
- Unified routing rules: map different requests to the right skill (env/core/output/mcp/rl)
- Unified command style: reduce vague answers and increase runnable commands
- Unified collaboration interface: reusable across Code, Claude Code, Trae, and Cursor

## What Is In This Repo

```text
sumo-env/      Installation, SUMO_HOME/PATH, smoke tests
sumo-core/     Networks, demand, routing, simulation run, TraCI basics
sumo-output/   Output config, detectors, XML/CSV conversion, stats
sumo-mcp/      MCP workflow design and tool parameter references
sumo-rl/       Traffic signal reinforcement learning with sumo-rl
```

## Feature Overview

| Module | Problem It Solves | Typical Output |
|---|---|---|
| `sumo-env` | Failed setup, broken `SUMO_HOME`/`PATH`, missing tools | Runnable environment + verification |
| `sumo-core` | End-to-end base simulation flow (net -> trips -> routes -> sumo) | `.net.xml` / `.rou.xml` / `.sumocfg` |
| `sumo-output` | tripinfo/FCD/summary/detector analysis needs | Structured output files + analysis commands |
| `sumo-mcp` | Multi-step automation, live TraCI control, workflow orchestration | MCP tool calls + workflow plans |
| `sumo-rl` | RL experiment design and training for signal control | Training config + script skeletons |

## 5-Minute Quick Start

### 1) Verify SUMO

```bash
sumo --version
```

If SUMO is not installed:

- Windows: `winget install --name sumo`
- Ubuntu/Debian: `sudo apt-get install sumo sumo-tools sumo-doc`
- macOS: `brew install sumo`

### 2) Set Environment Variables

Linux/macOS:

```bash
export SUMO_HOME="/usr/share/sumo"
export PATH="$SUMO_HOME/bin:$PATH"
```

Windows PowerShell:

```powershell
$env:SUMO_HOME="C:\Program Files\Eclipse\sumo"
$env:PATH="$env:SUMO_HOME\bin;$env:PATH"
```

### 3) Run Repository Smoke Test

```bash
python sumo-env/scripts/sumo_skills_smoke_test.py
```

## How To Collaborate In Code, Claude Code, Trae, Cursor

Start with the same shared principles:

1. Use this repository as the workspace context
2. Always include goal, input files, constraints, and expected output
3. Explicitly name the skill module (`sumo-core`, `sumo-output`, etc.)
4. Ask for executable steps and commands first, then file edits

### Code (Codex / terminal agent)

Recommended:

- Define skill routing in project rules (for example, AGENTS instructions)
- Name the skill directly in each request
- Ask the agent to run commands locally and report key results

Example prompt:

```text
Use sumo-core: generate a 4x4 grid network in the current directory, run a 1000-second simulation, output tripinfo.xml, and provide full commands.
```

### Claude Code

Recommended:

- Put skill routing in project instructions (commonly `CLAUDE.md`)
- Provide this repo path and SUMO env variables to the assistant
- Split complex jobs into two phases: plan first, execute second

Example prompt:

```text
Execute in order sumo-env -> sumo-core -> sumo-output:
1) check environment
2) run a minimal simulation
3) convert outputs to CSV
```

### Trae

Recommended:

- Add a skill routing table to Trae project memory/rules
- Use a fixed collaboration template: `goal -> current files -> constraints -> deliverables`
- Ask for command draft first, then confirm execution

Example prompt:

```text
Use sumo-output: update scenario.sumocfg to include tripinfo and summary outputs, and provide post-processing stats commands.
```

### Cursor

Recommended:

- Add skill routing to Cursor Project Rules (for example `.cursor/rules` or `.cursorrules`)
- Put "prefer runnable commands and concrete file edits" as top rule
- Require changed file paths and patch-style explanations for review

Example prompt:

```text
Use sumo-rl: create a minimal single-agent training script from existing net/route files and explain key hyperparameters.
```

## Universal Prompt Template (All 4 Tools)

```text
You are working as a SUMO engineering assistant.
Preferred skills: sumo-env / sumo-core / sumo-output / sumo-mcp / sumo-rl (pick by task).

Goal:
Known inputs:
Constraints:
Expected outputs:
- First provide a numbered execution plan
- Then provide directly runnable commands
- If files must be changed, list target file paths first
```

## Common Workflows

### Workflow 1: Minimal Runnable Simulation (core)

```bash
netgenerate --grid --grid.number 4 --grid.length 100 -o grid.net.xml
python $SUMO_HOME/tools/randomTrips.py -n grid.net.xml -e 1000 -p 5 -o trips.trips.xml
duarouter -n grid.net.xml -r trips.trips.xml -o routes.rou.xml
sumo -c scenario.sumocfg
```

### Workflow 2: Outputs and Stats (output)

```bash
sumo -c scenario.sumocfg --tripinfo-output tripinfo.xml --summary-output summary.xml
python $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml
python $SUMO_HOME/tools/output/attributeStats.py --element tripinfo --attribute timeLoss tripinfo.xml
```

### Workflow 3: Automation Orchestration (mcp)

- Use `sumo-mcp` to design multi-step flows for network generation, demand generation, simulation control, and signal optimization
- Best for full pipeline automation in one request
- Note: the MCP server itself must be configured locally; this repository provides skill guidance and parameter references

## Skill Routing Cheat Sheet

| Task | Preferred Skill |
|---|---|
| Install SUMO and fix env variables | `sumo-env` |
| Build network, demand, and run simulation | `sumo-core` |
| Configure tripinfo/FCD/detectors and analyze results | `sumo-output` |
| Multi-step automation and live TraCI control | `sumo-mcp` |
| RL-based traffic signal control | `sumo-rl` |

## Additional Resources

- [Eclipse SUMO Docs](https://sumo.dlr.de/docs/)
- [SUMO GitHub Repository](https://github.com/eclipse-sumo/sumo)
- [sumo-rl Project](https://github.com/LucasAlegre/sumo-rl)

## License

MIT

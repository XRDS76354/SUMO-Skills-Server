# SUMO-Skills: Comprehensive SUMO Traffic Simulation Skill Collection

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

SUMO-Skills is a comprehensive collection of AI skills for [Eclipse SUMO](https://www.eclipse.org/sumo/) (Simulation of Urban MObility) traffic simulation. It provides structured guidance and best practices for network creation, demand generation, simulation execution, output analysis, reinforcement learning, and MCP-based automation workflows.

## 📚 Overview

This skill collection is organized into five specialized modules:

| Skill | Description | Use Case |
|-------|-------------|----------|
| **sumo-core** | Core SUMO workflows and CLI usage | Standard simulation tasks |
| **sumo-env** | Installation and environment setup | Setup and configuration |
| **sumo-mcp** | MCP server integration for automation | Automated workflows |
| **sumo-output** | Output configuration and analysis | Result processing |
| **sumo-rl** | Reinforcement learning for traffic signals | RL training |

## 🚀 Quick Start

### Prerequisites

- **Operating System**: Windows 10+, Linux (Ubuntu 18.04+), macOS 10.15+
- **Python**: 3.10 or higher
- **SUMO**: 1.20.0 or higher
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Disk Space**: 2GB free space

### Installation

#### Step 1: Install SUMO

**Windows:**
```powershell
# Using winget (recommended)
winget install --name sumo

# Or download installer from https://sumo.dlr.de/
```

**Linux (Ubuntu/Debian):**
```bash
sudo add-apt-repository ppa:sumo/stable
sudo apt-get update
sudo apt-get install sumo sumo-tools sumo-doc
```

**macOS:**
```bash
brew install sumo
```

#### Step 2: Configure Environment Variables

**Windows (PowerShell):**
```powershell
$env:SUMO_HOME="C:\Program Files\Eclipse\sumo"
$env:PATH="$env:SUMO_HOME\bin;$env:PATH"

# For permanent setup
[Environment]::SetEnvironmentVariable("SUMO_HOME", "C:\Program Files\Eclipse\sumo", "User")
```

**Linux/macOS:**
```bash
export SUMO_HOME="/usr/share/sumo"  # Linux
# export SUMO_HOME="/usr/local/share/sumo"  # macOS with Homebrew
export PATH="$SUMO_HOME/bin:$PATH"

# Add to ~/.bashrc or ~/.zshrc for persistence
echo 'export SUMO_HOME="/usr/share/sumo"' >> ~/.bashrc
echo 'export PATH="$SUMO_HOME/bin:$PATH"' >> ~/.bashrc
```

#### Step 3: Verify Installation

```bash
sumo --version
python sumo-env/scripts/sumo_skills_smoke_test.py
```

## 📖 Skill Modules

### 1. sumo-core: Core Simulation Workflows

Use this skill for standard SUMO operations including network creation, demand generation, and simulation execution.

**Key Capabilities:**
- Network generation (`netgenerate`, `netconvert`)
- OSM import and conversion
- Demand generation (`randomTrips.py`, `od2trips`)
- Route computation (`duarouter`)
- Simulation execution (`sumo`, `sumo-gui`)
- TraCI basics

**Example Workflow:**
```bash
# 1. Generate a grid network
netgenerate --grid --grid.number 4 --grid.length 100 -o grid.net.xml

# 2. Generate random trips
python $SUMO_HOME/tools/randomTrips.py -n grid.net.xml -e 3600 -p 1 -o trips.trips.xml

# 3. Compute routes
duarouter -n grid.net.xml -r trips.trips.xml -o routes.rou.xml

# 4. Run simulation
sumo -c scenario.sumocfg
```

**References:**
- [Command Line Basics](sumo-core/references/command-line-basics.md)
- [Network Build](sumo-core/references/network-build.md)
- [Demand and Routing](sumo-core/references/demand-routing.md)
- [Simulation Run](sumo-core/references/simulation-run.md)
- [TraCI Basics](sumo-core/references/traci-basics.md)

### 2. sumo-env: Environment Setup

Use this skill for SUMO installation, environment variable configuration, and dependency management.

**Key Capabilities:**
- Cross-platform installation guides
- Environment variable setup (SUMO_HOME, PATH)
- Python tool dependencies
- Installation verification

**Smoke Test:**
```bash
python sumo-env/scripts/sumo_skills_smoke_test.py --keep-dir
```

**References:**
- [Install SUMO](sumo-env/references/install-sumo.md)
- [Environment Variables](sumo-env/references/env-vars.md)
- [Python Tools](sumo-env/references/python-tools.md)

### 3. sumo-mcp: MCP Automation

Use this skill for automated multi-step SUMO workflows via the Model Context Protocol (MCP).

**Key Capabilities:**
- Automated network generation and conversion
- Demand generation and routing
- Real-time simulation control via TraCI
- Traffic signal optimization
- Reinforcement learning workflows
- Pre-built automation workflows

**Available Tools:**
- `manage_network`: Network generation, OSM download, conversion
- `manage_demand`: Random trips, OD matrix, route computation
- `control_simulation`: Connect, step, disconnect
- `query_simulation_state`: Vehicle list, variables, simulation stats
- `optimize_traffic_signals`: Cycle adaptation, coordination
- `run_workflow`: sim_gen_eval, signal_opt, rl_train
- `manage_rl_task`: List scenarios, custom training

**Example Workflow:**
```json
{
  "workflow_name": "sim_gen_eval",
  "params": {
    "grid_number": 4,
    "sim_seconds": 1000,
    "output_dir": "output"
  }
}
```

**References:**
- [MCP Setup](sumo-mcp/references/mcp-setup.md)
- [MCP Tools](sumo-mcp/references/mcp-tools.md)

### 4. sumo-output: Output Analysis

Use this skill for configuring, generating, and analyzing SUMO simulation outputs.

**Key Capabilities:**
- Output type configuration (tripinfo, FCD, summary, etc.)
- Detector setup and data collection
- XML to CSV conversion
- Statistical analysis

**Common Outputs:**
```bash
# Command line outputs
sumo -c scenario.sumocfg --tripinfo-output tripinfo.xml --fcd-output fcd.xml

# Convert to CSV
python $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml

# Generate statistics
python $SUMO_HOME/tools/output/attributeStats.py --element tripinfo --attribute timeLoss tripinfo.xml
```

**References:**
- [Output Types](sumo-output/references/output-types.md)
- [Output Tools](sumo-output/references/output-tools.md)
- [Output Parsing](sumo-output/references/output-parsing.md)

### 5. sumo-rl: Reinforcement Learning

Use this skill for reinforcement learning-based traffic signal control using sumo-rl.

**Key Capabilities:**
- Single-agent (Gymnasium) environments
- Multi-agent (PettingZoo) environments
- Custom observation functions
- Custom reward functions
- Integration with RL libraries (stable-baselines3, RLlib)

**Example Usage:**
```python
import gymnasium as gym
import sumo_rl

# Single-agent environment
env = gym.make('sumo-rl-v0',
               net_file='path/to/net.net.xml',
               route_file='path/to/routes.rou.xml',
               use_gui=False,
               num_seconds=10000)

obs, info = env.reset()
done = False
while not done:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
```

**References:**
- [RL Installation](sumo-rl/references/rl-install.md)
- [MDP (Observations, Actions, Rewards)](sumo-rl/references/rl-mdp.md)
- [Environment API](sumo-rl/references/rl-env-api.md)

## ⚙️ Configuration

### SUMO Configuration File (.sumocfg)

```xml
<configuration>
  <input>
    <net-file value="network.net.xml"/>
    <route-files value="routes.rou.xml"/>
    <additional-files value="detectors.add.xml"/>
  </input>
  <time>
    <begin value="0"/>
    <end value="3600"/>
  </time>
  <output>
    <tripinfo-output value="tripinfo.xml"/>
    <summary-output value="summary.xml"/>
    <fcd-output value="fcd.xml"/>
  </output>
</configuration>
```

### Additional Files

**Traffic Light Definition:**
```xml
<additional>
  <tlLogic id="center" type="static" programID="0" offset="0">
    <phase duration="31" state="GGGrrrGGGrrr"/>
    <phase duration="5" state="yyyrrryyyrrr"/>
    <phase duration="31" state="rrrGGGrrrGGG"/>
    <phase duration="5" state="rrryyyrrryyy"/>
  </tlLogic>
</additional>
```

**Detector Definition:**
```xml
<additional>
  <inductionLoop id="detector_0" lane="edge_0_0" pos="10" 
                 period="60" file="detector_output.xml"/>
</additional>
```

## 🛠️ Usage Examples

### Example 1: Basic Grid Simulation

```bash
# Create working directory
mkdir -p grid_simulation && cd grid_simulation

# Generate 4x4 grid network
netgenerate --grid --grid.number 4 --grid.length 100 -o grid.net.xml

# Generate 200 vehicles over 1000 seconds
python $SUMO_HOME/tools/randomTrips.py -n grid.net.xml -e 1000 -p 5 -o trips.trips.xml

# Compute routes
duarouter -n grid.net.xml -r trips.trips.xml -o routes.rou.xml --ignore-errors

# Create config file
cat > scenario.sumocfg << 'EOF'
<configuration>
  <input>
    <net-file value="grid.net.xml"/>
    <route-files value="routes.rou.xml"/>
  </input>
  <time>
    <begin value="0"/>
    <end value="1000"/>
  </time>
  <output>
    <tripinfo-output value="tripinfo.xml"/>
    <summary-output value="summary.xml"/>
  </output>
</configuration>
EOF

# Run simulation
sumo -c scenario.sumocfg

# Convert output to CSV
python $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml
```

### Example 2: OSM Import

```bash
# Download OSM data (using SUMO tools)
python $SUMO_HOME/tools/osmGet.py --bbox 116.3,39.9,116.5,40.0 --output map.osm.xml

# Convert to SUMO network
netconvert --osm map.osm.xml -o map.net.xml --tls.guess true

# Generate trips and routes
python $SUMO_HOME/tools/randomTrips.py -n map.net.xml -e 3600 -p 2 -o trips.trips.xml
duarouter -n map.net.xml -r trips.trips.xml -o routes.rou.xml

# Run with GUI
sumo-gui -c scenario.sumocfg --start
```

### Example 3: Traffic Signal Optimization

```bash
# Generate network with traffic lights
netgenerate --grid --grid.number 3 --grid.length 100 --tls.guess true -o grid.net.xml

# Generate demand
python $SUMO_HOME/tools/randomTrips.py -n grid.net.xml -e 3600 -p 1 -o trips.trips.xml
duarouter -n grid.net.xml -r trips.trips.xml -o routes.rou.xml

# Run signal optimization (requires tlsCycleAdaptation.py)
python $SUMO_HOME/tools/tlsCycleAdaptation.py -n grid.net.xml -r routes.rou.xml -o tls_opt.add.xml

# Run simulation with optimized signals
sumo -c scenario.sumocfg --additional-files tls_opt.add.xml
```

## 🔧 Troubleshooting

### Common Issues

#### Issue 1: "sumo: command not found"

**Cause:** SUMO not installed or not in PATH

**Solution:**
```bash
# Verify SUMO_HOME is set
echo $SUMO_HOME  # Linux/macOS
echo %SUMO_HOME%  # Windows

# Add to PATH
export PATH="$SUMO_HOME/bin:$PATH"  # Linux/macOS
set PATH=%SUMO_HOME%\bin;%PATH%  # Windows CMD
```

#### Issue 2: "ModuleNotFoundError: No module named 'sumolib'"

**Cause:** Python tools dependencies not installed

**Solution:**
```bash
pip install sumolib traci
# Or install all tool dependencies
pip install -r $SUMO_HOME/tools/requirements.txt
```

#### Issue 3: "Error: Could not locate SUMO executable"

**Cause:** SUMO_HOME not set correctly

**Solution:**
```bash
# Find SUMO installation
which sumo  # Linux/macOS
where sumo  # Windows

# Set SUMO_HOME to parent directory of bin/
export SUMO_HOME=/usr/share/sumo  # Adjust path as needed
```

#### Issue 4: TraCI Connection Refused

**Cause:** SUMO not started with --remote-port

**Solution:**
```bash
# Start SUMO as server
sumo -c scenario.sumocfg --remote-port 8813

# Or with GUI
sumo-gui -c scenario.sumocfg --remote-port 8813 --start
```

#### Issue 5: Low Simulation Performance

**Solutions:**
- Use `sumo` instead of `sumo-gui` for batch runs
- Enable libsumo: `export LIBSUMO_AS_TRACI=1`
- Reduce output frequency
- Use step-length control

### Verification Commands

```bash
# Check SUMO version
sumo --version

# Verify environment
python -c "import sumolib; print(sumolib.__file__)"
python -c "import traci; print(traci.__file__)"

# Run smoke test
python sumo-env/scripts/sumo_skills_smoke_test.py
```

## 📋 Best Practices

1. **Always use .sumocfg files** for reproducible simulations
2. **Set random seeds** for reproducible results (`--seed`)
3. **Use absolute paths** in MCP configurations
4. **Enable appropriate outputs** for analysis needs
5. **Test with smoke test** before complex workflows
6. **Version control** your network and route files
7. **Document parameters** used for generation

## 🤝 Skill Routing Guide

| Task | Recommended Skill |
|------|-------------------|
| Install SUMO | sumo-env |
| Fix PATH/SUMO_HOME issues | sumo-env |
| Create network manually | sumo-core |
| Generate grid/spider network | sumo-core or sumo-mcp |
| OSM import | sumo-core or sumo-mcp |
| Generate random trips | sumo-core or sumo-mcp |
| Run simple simulation | sumo-core |
| Multi-step automated workflow | sumo-mcp |
| Real-time TraCI control | sumo-mcp |
| Signal optimization | sumo-mcp |
| RL training | sumo-rl or sumo-mcp |
| Configure outputs | sumo-output |
| Parse/analyze results | sumo-output |

## 📚 Additional Resources

- [Eclipse SUMO Official Documentation](https://sumo.dlr.de/docs/)
- [SUMO GitHub Repository](https://github.com/eclipse-sumo/sumo)
- [SUMO-RL Documentation](https://lucasalegre.github.io/sumo-rl/)
- [SUMO User Mailing List](https://www.eclipse.org/sumo/contact/)

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Eclipse SUMO](https://www.eclipse.org/sumo/) - Traffic simulation platform
- [sumo-rl](https://github.com/LucasAlegre/sumo-rl) - Reinforcement learning framework
- [SUMO-MCP](https://github.com/XRDS76354/SUMO-MCP-Server) - MCP server for SUMO automation

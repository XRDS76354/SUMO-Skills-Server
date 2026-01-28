# SUMO-Skills: 综合交通仿真技能集合

<div align="center">
  <br />
  <p align="center">
    <a href="#"><img src="https://img.shields.io/badge/状态-活跃-success" alt="Status" /></a>
    <a href="https://www.eclipse.org/sumo/"><img src="https://img.shields.io/badge/SUMO-1.20+-blue" alt="SUMO" /></a>
    <a href="#"><img src="https://img.shields.io/badge/Python-3.10+-blue" alt="Python" /></a>
    <a href="#"><img src="https://img.shields.io/badge/许可证-MIT-green" alt="License" /></a>
    <img src="https://img.shields.io/badge/平台-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey" alt="Platform" />
  </p>
</div>

SUMO-Skills 是一套针对 [Eclipse SUMO](https://www.eclipse.org/sumo/)（城市交通仿真）的综合性 AI 技能集合。它为路网创建、需求生成、仿真执行、输出分析、强化学习和基于 MCP 的自动化工作流提供结构化指导和最佳实践。

## 📚 概述

本技能集合分为五个专业模块：

| 技能 | 描述 | 使用场景 |
|------|-------------|----------|
| **sumo-core** | 核心 SUMO 工作流和命令行使用 | 标准仿真任务 |
| **sumo-env** | 安装和环境设置 | 安装和配置 |
| **sumo-mcp** | MCP 服务器集成自动化 | 自动化工作流 |
| **sumo-output** | 输出配置和分析 | 结果处理 |
| **sumo-rl** | 交通信号强化学习 | RL 训练 |

## 🚀 快速开始

### 系统要求

- **操作系统**: Windows 10+, Linux (Ubuntu 18.04+), macOS 10.15+
- **Python**: 3.10 或更高版本
- **SUMO**: 1.20.0 或更高版本
- **内存**: 最低 4GB RAM（推荐 8GB）
- **磁盘空间**: 2GB 可用空间

### 安装步骤

#### 步骤 1: 安装 SUMO

**Windows:**
```powershell
# 使用 winget（推荐）
winget install --name sumo

# 或从 https://sumo.dlr.de/ 下载安装程序
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

#### 步骤 2: 配置环境变量

**Windows (PowerShell):**
```powershell
$env:SUMO_HOME="C:\Program Files\Eclipse\sumo"
$env:PATH="$env:SUMO_HOME\bin;$env:PATH"

# 永久设置
[Environment]::SetEnvironmentVariable("SUMO_HOME", "C:\Program Files\Eclipse\sumo", "User")
```

**Linux/macOS:**
```bash
export SUMO_HOME="/usr/share/sumo"  # Linux
# export SUMO_HOME="/usr/local/share/sumo"  # macOS Homebrew
export PATH="$SUMO_HOME/bin:$PATH"

# 添加到 ~/.bashrc 或 ~/.zshrc 以持久化
echo 'export SUMO_HOME="/usr/share/sumo"' >> ~/.bashrc
echo 'export PATH="$SUMO_HOME/bin:$PATH"' >> ~/.bashrc
```

#### 步骤 3: 验证安装

```bash
sumo --version
python sumo-env/scripts/sumo_skills_smoke_test.py
```

## 📖 技能模块

### 1. sumo-core: 核心仿真工作流

将此技能用于标准 SUMO 操作，包括路网创建、需求生成和仿真执行。

**主要功能：**
- 路网生成（`netgenerate`, `netconvert`）
- OSM 导入和转换
- 需求生成（`randomTrips.py`, `od2trips`）
- 路径计算（`duarouter`）
- 仿真执行（`sumo`, `sumo-gui`）
- TraCI 基础

**示例工作流：**
```bash
# 1. 生成网格路网
netgenerate --grid --grid.number 4 --grid.length 100 -o grid.net.xml

# 2. 生成随机行程
python $SUMO_HOME/tools/randomTrips.py -n grid.net.xml -e 3600 -p 1 -o trips.trips.xml

# 3. 计算路径
duarouter -n grid.net.xml -r trips.trips.xml -o routes.rou.xml

# 4. 运行仿真
sumo -c scenario.sumocfg
```

**参考资料：**
- [命令行基础](sumo-core/references/command-line-basics.md)
- [路网构建](sumo-core/references/network-build.md)
- [需求和路由](sumo-core/references/demand-routing.md)
- [仿真运行](sumo-core/references/simulation-run.md)
- [TraCI 基础](sumo-core/references/traci-basics.md)

### 2. sumo-env: 环境设置

将此技能用于 SUMO 安装、环境变量配置和依赖管理。

**主要功能：**
- 跨平台安装指南
- 环境变量设置（SUMO_HOME, PATH）
- Python 工具依赖
- 安装验证

**冒烟测试：**
```bash
python sumo-env/scripts/sumo_skills_smoke_test.py --keep-dir
```

**参考资料：**
- [安装 SUMO](sumo-env/references/install-sumo.md)
- [环境变量](sumo-env/references/env-vars.md)
- [Python 工具](sumo-env/references/python-tools.md)

### 3. sumo-mcp: MCP 自动化

将此技能用于通过模型上下文协议（MCP）实现自动化的多步骤 SUMO 工作流。

**主要功能：**
- 自动化路网生成和转换
- 需求生成和路由
- 通过 TraCI 实时仿真控制
- 交通信号优化
- 强化学习工作流
- 预构建自动化工作流

**可用工具：**
- `manage_network`: 路网生成、OSM 下载、转换
- `manage_demand`: 随机行程、OD 矩阵、路径计算
- `control_simulation`: 连接、步进、断开
- `query_simulation_state`: 车辆列表、变量、仿真统计
- `optimize_traffic_signals`: 周期自适应、协调控制
- `run_workflow`: sim_gen_eval, signal_opt, rl_train
- `manage_rl_task`: 列出场景、自定义训练

**示例工作流：**
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

**参考资料：**
- [MCP 设置](sumo-mcp/references/mcp-setup.md)
- [MCP 工具](sumo-mcp/references/mcp-tools.md)

### 4. sumo-output: 输出分析

将此技能用于配置、生成和分析 SUMO 仿真输出。

**主要功能：**
- 输出类型配置（tripinfo, FCD, summary 等）
- 检测器设置和数据收集
- XML 到 CSV 转换
- 统计分析

**常见输出：**
```bash
# 命令行输出
sumo -c scenario.sumocfg --tripinfo-output tripinfo.xml --fcd-output fcd.xml

# 转换为 CSV
python $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml

# 生成统计信息
python $SUMO_HOME/tools/output/attributeStats.py --element tripinfo --attribute timeLoss tripinfo.xml
```

**参考资料：**
- [输出类型](sumo-output/references/output-types.md)
- [输出工具](sumo-output/references/output-tools.md)
- [输出解析](sumo-output/references/output-parsing.md)

### 5. sumo-rl: 强化学习

将此技能用于基于强化学习的交通信号控制，使用 sumo-rl。

**主要功能：**
- 单智能体（Gymnasium）环境
- 多智能体（PettingZoo）环境
- 自定义观察函数
- 自定义奖励函数
- 与 RL 库集成（stable-baselines3, RLlib）

**示例用法：**
```python
import gymnasium as gym
import sumo_rl

# 单智能体环境
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

**参考资料：**
- [RL 安装](sumo-rl/references/rl-install.md)
- [MDP（观察、动作、奖励）](sumo-rl/references/rl-mdp.md)
- [环境 API](sumo-rl/references/rl-env-api.md)

## ⚙️ 配置

### SUMO 配置文件 (.sumocfg)

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

### 附加文件

**交通灯定义：**
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

**检测器定义：**
```xml
<additional>
  <inductionLoop id="detector_0" lane="edge_0_0" pos="10" 
                 period="60" file="detector_output.xml"/>
</additional>
```

## 🛠️ 使用示例

### 示例 1: 基础网格仿真

```bash
# 创建工作目录
mkdir -p grid_simulation && cd grid_simulation

# 生成 4x4 网格路网
netgenerate --grid --grid.number 4 --grid.length 100 -o grid.net.xml

# 在 1000 秒内生成 200 辆车
python $SUMO_HOME/tools/randomTrips.py -n grid.net.xml -e 1000 -p 5 -o trips.trips.xml

# 计算路径
duarouter -n grid.net.xml -r trips.trips.xml -o routes.rou.xml --ignore-errors

# 创建配置文件
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

# 运行仿真
sumo -c scenario.sumocfg

# 转换输出为 CSV
python $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml
```

### 示例 2: OSM 导入

```bash
# 下载 OSM 数据（使用 SUMO 工具）
python $SUMO_HOME/tools/osmGet.py --bbox 116.3,39.9,116.5,40.0 --output map.osm.xml

# 转换为 SUMO 路网
netconvert --osm map.osm.xml -o map.net.xml --tls.guess true

# 生成行程和路径
python $SUMO_HOME/tools/randomTrips.py -n map.net.xml -e 3600 -p 2 -o trips.trips.xml
duarouter -n map.net.xml -r trips.trips.xml -o routes.rou.xml

# 使用 GUI 运行
sumo-gui -c scenario.sumocfg --start
```

### 示例 3: 交通信号优化

```bash
# 生成带交通灯的路网
netgenerate --grid --grid.number 3 --grid.length 100 --tls.guess true -o grid.net.xml

# 生成需求
python $SUMO_HOME/tools/randomTrips.py -n grid.net.xml -e 3600 -p 1 -o trips.trips.xml
duarouter -n grid.net.xml -r trips.trips.xml -o routes.rou.xml

# 运行信号优化（需要 tlsCycleAdaptation.py）
python $SUMO_HOME/tools/tlsCycleAdaptation.py -n grid.net.xml -r routes.rou.xml -o tls_opt.add.xml

# 使用优化后的信号运行仿真
sumo -c scenario.sumocfg --additional-files tls_opt.add.xml
```

## 🔧 故障排除

### 常见问题

#### 问题 1: "sumo: 命令未找到"

**原因：** SUMO 未安装或不在 PATH 中

**解决方案：**
```bash
# 验证 SUMO_HOME 是否设置
echo $SUMO_HOME  # Linux/macOS
echo %SUMO_HOME%  # Windows

# 添加到 PATH
export PATH="$SUMO_HOME/bin:$PATH"  # Linux/macOS
set PATH=%SUMO_HOME%\bin;%PATH%  # Windows CMD
```

#### 问题 2: "ModuleNotFoundError: No module named 'sumolib'"

**原因：** Python 工具依赖未安装

**解决方案：**
```bash
pip install sumolib traci
# 或安装所有工具依赖
pip install -r $SUMO_HOME/tools/requirements.txt
```

#### 问题 3: "Error: Could not locate SUMO executable"

**原因：** SUMO_HOME 设置不正确

**解决方案：**
```bash
# 查找 SUMO 安装位置
which sumo  # Linux/macOS
where sumo  # Windows

# 将 SUMO_HOME 设置为 bin/ 的父目录
export SUMO_HOME=/usr/share/sumo  # 根据实际路径调整
```

#### 问题 4: TraCI 连接被拒绝

**原因：** SUMO 未使用 --remote-port 启动

**解决方案：**
```bash
# 以服务器模式启动 SUMO
sumo -c scenario.sumocfg --remote-port 8813

# 或使用 GUI
sumo-gui -c scenario.sumocfg --remote-port 8813 --start
```

#### 问题 5: 仿真性能低下

**解决方案：**
- 批处理运行使用 `sumo` 而非 `sumo-gui`
- 启用 libsumo: `export LIBSUMO_AS_TRACI=1`
- 降低输出频率
- 使用步长控制

### 验证命令

```bash
# 检查 SUMO 版本
sumo --version

# 验证环境
python -c "import sumolib; print(sumolib.__file__)"
python -c "import traci; print(traci.__file__)"

# 运行冒烟测试
python sumo-env/scripts/sumo_skills_smoke_test.py
```

## 📋 最佳实践

1. **始终使用 .sumocfg 文件** 以确保仿真可重现
2. **设置随机种子** 以获得可重现的结果 (`--seed`)
3. **在 MCP 配置中使用绝对路径**
4. **根据分析需求启用适当的输出**
5. **在复杂工作流之前使用冒烟测试**
6. **对路网和路由文件进行版本控制**
7. **记录生成所用的参数**

## 🤝 技能路由指南

| 任务 | 推荐技能 |
|------|-------------------|
| 安装 SUMO | sumo-env |
| 修复 PATH/SUMO_HOME 问题 | sumo-env |
| 手动创建路网 | sumo-core |
| 生成网格/蜘蛛路网 | sumo-core 或 sumo-mcp |
| OSM 导入 | sumo-core 或 sumo-mcp |
| 生成随机行程 | sumo-core 或 sumo-mcp |
| 运行简单仿真 | sumo-core |
| 多步骤自动化工作流 | sumo-mcp |
| 实时 TraCI 控制 | sumo-mcp |
| 信号优化 | sumo-mcp |
| RL 训练 | sumo-rl 或 sumo-mcp |
| 配置输出 | sumo-output |
| 解析/分析结果 | sumo-output |

## 📚 额外资源

- [Eclipse SUMO 官方文档](https://sumo.dlr.de/docs/)
- [SUMO GitHub 仓库](https://github.com/eclipse-sumo/sumo)
- [SUMO-RL 文档](https://lucasalegre.github.io/sumo-rl/)
- [SUMO 用户邮件列表](https://www.eclipse.org/sumo/contact/)

## 📄 许可证

本项目采用 MIT 许可证。

## 🙏 致谢

- [Eclipse SUMO](https://www.eclipse.org/sumo/) - 交通仿真平台
- [sumo-rl](https://github.com/LucasAlegre/sumo-rl) - 强化学习框架
- [SUMO-MCP](https://github.com/XRDS76354/SUMO-MCP-Server) - SUMO 自动化 MCP 服务器

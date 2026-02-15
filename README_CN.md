# SUMO-Skills：面向 AI 助手的 SUMO 仿真技能库

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

`SUMO-Skills` 是一套为 **AI 编程助手** 准备的 SUMO 专项技能集合。  
它不是一个新的仿真引擎，也不是 Python SDK，而是把常见 SUMO 工作拆成可复用的技能模块（`SKILL.md + references`），让助手在做交通仿真任务时更稳定地给出可执行方案。

## 什么是 SUMO-Skills

你可以把它理解为一套“交通仿真任务操作系统”：

- 统一任务拆解：从环境安装、路网生成、需求建模到仿真运行与结果分析
- 统一路由规则：不同问题自动匹配到对应技能（env/core/output/mcp/rl）
- 统一命令风格：减少“只讲概念，不给命令”的情况
- 统一协作接口：可在 Code、Claude Code、Trae、Cursor 等工具里复用

## 仓库包含什么

```text
sumo-env/      环境安装、SUMO_HOME/PATH、冒烟测试
sumo-core/     路网、需求、路由、仿真运行、TraCI 基础
sumo-output/   输出配置、检测器、XML/CSV 转换、统计分析
sumo-mcp/      MCP 工作流设计与工具参数说明
sumo-rl/       基于 sumo-rl 的信号控制强化学习
```

## 功能总览

| 模块 | 解决的问题 | 典型输出 |
|---|---|---|
| `sumo-env` | SUMO 安装失败、`SUMO_HOME`/`PATH` 错误、工具不可用 | 可运行环境 + 验证结果 |
| `sumo-core` | 从 0 到 1 跑通仿真（net -> trips -> routes -> sumo） | `.net.xml` / `.rou.xml` / `.sumocfg` |
| `sumo-output` | 需要 tripinfo/FCD/summary/检测器统计 | 结构化输出文件与分析命令 |
| `sumo-mcp` | 多步骤自动化、在线 TraCI 控制、流程编排 | MCP 工具调用与工作流方案 |
| `sumo-rl` | 信号控制强化学习实验设计与训练 | 训练配置与实验脚本框架 |

## 5 分钟上手

### 1) 安装并验证 SUMO

```bash
sumo --version
```

若未安装，可参考：

- Windows: `winget install --name sumo`
- Ubuntu/Debian: `sudo apt-get install sumo sumo-tools sumo-doc`
- macOS: `brew install sumo`

### 2) 配置环境变量

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

### 3) 运行仓库冒烟测试

```bash
python sumo-env/scripts/sumo_skills_smoke_test.py
```

## 在 Code、Claude Code、Trae、Cursor 上如何配合

核心原则先统一：

1. 把本仓库作为项目上下文（workspace）
2. 每次提问都写清楚目标、输入文件、约束和输出格式
3. 明确点名技能模块（如 `sumo-core`、`sumo-output`）
4. 让助手先给“可执行步骤 + 命令”，再让它落地改文件

### Code（Codex / 命令行代理）

推荐做法：

- 在项目规则文件中声明技能路由（例如 AGENTS 规则）
- 提问时直接点名技能
- 让助手在本地执行命令并回传关键结果

示例提问：

```text
使用 sumo-core：在当前目录生成 4x4 网格路网，仿真 1000 秒，输出 tripinfo.xml，并给出完整命令。
```

### Claude Code

推荐做法：

- 在项目说明文件中写入技能路由（常见是 `CLAUDE.md`）
- 把本仓库路径和 SUMO 环境变量告知助手
- 对复杂任务分两步：先方案，后执行

示例提问：

```text
请按 sumo-env -> sumo-core -> sumo-output 的顺序执行：
1) 检查环境
2) 运行一个最小仿真
3) 把输出转换为 CSV
```

### Trae

推荐做法：

- 在 Trae 的项目规则/记忆中加入“技能路由表”
- 固定协作模板：`目标 -> 现有文件 -> 约束 -> 期望产物`
- 让助手先生成命令草案，再确认执行

示例提问：

```text
使用 sumo-output：帮我给 scenario.sumocfg 增加 tripinfo 和 summary 输出，并给出后处理统计命令。
```

### Cursor

推荐做法：

- 在 Cursor 的 Project Rules（如 `.cursor/rules` 或 `.cursorrules`）写入技能路由
- 把“优先给可运行命令和文件改动”的规则放在第一条
- 对改动要求带文件路径和补丁说明，便于审查

示例提问：

```text
使用 sumo-rl：基于现有 net/route 文件创建一个最小单智能体训练脚本，并说明关键超参数。
```

## 一套通用提示词模板（四个平台都能用）

```text
你现在作为 SUMO 工程助手工作。
优先技能：sumo-env / sumo-core / sumo-output / sumo-mcp / sumo-rl（按任务选择）。

目标：
已知输入：
约束条件：
期望输出：
- 先给执行计划（编号）
- 再给可直接运行的命令
- 若要改文件，列出将修改的文件路径
```

## 常见工作流

### 工作流 1：最小可运行仿真（core）

```bash
netgenerate --grid --grid.number 4 --grid.length 100 -o grid.net.xml
python $SUMO_HOME/tools/randomTrips.py -n grid.net.xml -e 1000 -p 5 -o trips.trips.xml
duarouter -n grid.net.xml -r trips.trips.xml -o routes.rou.xml
sumo -c scenario.sumocfg
```

### 工作流 2：输出与统计（output）

```bash
sumo -c scenario.sumocfg --tripinfo-output tripinfo.xml --summary-output summary.xml
python $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml
python $SUMO_HOME/tools/output/attributeStats.py --element tripinfo --attribute timeLoss tripinfo.xml
```

### 工作流 3：自动化编排（mcp）

- 使用 `sumo-mcp` 设计网络生成、需求生成、仿真控制、信号优化等多步骤流程
- 适合“要自动跑一整条链路”的任务
- 注意：MCP 服务器需要你在本地单独配置（本仓库提供的是技能说明与参数参考）

## 技能路由速查

| 你要做的事 | 优先技能 |
|---|---|
| 安装 SUMO、修环境变量 | `sumo-env` |
| 生成路网、车辆需求、运行仿真 | `sumo-core` |
| 配置 tripinfo/FCD/检测器并做统计 | `sumo-output` |
| 多步骤自动化、TraCI 在线控制 | `sumo-mcp` |
| 信号控制强化学习 | `sumo-rl` |

## 额外资源

- [Eclipse SUMO 官方文档](https://sumo.dlr.de/docs/)
- [SUMO GitHub 仓库](https://github.com/eclipse-sumo/sumo)
- [sumo-rl 项目](https://github.com/LucasAlegre/sumo-rl)

## 许可证

MIT

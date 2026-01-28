---
name: sumo-output
description: Configure, generate, and analyze SUMO simulation outputs such as tripinfo, fcd, summary, vehroute, detectors, and edge/lane measures. Use when the task involves output options, additional-file detectors, conversion to CSV, or output statistics.
---

# Sumo Output

## Overview
Use this skill to decide which SUMO outputs to enable, how to enable them, and how to parse or summarize the results.

## Skill Routing
- Use sumo-core to run the simulation itself or to build networks and routes.
- Use sumo-env for installation or SUMO_HOME issues.
- Use sumo-mcp when output generation requires automated tool execution or multi-step workflows.
- Use sumo-rl for RL-specific metrics and training logs.

## Output Workflow
1. Choose output type and aggregation level.
2. Enable via command line options or additional files.
3. Run the simulation.
4. Convert or analyze outputs with tools.

## References
- Output types and enablement: references/output-types.md
- Output tools (detectors and stats): references/output-tools.md
- Parsing and conversion: references/output-parsing.md

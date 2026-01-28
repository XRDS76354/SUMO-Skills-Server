---
name: sumo-mcp
description: Model Context Protocol integration for SUMO. Use when a task needs automated multi-step SUMO workflows, programmatic tool execution, live TraCI control, or RL training via MCP tools. Avoid for simple command hints or static config edits.
---

# Sumo MCP

## Overview
Use this skill to drive SUMO through the MCP server tools for automation, live control, or complex workflows.

## When to Use MCP
- Use MCP for multi-step pipelines (network -> demand -> routes -> run -> analysis).
- Use MCP for live TraCI control or state queries during a running simulation.
- Use MCP for signal optimization or RL training workflows.

## When to Avoid MCP
- Avoid MCP for simple command suggestions or static file edits.
- Use sumo-core or sumo-output when no tool execution is required.

## Tooling Map
- manage_network: generate, convert/convert_osm, download_osm
- manage_demand: generate_random/random_trips, convert_od/od_matrix, compute_routes/routing
- control_simulation: connect, step, disconnect
- query_simulation_state: vehicle_list, vehicle_variable, simulation
- optimize_traffic_signals: cycle_adaptation/Websters, coordination
- run_workflow: sim_gen_eval, signal_opt, rl_train
- manage_rl_task: list_scenarios, train_custom

## Preflight
- Verify SUMO_HOME and PATH.
- Ensure the MCP server is configured with absolute paths.

## References
- Server setup and client config: references/mcp-setup.md
- Tool actions and parameters: references/mcp-tools.md

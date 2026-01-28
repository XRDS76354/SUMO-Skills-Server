---
name: sumo-env
description: "Install and configure SUMO and its tooling: downloads, PATH and SUMO_HOME setup, Python tool dependencies, and verification steps on Windows/Linux/macOS. Use for setup, environment errors, or missing executables/tools."
---

# Sumo Env

## Overview
Use this skill to set up SUMO and its tooling, fix environment variable issues, and verify installations.

## Skill Routing
- Use sumo-core for simulation workflows once SUMO is installed.
- Use sumo-output for output options and parsing.
- Use sumo-mcp for MCP server setup or tool execution workflows.
- Use sumo-rl for RL library installation and training details.

## Setup Checklist
1. Install SUMO (binary, package manager, or source).
2. Set SUMO_HOME and add SUMO_HOME/bin to PATH.
3. Verify with `sumo --version`.
4. Install Python tool dependencies if using SUMO tools.

## Scripts
- scripts/sumo_skills_smoke_test.py: Cross-platform smoke test for SUMO CLI and tools.

## References
- Install SUMO: references/install-sumo.md
- Environment variables: references/env-vars.md
- Python tools and packages: references/python-tools.md

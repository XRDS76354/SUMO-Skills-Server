---
name: sumo-rl
description: Reinforcement learning traffic signal control with sumo-rl, including SumoEnvironment setup, Gymnasium/PettingZoo APIs, observation/action/reward design, and training workflows. Use for RL signal control tasks or when SUMO-RL is requested.
---

# Sumo RL

## Overview
Use this skill to design and run RL traffic signal control experiments with sumo-rl.

## Skill Routing
- Use sumo-env for installing SUMO or Python dependencies.
- Use sumo-core to build networks, routes, and traffic light definitions.
- Use sumo-mcp for automated RL training workflows or tool execution.
- Use sumo-output for output analysis outside RL logs.

## RL Workflow
1. Prepare a network with traffic lights and a route file.
2. Choose single-agent (Gymnasium) or multi-agent (PettingZoo) API.
3. Select observation and reward functions.
4. Train with your RL library or built-in examples.

## Requirements
- SUMO_HOME set and SUMO executables available.
- Traffic lights must exist in the network for signal control.

## References
- Installation: references/rl-install.md
- Observations, actions, rewards: references/rl-mdp.md
- Gymnasium and PettingZoo APIs: references/rl-env-api.md

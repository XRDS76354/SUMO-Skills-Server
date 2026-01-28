# TraCI Basics

## Start sumo as a server
- Headless:
  sumo -c scenario.sumocfg --remote-port 8813
- GUI:
  sumo-gui -c scenario.sumocfg --remote-port 8813 --start

## Multiple clients
- Use --num-clients N and set a client execution order.

## Notes
- When TraCI is active, sumo ignores --end and runs until the client closes.
- Use libsumo for higher performance when GUI is not required.

## MCP handoff
- Use sumo-mcp for automated TraCI control workflows.

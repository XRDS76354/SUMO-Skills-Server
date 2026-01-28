# MCP Setup

## Requirements
- Python 3.10+
- SUMO installed with sumo on PATH
- SUMO_HOME set for tools
- Python deps: mcp[cli], sumolib, traci, sumo-rl, pandas, requests

## Start server
- Direct:
  python src/server.py
- Helper scripts:
  start_server.ps1 / start_server.bat / start_server.sh

## Client config (absolute paths required)
```json
{
  "mcpServers": {
    "sumo-mcp": {
      "command": "C:/Path/To/python.exe",
      "args": ["C:/Path/To/sumo-mcp/src/server.py"],
      "env": {
        "SUMO_HOME": "C:/Path/To/sumo",
        "PYTHONPATH": "C:/Path/To/sumo-mcp/src"
      }
    }
  }
}
```

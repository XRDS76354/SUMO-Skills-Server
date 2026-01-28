# Environment Variables

## Windows
- SUMO_HOME should point to the base directory containing bin/ and tools/.
- PowerShell session example:
  $env:SUMO_HOME="C:\Program Files\Eclipse\sumo"
  $env:PATH="$env:SUMO_HOME\bin;$env:PATH"
- For persistence, use setx or the System Environment Variables UI.
- start-command-line.bat can open a preconfigured shell.

## Linux
- Session example:
  export SUMO_HOME="/usr/share/sumo"
  export PATH="$SUMO_HOME/bin:$PATH"
- Add to ~/.bashrc for persistence.

## macOS
- Add to ~/.zshrc or ~/.bash_profile:
  export SUMO_HOME="/your/path/to/sumo"
  export PATH="$SUMO_HOME/bin:$PATH"

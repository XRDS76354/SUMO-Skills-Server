# Install SUMO

## Windows
- Use the official installer or zip.
- Winget:
  winget install --name sumo
- Ensure sumo.exe is in PATH after install.

## Linux (Ubuntu/Debian)
- Install from the stable PPA:
  sudo add-apt-repository ppa:sumo/stable
  sudo apt-get update
  sudo apt-get install sumo sumo-tools sumo-doc

## macOS
- Use the official .pkg installer.
- Ensure XQuartz and Python are installed.

## Verify
- Run:
  sumo --version

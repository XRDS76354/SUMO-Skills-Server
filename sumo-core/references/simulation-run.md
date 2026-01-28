# Running Simulations

## Command line
- Run headless:
  sumo -c scenario.sumocfg
- Run with GUI:
  sumo-gui -c scenario.sumocfg

## Inputs
- net-file: .net.xml
- route-files: .rou.xml
- additional-files: detectors, traffic lights, outputs, vTypes, routes

## Additional files
- Use an <additional> root element.
- Load via --additional-files or in the .sumocfg.

## Tips
- Use --begin and --end to set time bounds.
- Use --start with sumo-gui to auto-start the simulation.

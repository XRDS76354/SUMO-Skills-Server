# MCP Tools and Parameters

## Common conventions
- All tools return a string. Errors start with "Error:".
- Some tools accept params.options (list of strings) to pass extra CLI tokens.

## manage_network
- action: generate | convert | convert_osm | download_osm
- output_file: output path (directory for download_osm)
- params:
  - generate: {grid: bool, grid_number: int, spider: bool}
  - convert/convert_osm: {osm_file: string}
  - download_osm: {bbox: "w,s,e,n", prefix: string}

## manage_demand
- action: generate_random | random_trips | convert_od | od_matrix | compute_routes | routing
- net_file: .net.xml
- output_file: output path
- params:
  - generate_random/random_trips: {end_time: int, end: int, period: float}
  - convert_od/od_matrix: {od_file: string}
  - compute_routes/routing: {route_files: string}

## control_simulation
- action: connect | step | disconnect
- params:
  - connect: {config_file: string, gui: bool, port: int, host: string}
  - step: {step: float} (default 0 means one step)

## query_simulation_state
- target: vehicle_list | vehicles | vehicle_variable | simulation
- params:
  - vehicle_variable: {vehicle_id: string, variable: speed|position|acceleration|lane|route}

## optimize_traffic_signals
- method: cycle_adaptation | Websters | coordination
- net_file, route_file, output_file
- output is an <additional> file; load via --additional-files

## run_workflow
- workflow_name: sim_gen_eval | signal_opt | rl_train
- sim_gen_eval params: {grid_number, sim_seconds, output_dir}
- signal_opt params: {net_file, route_file, sim_seconds, use_coordinator, output_dir}
- rl_train params: {scenario_name, episodes, steps, output_dir}

## manage_rl_task
- action: list_scenarios | train_custom
- train_custom params (either):
  - scenario-based: {scenario/scenario_name, output_dir, episodes, steps, algorithm, reward_type}
  - file-based: {net_file, route_file, output_dir, episodes, steps, algorithm, reward_type}
- algorithm currently supports ql

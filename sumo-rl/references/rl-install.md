# Install SUMO-RL

## Install SUMO
- Install SUMO and set SUMO_HOME (see sumo-env).
- Optional performance: export LIBSUMO_AS_TRACI=1 (no GUI, no parallel sims).

## Install sumo-rl
- Stable release:
  pip install sumo-rl
- Latest version:
  git clone https://github.com/LucasAlegre/sumo-rl
  cd sumo-rl
  pip install -e .

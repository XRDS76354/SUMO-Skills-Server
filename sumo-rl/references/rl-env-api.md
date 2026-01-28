# Gymnasium and PettingZoo APIs

## Gymnasium (single-agent)
```python
import gymnasium as gym
import sumo_rl

env = gym.make(
    "sumo-rl-v0",
    net_file="path/to/net.net.xml",
    route_file="path/to/routes.rou.xml",
    out_csv_name="path/to/output.csv",
    use_gui=False,
    num_seconds=1000,
)
obs, info = env.reset()
terminated = truncated = False
while not (terminated or truncated):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
```

## PettingZoo (multi-agent)
```python
import sumo_rl

env = sumo_rl.parallel_env(
    net_file="path/to/net.net.xml",
    route_file="path/to/routes.rou.xml",
    use_gui=False,
    num_seconds=3600,
)
observations = env.reset()
while env.agents:
    actions = {agent: env.action_space(agent).sample() for agent in env.agents}
    observations, rewards, terminations, truncations, infos = env.step(actions)
```

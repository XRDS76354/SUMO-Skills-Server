# MDP: Observations, Actions, Rewards

## Observation (default)
obs = [phase_one_hot, min_green, lane_i_density..., lane_i_queue...]
- phase_one_hot: current green phase as one-hot
- min_green: whether min_green time has passed
- lane_i_density: vehicles / lane capacity
- lane_i_queue: queued vehicles / lane capacity

## Action
- Discrete actions select the next green phase every delta_time.
- Each green change is preceded by a yellow phase of yellow_time.

## Reward
- Default reward: change in cumulative vehicle delay.
- Customize with reward_fn in SumoEnvironment.

## Custom observation
- Implement ObservationFunction and pass it to the environment.

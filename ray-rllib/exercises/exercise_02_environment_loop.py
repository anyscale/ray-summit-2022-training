# Solution to Exercise #1
# ...

import time
from ipywidgets import Output
from IPython import display
import time


# Construct the environment object.
env = MultiAgentArena()
# Call the env's `reset()` method to start a new episode.
obs = env.reset()

while True:
    # Compute actions separately for each agent.
    a1 = env.action_space.sample()
    a2 = env.action_space.sample()

    # Send the action-dict to the env, using the `step()` method.
    obs, rewards, dones, _ = env.step({"agent1": a1, "agent2": a2})

    # Get a rendered image from the env.
    out.clear_output(wait=True)
    env.render()
    time.sleep(0.1)

    # If agent1 is done (feel free to check for agent2; they should be done at the same time) ...
    # -> break out of the loop.
    if dones["agent1"]:
        break

# Solution to Exercise #1
# ...

from ipywidgets import Output
from IPython import display
import time


# Construct the environment object.
env = MultiAgentArena()
# Call the env's `reset()` method to start a new episode.
obs = env.reset()

# Render in notebook in place.
with env.out:

    env.render()

    while True:

        # Compute actions separately for each agent.
        actions = env.action_space.sample()

        # Send the action-dict to the env, using the `step()` method.
        obs, rewards, dones, _ = env.step(actions)

        # Get a rendered image from the env.
        env.render()

        # If agent1 is done (feel free to check for agent2; they should be done at the same time) ...
        # -> break out of the loop.
        if dones["agent1"]:
            break

# To setup a simple offline RL experiment, using RLlib's BC (behavioral cloning) Algorithm:

import os
import re

from ray.rllib.algorithms.bc import BCConfig
from ray.rllib.examples.env.recommender_system_envs_with_recsim import InterestEvolutionRecSimEnv

# Offline input (JSON) file:
output_dir = "offline_rl/"
all_output_files = os.listdir(os.path.dirname(output_dir + "/"))
json_output_file = os.path.join(output_dir, [f for f in all_output_files if re.match("^.*worker.*\.json$", f)][0])

# The following env config must match the environment that was used for recording the JSON data.
interest_evolution_env = InterestEvolutionRecSimEnv({
    "num_candidates": 20,
    "slate_size": 2,
    "wrap_for_bandits": False,  # SlateQ != Bandit
    "convert_to_discrete_action_space": False,
})

offline_rl_config = BCConfig()
offline_rl_config.offline_data(
    # Specify your offline RL algo's historic (JSON) inputs:
    # Note: For non-offline RL algos, this is set to "sampler" by default.
    #"input": "sampler",
    input_=[json_output_file],
)

offline_rl_config.environment(
    # Since we don't have an environment and the obs/action-spaces are not defined in the JSON file,
    # we need to provide these here manually.
    observation_space=interest_evolution_env.observation_space,
    action_space=interest_evolution_env.action_space,
)

# Create a behavior cloning (BC) Trainer.
algo = offline_rl_config.build()

# Perform a single iteration and print out results.
print(algo.train())

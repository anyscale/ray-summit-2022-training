# Perform the `tune.run()` call here:
from ray import tune

results = tune.run(
    # Registered name for the CRR Algorithm.
    "CRR",
    # Use our config -> converted to python dict.
    config=config.to_dict(),
    # Stopping criteria.
    stop={
        "timesteps_total": 2000000,
        "evaluation/episode_reward_mean": -300.0,
    },
    # Create checkpoint every iteration.
    checkpoint_freq=1,
    local_dir="results",
    verbose=2,
)

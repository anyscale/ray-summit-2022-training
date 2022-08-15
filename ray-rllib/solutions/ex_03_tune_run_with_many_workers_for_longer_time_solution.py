# Change the config as stated in the exercise task:
config.rollouts(
    num_rollout_workers=5,
    num_envs_per_worker=5,
)

# Undo our tune hyperparameter search:
config.training(
    lr=0.0001,
    train_batch_size=4000,
)

# Run the experiment for 180 iterations:
experiment_results = tune.run(
    "PPO",
    config=config.to_dict(),
    stop={
        "training_iteration": 180,
    },
    # redirect logs instead of default ~/ray_results/
    local_dir="results",
    checkpoint_freq=10,
    checkpoint_at_end=True,
    verbose=1,
    metric="episode_reward_mean",
    mode="max",
)

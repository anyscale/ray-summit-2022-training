# Add the following training settings to your CRR config:
config.training(
    gamma=0.99,
    train_batch_size=1024,
    target_network_update_freq=1,
    tau=0.0001,
    weight_type="exp",
)

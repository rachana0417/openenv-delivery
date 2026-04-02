from env.environment import DeliveryEnv

env = DeliveryEnv(grid_size=5, num_deliveries=1)

state = env.reset()
print("Initial State:", state)

for _ in range(5):
    action = "RIGHT"
    state, reward, done, _ = env.step(action)
    print("State:", state)
    print("Reward:", reward)
    print("Done:", done)
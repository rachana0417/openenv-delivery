from env.environment import DeliveryEnv

def easy_task():
    return DeliveryEnv(grid_size=5, num_deliveries=1)
    

def medium_task():
    return DeliveryEnv(grid_size=6, num_deliveries=2)

def hard_task():
    return DeliveryEnv(grid_size=7, num_deliveries=3)
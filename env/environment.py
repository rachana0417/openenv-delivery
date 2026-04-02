import random

class DeliveryEnv:
    def __init__(self, grid_size=5, num_deliveries=1):
        self.grid_size = grid_size
        self.num_deliveries = num_deliveries
        self.reset()

    def reset(self):
        # Agent starts at random position
        self.agent_pos = [
            random.randint(0, self.grid_size - 1),
            random.randint(0, self.grid_size - 1)
        ]

        # Generate delivery locations
        self.delivery_locations = []
        for _ in range(self.num_deliveries):
            loc = [
                random.randint(0, self.grid_size - 1),
                random.randint(0, self.grid_size - 1)
            ]
            self.delivery_locations.append(loc)

        self.delivered = [False] * self.num_deliveries
        self.steps = 0

        return self.state()

    def state(self):
        return {
            "agent_position": self.agent_pos,
            "delivery_locations": self.delivery_locations,
            "delivered": self.delivered,
            "steps": self.steps
        }

    def step(self, action):
        reward = -1  # penalty for each move
        done = False

        # Movement actions
        if action == "UP":
            self.agent_pos[1] = max(0, self.agent_pos[1] - 1)
        elif action == "DOWN":
            self.agent_pos[1] = min(self.grid_size - 1, self.agent_pos[1] + 1)
        elif action == "LEFT":
            self.agent_pos[0] = max(0, self.agent_pos[0] - 1)
        elif action == "RIGHT":
            self.agent_pos[0] = min(self.grid_size - 1, self.agent_pos[0] + 1)

        elif action == "DELIVER":
            delivered_flag = False
            for i, loc in enumerate(self.delivery_locations):
                if self.agent_pos == loc and not self.delivered[i]:
                    self.delivered[i] = True
                    reward += 10
                    delivered_flag = True

            if not delivered_flag:
                reward -= 5  # wrong delivery

        self.steps += 1

        # Check if all deliveries done
        if all(self.delivered):
            done = True
            reward += 20  # bonus for completion

        return self.state(), reward, done, {}
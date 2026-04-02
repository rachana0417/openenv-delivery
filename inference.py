import os
import requests

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT", "DELIVER"]


def run_task(task_name):
    print("[START]")
    print(f"task: {task_name}")

    # Reset environment
    res = requests.get(f"{API_BASE_URL}/reset", params={"task": task_name})
    state = res.json()["state"]

    done = False
    steps = 0

    while not done and steps < 20:
        action = ACTIONS[steps % len(ACTIONS)]

        res = requests.post(
            f"{API_BASE_URL}/step",
            json={"action": action}
        )

        data = res.json()
        state = data["state"]
        reward = data["reward"]
        done = data["done"]

        print("[STEP]")
        print(f"action: {action}")
        print(f"reward: {reward}")
        print(f"done: {done}")

        steps += 1

    # Simple scoring
    if done:
        score = 1.0
    else:
        score = 0.0

    print("[END]")
    print(f"score: {score}")


if __name__ == "__main__":
    for task in ["easy", "medium", "hard"]:
        run_task(task)
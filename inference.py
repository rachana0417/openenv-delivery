import os
import requests
from openai import OpenAI

# ===============================
# REQUIRED ENV VARIABLES
# ===============================
API_BASE_URL = os.getenv("API_BASE_URL", "https://rachana0417-openenv-delivery.hf.space")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# ===============================
# LOG FORMAT FUNCTIONS
# ===============================
def log_start():
    print("[START] OpenEnv Inference Started")

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward} done={done}")

def log_end(score):
    print(f"[END] Final Score: {score}")

# ===============================
# SIMPLE AGENT LOGIC
# ===============================
def run_episode():
    # Reset environment
    response = requests.get(f"{API_BASE_URL}/reset?task=easy").json()
    state = response["state"]

    done = False
    step_count = 0
    total_reward = 0

    actions = ["up", "down", "left", "right"]

    while not done and step_count < 20:
        action = actions[step_count % 4]

        res = requests.post(
            f"{API_BASE_URL}/step",
            json={"action": action}
        ).json()

        state = res["state"]
        reward = res["reward"]
        done = res["done"]

        total_reward += reward
        step_count += 1

        log_step(step_count, action, reward, done)

    return total_reward


# ===============================
# MAIN
# ===============================
if __name__ == "__main__":
    log_start()

    score = run_episode()

    # Normalize score between 0 and 1
    final_score = max(0.0, min(1.0, score / 20))

    log_end(final_score)
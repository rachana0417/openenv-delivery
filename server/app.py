from fastapi import FastAPI
from tasks.tasks import easy_task

app = FastAPI()

env = easy_task()

@app.get("/")
def home():
    return {"message": "OpenEnv Delivery Running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: str):
    state, reward, done, _ = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def state():
    return env.state()
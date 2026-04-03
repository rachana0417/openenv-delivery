from fastapi import FastAPI
from pydantic import BaseModel
from tasks.tasks import easy_task, medium_task, hard_task

# ✅ FIRST define app
app = FastAPI()

# ✅ THEN use @app
@app.get("/")
def home():
    return {"message": "OpenEnv API is running 🚀"}

# Global environment variable
env = None


class ActionRequest(BaseModel):
    action: str


# ✅ FIX: support BOTH GET and POST
@app.get("/reset")
@app.post("/reset")
def reset(task: str = "easy"):
    global env

    if task == "easy":
        env = easy_task()
    elif task == "medium":
        env = medium_task()
    elif task == "hard":
        env = hard_task()
    else:
        return {"error": "Invalid task"}

    state = env.reset()
    return {"state": state}


@app.post("/step")
def step(request: ActionRequest):
    global env

    if env is None:
        return {"error": "Environment not initialized. Call /reset first."}

    state, reward, done, _ = env.step(request.action)

    return {
        "state": state,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def get_state():
    global env

    if env is None:
        return {"error": "Environment not initialized"}

    return {"state": env.state()}
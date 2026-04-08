from fastapi import FastAPI
from pydantic import BaseModel
from app.env import CustomerSupportEnv

app = FastAPI()
env = CustomerSupportEnv()


class Action(BaseModel):
    action: str


@app.get("/")
def home():
    return {"message": "Customer Support OpenEnv is running"}


@app.get("/reset")
@app.post("/reset")
def reset():
    return {"state": env.reset()}


@app.get("/step")
@app.post("/step")
def step(action: Action):
    state, reward, done = env.step(action.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def state():
    return {"state": env.state()}

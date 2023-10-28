from fastapi import FastAPI

from app.configs.Environment import get_environment_variables

app = FastAPI()

env = get_environment_variables()


@app.get("/")
async def root():
    return {"message": f"Hello World! Running {env.APP_NAME}({env.API_VERSION})"}
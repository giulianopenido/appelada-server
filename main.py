from fastapi import FastAPI

from app.configs.Database import init_database
from app.configs.Environment import get_environment_variables
from app.routers.GroupRouter import router as GroupRouter
from app.routers.UserRouter import router as UserRouter
from app.services.OTPService import OTPService
from app.routers.AuthRouter import router as AuthRouter

app = FastAPI()

env = get_environment_variables()

app.include_router(AuthRouter)
app.include_router(UserRouter)
app.include_router(GroupRouter)


@app.on_event("startup")
async def start_db():
    await init_database()


@app.get("/")
async def root():
    OTPService().verify_otp(destinationNumber="+5531991311910", otp='94586')

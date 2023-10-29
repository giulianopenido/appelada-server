from fastapi import FastAPI

from app.configs.Database import init_database
from app.configs.Environment import get_environment_variables
from app.services.OTPService import OTPService

app = FastAPI()

env = get_environment_variables()


@app.on_event("startup")
async def start_db():
    await init_database()


@app.get("/")
async def root():
    OTPService().verify_otp(destinationNumber="+5531991311910", otp='94586')


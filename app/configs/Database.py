from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.configs.Environment import get_environment_variables
from app.models.Group import Group, Member
from app.models.User import User

env = get_environment_variables()


async def init_database():
    client = AsyncIOMotorClient(env.DATABASE_CONNECTION_STRING)

    # Initialize beanie with the Sample document class and a database
    await init_beanie(
        database=client.Appelada,
        document_models=[
            User,
            Group,
        ]
    )

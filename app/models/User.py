from datetime import datetime
from enum import Enum

from beanie import Document


class SkillFulFoot(Enum):
    RIGHT_FOOT = "rightFoot"
    LEFT_FOOT = "leftFoot"
    AMBIDEXTROUS = "ambidextrous"


class User(Document):
    phone: str
    name: str
    birthDate: datetime
    skillfulFoot: SkillFulFoot

    class Settings:
        name = "Users"

from datetime import datetime
from enum import Enum
from typing import List, Optional

from beanie import Document, Link
from pydantic import BaseModel


class SkillFulFoot(Enum):
    RIGHT_FOOT = "rightFoot"
    LEFT_FOOT = "leftFoot"
    AMBIDEXTROUS = "ambidextrous"


class User(Document):
    phone: str
    name: str
    birthDate: datetime
    skillfulFoot: SkillFulFoot
    groups: List[str] = []

    class Settings:
        name = "Users"


class Member(BaseModel):
    user: Link[User]
    speed: Optional[int] = None
    defense: Optional[int] = None
    passing: Optional[int] = None
    shooting: Optional[int] = None
    stamina: Optional[int] = None
    dribble: Optional[int] = None

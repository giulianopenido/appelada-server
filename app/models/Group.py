from typing import List

from beanie import Document, Link

from app.models.User import User, Member


class Group(Document):
    name: str
    description: str
    creator: Link[User]
    members: List[Member] = []

    class Settings:
        name = "Groups"

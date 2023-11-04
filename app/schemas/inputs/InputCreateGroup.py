from pydantic import BaseModel


class InputCreateGroup(BaseModel):
    name: str
    description: str

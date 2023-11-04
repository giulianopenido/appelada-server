from pydantic import BaseModel


class InputPhoneVerification(BaseModel):
    phone: str

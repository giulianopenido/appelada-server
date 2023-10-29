from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber


class InputPhoneVerification(BaseModel):
    phone: PhoneNumber

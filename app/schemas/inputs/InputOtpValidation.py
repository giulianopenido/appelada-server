from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber


class InputOtpVerification(BaseModel):
    phone: PhoneNumber
    otp: str

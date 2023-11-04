from pydantic import BaseModel


class InputOtpVerification(BaseModel):
    phone: str
    otp: str

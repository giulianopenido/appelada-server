from app.services.AuthService import AuthService
from app.services.OTPService import OTPService

from fastapi import Depends


# Services
def get_auth_service():
    return AuthService(otpService=Depends(get_otp_service))


def get_otp_service():
    return OTPService()

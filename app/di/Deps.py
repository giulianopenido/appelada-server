from app.services.AuthService import AuthService
from app.services.GroupService import GroupService
from app.services.OTPService import OTPService

from fastapi import Depends

from app.services.UserService import UserService


# Services
def get_auth_service():
    return AuthService(otpService=OTPService(), userService= UserService())


def get_otp_service():
    return OTPService()


def get_user_service():
    return UserService()


def get_group_service():
    return GroupService()

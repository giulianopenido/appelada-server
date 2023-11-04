from fastapi import HTTPException

from app.configs.Auth import signJWT
from app.schemas.inputs.InputOtpValidation import InputOtpVerification
from app.schemas.inputs.InputPhoneVerification import InputPhoneVerification
from app.services.OTPService import OTPService
from app.services.UserService import UserService


class AuthService:
    def __init__(self, otpService: OTPService, userService: UserService):
        self.otpService = otpService
        self.userService = userService

    def sendOtpVerification(self, phoneVerification: InputPhoneVerification):
        language = "pt_BR"
        self.otpService.send_otp(language=language, destinationNumber=phoneVerification.phone)

        return

    async def verifyOtp(self, otpValidation: InputOtpVerification):
        success = self.otpService.verify_otp(destinationNumber=otpValidation.phone, otp=otpValidation.otp)
        if not success:
            raise HTTPException(status_code=401, detail="Wrong OTP Code")

        user = await self.userService.findUserByPhoneNumber(phoneNumber=otpValidation.phone)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        accessToken = signJWT(str(user.id))

        return {
            "accessToken": accessToken,
        }

from fastapi import HTTPException

from app.schemas.inputs.InputOtpValidation import InputOtpVerification
from app.schemas.inputs.InputPhoneVerification import InputPhoneVerification


class AuthService:
    def __init__(self, otpService):
        self.otpService = otpService

    def sendOtpVerification(self, phoneVerification: InputPhoneVerification):
        language = "pt_BR"
        self.otpService.send_otp(language=language, destinationNumber=phoneVerification.phone)

        return

    def verifyOtp(self, otpValidation: InputOtpVerification):
        success = self.otpService.verify_otp(destinationNumber=otpValidation.phone, otp=otpValidation.otp)
        if not success:
            raise HTTPException(status_code=401, detail="Wrong OTP Code")

        return

from fastapi import APIRouter, Depends

from app.di import Deps
from app.schemas.inputs.InputOtpValidation import InputOtpVerification
from app.schemas.inputs.InputPhoneVerification import InputPhoneVerification

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/otp")
async def send_otp_verification(phoneVerification: InputPhoneVerification, authService=Depends(Deps.get_auth_service)):
    return authService.sendOtpVerification(phoneVerification=phoneVerification)


@router.post("/otp/verify")
async def verify_otp(otpValidation: InputOtpVerification, authService=Depends(Deps.get_auth_service)):
    return await authService.verifyOtp(otpValidation=otpValidation)



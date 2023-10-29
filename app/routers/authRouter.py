from fastapi import APIRouter, Depends

from app.di import deps
from app.schemas.inputs.InputPhoneVerification import InputPhoneVerification

router = APIRouter(prefix="/auth", tags=["Register"])


@router.post("/otp")
async def send_otp_verification(phoneVerification: InputPhoneVerification, authService=Depends(deps.get_auth_service)):
    return authService.sendOtpVerification(phoneVerification=phoneVerification)


@router.post("/otp/verify")
async def verify_otp(phoneVerification: InputPhoneVerification, authService=Depends(deps.get_auth_service)):
    authService.verifyOtp(phoneVerification=phoneVerification)


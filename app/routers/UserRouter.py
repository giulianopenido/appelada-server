from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.configs.Auth import JWTBearer
from app.di import Deps
from app.models.User import User

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/verify-phone/{phoneNumber}")
async def verify_phone(phoneNumber: str, userService=Depends(Deps.get_user_service)):
    return await userService.verifyPhoneRegistered(phoneNumber=phoneNumber)


@router.post("/register")
async def create_user(user: User, userService=Depends(Deps.get_user_service)) -> User:
    return await userService.createUser(user)


@router.get("/{id}")
async def get_user(id: str, user: Annotated[User, Depends(JWTBearer())], userService=Depends(Deps.get_user_service)):
    if str(user.id) != id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await userService.findUserById(id=id)

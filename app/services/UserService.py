from fastapi import HTTPException

from app.models.User import User


class UserService:
    def __init__(self):
        return

    async def verifyPhoneRegistered(self, phoneNumber):
        user = await self.findUserByPhoneNumber(phoneNumber=phoneNumber)
        return {
            "mustRegister": user is None
        }

    async def createUser(self, user: User) -> User:
        foundUser = await self.findUserByPhoneNumber(user.phone)
        if foundUser is not None:
            raise HTTPException(status_code=400, detail="This phone was already used")

        await user.create()
        return user

    async def findUserByPhoneNumber(self, phoneNumber: str) -> User:
        return await User.find_one(User.phone == phoneNumber)

    async def findUserById(self, id: str) -> User:
        return await User.get(id)

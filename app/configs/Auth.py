from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from app.configs.Environment import get_environment_variables
from app.models.User import User

env = get_environment_variables()


def signJWT(user_id: str) -> str:
    payload = {
        "id": user_id
    }
    return jwt.encode(payload, env.JWT_SECRET)


def decodeJWT(token: str) -> dict:
    try:
        return jwt.decode(token, env.JWT_SECRET)
    except:
        return {}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            payload = decodeJWT(credentials.credentials)
            if not payload:
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")

            return await User.get(payload['id'])

        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")


def get_current_user(req: Request):
    token = req.headers["Authorization"]

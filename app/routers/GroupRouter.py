from fastapi import APIRouter, Depends
from typing import Annotated

from app.configs.Auth import JWTBearer
from app.di import Deps
from app.models.Group import Group
from app.models.User import User, Member
from app.schemas.inputs.InputCreateGroup import InputCreateGroup
from app.schemas.inputs.InputUpdateMemberStatus import InputUpdateMemberStatus

router = APIRouter(prefix="/group", tags=["Group"])


@router.post("")
async def create_group(
    inputGroup: InputCreateGroup,
    loggedUser: Annotated[User, Depends(JWTBearer())],
    groupService=Depends(Deps.get_group_service)
) -> Group:
    return await groupService.createGroup(loggedUser, inputGroup)


@router.put("/{groupId}/member")
async def updateMemberStatus(
    newStats: InputUpdateMemberStatus,
    loggedUser: Annotated[User, Depends(JWTBearer())],
    groupId: str,
    groupService=Depends(Deps.get_group_service)
) -> Member:
    return await groupService.updateMemberStatus(
        newStats=newStats,
        loggedUser=loggedUser,
        groupId=groupId,
    )


@router.put("/{groupId}/join")
async def addUserToGroup(
    loggedUser: Annotated[User, Depends(JWTBearer())],
    groupId: str,
    groupService=Depends(Deps.get_group_service)
) -> Group:
    return await groupService.addUserToGroup(loggedUser, groupId)

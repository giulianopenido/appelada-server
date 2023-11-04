from fastapi import HTTPException

from app.models.Group import Group, Member
from app.models.User import User
from app.schemas.inputs.InputCreateGroup import InputCreateGroup
from app.schemas.inputs.InputUpdateMemberStatus import InputUpdateMemberStatus


class GroupService:

    async def createGroup(self, creator: User, inputGroup: InputCreateGroup) -> Group:
        group = Group(name=inputGroup.name, description=inputGroup.description, creator=creator)
        group.members.append(Member(user=creator))

        await group.create()

        creator.groups.append(str(group.id))
        await creator.save()

        return group

    async def getGroupById(self, groupId: str) -> Group:
        return await Group.get(groupId, fetch_links=True)

    async def updateMemberStatus(
        self,
        newStats: InputUpdateMemberStatus,
        loggedUser: User,
        groupId: str,
        userId: str,
    ) -> Member:
        group = await self.getGroupById(groupId=groupId)
        if group is None:
            raise HTTPException(status_code=404, detail="Group not found")

        if loggedUser.id != group.creator.id:
            raise HTTPException(status_code=401, detail="Only creators can update members status")

        member = list(filter(lambda m: str(m.user.id) == userId, group.members))[0]
        member.speed = newStats.speed
        member.defense = newStats.defense
        member.passing = newStats.passing
        member.shooting = newStats.shooting
        member.stamina = newStats.stamina
        member.dribble = newStats.dribble

        await group.save()

        return member

    async def addUserToGroup(self, loggedUser: User, groupId: str) -> Group:
        group = await self.getGroupById(groupId=groupId)

        if group is None:
            raise HTTPException(status_code=404, detail="Group not found")

        group.members.append(Member(user=loggedUser))
        await group.save()

        loggedUser.groups.append(groupId)
        await loggedUser.save()

        return group

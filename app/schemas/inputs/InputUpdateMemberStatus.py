from typing import Annotated

from pydantic import BaseModel, AfterValidator


def validate_stats_range(stats: int) -> int:
    assert 1 <= stats <= 99, 'stats must be between 1 and 99'

    return stats


class InputUpdateMemberStatus(BaseModel):
    speed: Annotated[int, AfterValidator(validate_stats_range)]
    defense: Annotated[int, AfterValidator(validate_stats_range)]
    passing: Annotated[int, AfterValidator(validate_stats_range)]
    shooting: Annotated[int, AfterValidator(validate_stats_range)]
    stamina: Annotated[int, AfterValidator(validate_stats_range)]
    dribble: Annotated[int, AfterValidator(validate_stats_range)]

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    avatar_url: str
    country_code: str
    default_group: str
    is_active: bool
    is_bot: bool
    is_deleted: bool
    is_online: bool
    is_supporter: bool
    last_visit: Optional[datetime]
    pm_friends_only: bool
    profile_colour: Optional[str]
    id: int
    username: str

# to do
# class UserExtended(BaseModel):
#     cover_url: str

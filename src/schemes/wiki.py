from typing import Optional, List

from pydantic import BaseModel


class Wiki(BaseModel):
    available_locales: List[str]
    layout: str
    locale: str
    markdown: str
    path: str
    subtitle: Optional[str]
    tags: List[str]
    title: str

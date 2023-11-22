from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BeatmapExtended(BaseModel):
    accuracy: float
    ar: float
    beatmapset_id: int
    bpm: Optional[float]
    convert: bool
    count_circles: int
    count_sliders: int
    count_spinners: int
    cs: float
    deleted_at: Optional[datetime]
    drain: float
    hit_length: int
    is_scoreable: bool
    last_updated: datetime
    mode_int: int
    passcount: int
    playcount: int
    ranked: int

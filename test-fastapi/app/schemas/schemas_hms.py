from typing import List, Optional

from pydantic import BaseModel


class HorseBase(BaseModel):
    horse_name: str
    size: int


class CoatBase(BaseModel):
    id: int
    color_name: str
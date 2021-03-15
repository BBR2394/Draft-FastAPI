from pydantic import BaseModel
from typing import Optional, List


class baseDisease(BaseModel):
    name: str
    description: str
    is_vaccine: bool


class disease(baseDisease):
    id: Optional[int]


class typeDisease(BaseModel):
    id: Optional[int]
    type: str
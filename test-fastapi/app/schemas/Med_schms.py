from pydantic import BaseModel
from typing import Optional, List


class med(BaseModel):
    name: Optional[str] = None 
    dose: Optional[int]


class type(BaseModel):
    id: Optional[int]
    type: Optional[str]


class med_plus(med):
    list_type: Optional[List[int]]
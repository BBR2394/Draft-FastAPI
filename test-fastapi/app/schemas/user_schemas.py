from pydantic import BaseModel
from typing import Optional

# c'est ceci le schema
class userBody(BaseModel):
    id: Optional[int]
    # attention met des chaine vide quand rien n'est donné
    email: Optional[str] = None
    last_name: Optional[str]
    first_name: Optional[str]
    username: Optional[str]
    group_name: Optional[str]
    items: Optional[str]
    moreInfo: bool
    nomdugroupe: Optional[str]

class group(BaseModel):
    id: Optional[int]
    type: Optional[str] 

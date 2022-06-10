
from pydantic import BaseModel
#from sqlalchemy.orm import Session

from . import model, schemas

from typing import Optional, List

class Base(BaseModel):
    title: str
    Message: Optional[str] = None
    # is_accepted: Optional[bool] = False

#


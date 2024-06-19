from datetime import datetime
from typing import List, Annotated, Optional
import uuid
from pydantic import BaseModel

class ArticleCreateDTO(BaseModel):
    title: str
    content: str
    temp: str
    
class ArticleUpdateDTO(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    temp: Optional[str] = None
    
class ArticleResponseDTO(BaseModel):
    id: int
    title: str
    content: str
    temp: str
    
    class config:
        orm_mode = True
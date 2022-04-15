from pydantic import BaseModel
from typing import Optional


class Usuarios(BaseModel):
    id : int
    nome : str
    senha : Optional[str]

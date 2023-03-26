from typing import Optional
from pydantic import BaseModel

class AdmissionRequestModel(BaseModel):
    name: str
    last_name: str
    dni: str
    age: int
    magic_affinities_id: int
class UpdateStatusRequestModel(BaseModel):
    comments: str = ''
    status: bool
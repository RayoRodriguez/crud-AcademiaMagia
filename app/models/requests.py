from pydantic import BaseModel, Field, validator


class AdmissionRequestModel(BaseModel):
    name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    dni: str = Field(max_length=10)
    age: int = Field(ge=1, le=99)
    magic_affinities_id: int = Field(ge=1)

    @validator('name', 'last_name')
    def is_alpha(cls, v):
        if not v.isalpha():
            raise ValueError('El nombre y/o apellido contiene caracteres especiales')
        return v

    @validator('dni')
    def is_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('El DNI contiene caracteres especiales')
        return v


class UpdateStatusRequestModel(BaseModel):
    comments: str = ''
    status: bool

from pydantic import BaseModel

class AdmissionRequestModel(BaseModel):
    name: str
    last_name: str
    dni: str
    age: int
    magic_affinities_id: int


class UpdateAdmissionRequestModel(AdmissionRequestModel):
    update_by: str





    #grimoires_id = ForeignKeyField(column_name='grimoires-id', field='id', model=Grimoires, null=True)
    #is_approved = BooleanField(constraints=[SQL("DEFAULT false")])
    #comments = CharField(null=True)

    #updated_by = CharField(null=True)
    #updated_at = DateField(null=True)
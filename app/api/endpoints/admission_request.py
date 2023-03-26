from fastapi import APIRouter
from app.models.requests import AdmissionRequestModel, UpdateAdmissionRequestModel
from app.services.requests_class import AdmissionRequest


router = APIRouter()


#GET
@router.get(path='/')
async def all_applications():
    return ('res')

#POST
@router.post(path='/create')
def create_applications(request: AdmissionRequestModel):
    object_AdmissionRequest = AdmissionRequest(request.name, request.last_name, request.dni, 
                                                  request.age, request.magic_affinities_id)
    return object_AdmissionRequest.create_request()

#PUT
@router.put(path='/update/{id}')
async def update_request(id, request: UpdateAdmissionRequestModel):
    return ('res')

@router.put(path='/approved/{id}')
async def update_request(id):
    return ('res')

#DELETE
@router.delete(path='/delete/{id}')
async def delete_request(id):
    return ('res')
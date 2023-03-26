from fastapi import APIRouter
from app.models.requests import AdmissionRequestModel, UpdateAdmissionRequestModel
from app.services.requests_class import AdmissionRequest


router = APIRouter()


#GET
@router.get(path='/')
async def all_applications():
    object_AdmissionRequest = AdmissionRequest()
    return object_AdmissionRequest.all_requests()

@router.get(path='/dni/{id}')
async def dni_application(id):
    object_AdmissionRequest = AdmissionRequest()
    return object_AdmissionRequest.all_requests(id)

#POST
@router.post(path='/create')
async def create_applications(request: AdmissionRequestModel):
    object_AdmissionRequest = AdmissionRequest(request.name, request.last_name, request.dni, 
                                                  request.age, request.magic_affinities_id, request.comments)
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
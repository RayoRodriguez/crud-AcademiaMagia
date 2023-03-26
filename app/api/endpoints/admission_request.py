from fastapi import APIRouter
from app.models.requests import AdmissionRequestModel, UpdateStatusRequestModel
from app.services.requests_class import AdmissionRequest


router = APIRouter()

#GET
@router.get(path = '/')
async def all_applications():
    object_AdmissionRequest = AdmissionRequest()
    return object_AdmissionRequest.all_requests()

@router.get(path = '/{dni}')
async def dni_application(dni):
    object_AdmissionRequest = AdmissionRequest()
    return object_AdmissionRequest.all_requests(dni)

#POST
@router.post(path = '/create')
async def create_applications(request: AdmissionRequestModel):
    object_AdmissionRequest = AdmissionRequest(request.name, request.last_name, request.dni, 
                                                  request.age, request.magic_affinities_id)
    object_AdmissionRequest.comment = request.comments
    return object_AdmissionRequest.create_request()

#PUT
@router.put(path = '/update/{id}')
async def update_request(id, request: AdmissionRequestModel):
    object_AdmissionRequest = AdmissionRequest(request.name, request.last_name, request.dni, 
                                                  request.age, request.magic_affinities_id)
    return object_AdmissionRequest.update_request(id)

@router.put(path = '/approved/{dni}')
async def update_status(dni, request: UpdateStatusRequestModel):
    object_AdmissionRequest = AdmissionRequest()
    object_AdmissionRequest.comment = request.comments
    return object_AdmissionRequest.update_status(dni, request.status)

#DELETE
@router.delete(path='/delete/{dni}')
async def delete_request(dni):
    object_AdmissionRequest = AdmissionRequest()
    return object_AdmissionRequest.delete_request(dni)
from fastapi import APIRouter

from app.models.requests import AdmissionRequestModel, UpdateStatusRequestModel
from app.services.requests_class import AdmissionRequest

router = APIRouter()


# GET
@router.get(path='/')
async def all_applications():
    object_admission_request = AdmissionRequest()
    return object_admission_request.all_requests()


@router.get(path='/{dni}')
async def dni_application(dni):
    object_admission_request = AdmissionRequest()
    return object_admission_request.all_requests(dni)


# POST
@router.post(path='/create')
async def create_applications(request: AdmissionRequestModel):
    object_admission_request = AdmissionRequest(request.name, request.last_name, request.dni,
                                                request.age, request.magic_affinities_id)
    return object_admission_request.create_request()


# PUT
@router.put(path='/update/{id}')
async def update_request(id, request: AdmissionRequestModel):
    object_admission_request = AdmissionRequest(request.name, request.last_name, request.dni,
                                                request.age, request.magic_affinities_id)
    return object_admission_request.update_request(id)


@router.put(path='/approved/{dni}')
async def update_status(dni, request: UpdateStatusRequestModel):
    object_admission_request = AdmissionRequest()
    object_admission_request.comment = request.comments
    return object_admission_request.update_status(dni, request.status)


# DELETE
@router.delete(path='/delete/{dni}')
async def delete_request(dni):
    object_admission_request = AdmissionRequest()
    return object_admission_request.delete_request(dni)

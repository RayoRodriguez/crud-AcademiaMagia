import uuid
from datetime import date

from fastapi.responses import JSONResponse

from app.models.db import fn, Applications as ApplicationsDB, Grimoires as GrimoireDB


class AdmissionRequest:
    comment = 'Registro Creado'
    updated_by = 'Administrador'

    def __init__(self, name='Default', last_name='Default', dni='Default123',
                 years_old='1', magic_affinities='1'):
        self.__name = name
        self.__last_name = last_name
        self.__dni = dni
        self.__year_old = years_old
        self.__magic_affinities = magic_affinities
        self.__today = date.today()

    def all_requests(self, dni=None):
        res = []
        if dni is None:
            try:
                query = ApplicationsDB.select().dicts()
                for row in query:
                    row['created_at'] = str(row['created_at'])
                    row['updated_at'] = str(row['created_at'])
                    res.append(row)
                return JSONResponse(status_code=200, content=res)
            except Exception as exp:
                return JSONResponse(status_code=404, content={'detail': [{'msg': str(exp)}]})
        else:
            try:
                query = ApplicationsDB.select().where(ApplicationsDB.dni == dni).dicts()
                for row in query:
                    row['created_at'] = str(row['created_at'])
                    row['updated_at'] = str(row['created_at'])
                    res.append(row)
                return JSONResponse(status_code=200, content=res)
            except Exception as exp:
                return JSONResponse(status_code=404, content={'detail': [{'msg': str(exp)}]})

    def create_request(self):
        insert_data = {'id': str(uuid.uuid4()), 'name': self.__name, 'last_name': self.__last_name,
                       'dni': self.__dni, 'years': self.__year_old, 'magic_affinities_id': self.__magic_affinities,
                       'comments': self.comment, 'created_by': self.__name, 'created_at': self.__today,
                       'updated_by': self.__name, 'updated_at': self.__today
                       }
        try:
            ApplicationsDB.insert(insert_data).execute()
            return JSONResponse(status_code=200, content={'detail': [{'msg': 'Solicitud creada con exito'}]})
        except Exception as exp:
            return JSONResponse(status_code=400, content={'detail': [{'msg': str(exp)}]})

    def update_request(self, id):
        self.comment = 'Actualizado'
        update_data = {ApplicationsDB.name: self.__name, ApplicationsDB.last_name: self.__last_name,
                       ApplicationsDB.dni: self.__dni, ApplicationsDB.years: self.__year_old,
                       ApplicationsDB.magic_affinities_id: self.__magic_affinities,
                       ApplicationsDB.comments: self.comment, ApplicationsDB.updated_by: self.updated_by,
                       ApplicationsDB.updated_at: self.__today,
                       }
        try:
            res = ApplicationsDB.update(update_data).where(ApplicationsDB.id == id).execute()
            if res == 0:
                return JSONResponse(status_code=201, content={'detail': [{'msg': 'No se actualizó ningun registro'}]})
            return JSONResponse(status_code=200, content={'detail': [{'msg': 'Se actualizó correctamente'}]})
        except Exception as exep:
            return JSONResponse(status_code=404, content={'detail': [{'msg': str(exep)}]})
        pass

    def update_status(self, dni, status):
        id_grimoire = GrimoireDB.select(GrimoireDB.id).order_by(fn.random()).limit(1)
        update_data = {ApplicationsDB.updated_by: self.updated_by,
                       ApplicationsDB.updated_at: self.__today,
                       ApplicationsDB.is_approved: status,
                       ApplicationsDB.comments: self.comment,
                       ApplicationsDB.grimoires_id: id_grimoire}
        try:
            res = ApplicationsDB.update(update_data).where(
                (ApplicationsDB.dni == dni) & (ApplicationsDB.is_approved is False)).execute()
            if res == 0:
                return JSONResponse(status_code=201, content={'detail': [{'msg': 'No se actualizó ningun registro'}]})
            return JSONResponse(status_code=200, content={'detail': [{'msg': 'Se actualizó correctamente'}]})
        except Exception as exp:
            return JSONResponse(status_code=404, content={'detail': [{'msg': str(exp)}]})

    def delete_request(self, dni):
        try:
            res = ApplicationsDB.delete().where(ApplicationsDB.dni == dni).execute()
            if res == 0:
                return JSONResponse(status_code=201,
                                    content={'detail': [{'msg': 'No se encontro ningun registro con ese DNI'}]})
            return JSONResponse(status_code=200, content={'detail': [{'msg': 'Se eliminó correctamente'}]})
        except Exception as exp:
            return JSONResponse(status_code=404, content={'detail': [{'msg': str(exp)}]})

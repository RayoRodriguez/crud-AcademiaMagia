from app.models.db import database, Applications as ApplicationsDB
from datetime import date
from fastapi.responses import JSONResponse
import uuid


class AdmissionRequest:
    #TODO Ver que el comments no sea requerido
    def __init__ (self, name = 'Default', last_name = 'Default', dni = 'Default123', 
                  years_old = '1', magic_affinities = '1', comments = 'Default' ):
        self.__name = name
        self.__last_name = last_name
        self.__dni = dni
        self.__year_old = years_old
        self.__magic_affinities = magic_affinities
        self.__today = date.today()
        self.__comments = 'Registro Creado' if (comments is None or comments == 'string')  else comments
        
    def all_requests(self, dni = None):
        res = []
        if dni is None:
            try:
                query = ApplicationsDB.select().dicts()
                for row in query:
                    row['created_at'] = str(row['created_at'])
                    row['updated_at'] = str(row['created_at'])
                    res.append(row)
                return JSONResponse(status_code = 200, content = res)
            except Exception as exep:
                return JSONResponse(status_code = 404, content = str(exep))
        else:
            try:
                query = ApplicationsDB.select().where(ApplicationsDB.dni == dni).dicts()
                for row in query:
                    row['created_at'] = str(row['created_at'])
                    row['updated_at'] = str(row['created_at'])
                    res.append(row)
                return JSONResponse(status_code = 200, content = res)
            except Exception as exep:
                return JSONResponse(status_code = 404, content = str(exep))

    def create_request(self):
        data = {'id': str(uuid.uuid4()), 'name' : self.__name, 'last_name' : self.__last_name, 
                'dni' : self.__dni, 'years' : self.__year_old, 'magic_affinities_id' : self.__magic_affinities,
                'comments': self.__comments, 'created_by': self.__name, 'created_at': self.__today, 
                'updated_by': self.__name, 'updated_at': self.__today
                }
        try:
            ApplicationsDB.insert(data).execute()
            return JSONResponse(status_code = 200, content = 'ok')
        except Exception as exep:
            return JSONResponse(status_code = 400, content = str(exep))

    def update_request(self):
        pass

    def update_status(self):
        pass

    def delete_request(self):
        pass


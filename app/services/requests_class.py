from app.models.db import database, Applications
from datetime import date
from fastapi.responses import JSONResponse
import uuid


class AdmissionRequest:
    
    def __init__ (self, name, last_name, dni, years_old, magic_affinities):
        self.__name = name
        self.__last_name = last_name
        self.__dni = dni
        self.__year_old = years_old
        self.__magic_affinities = magic_affinities
        self.__today = date.today()

    def create_request(self):
        data = {'id' : str(uuid.uuid4()), 'name' : self.__name, 'last_name' : self.__last_name, 
                'dni' : self.__dni, 'years' : self.__year_old, 'magic_affinities_id' : self.__magic_affinities,
                'comments': 'Registro Creado', 'created_by': self.__name, 'created_at': self.__today, 
                'updated_by': self.__name, 'updated_at': self.__today
                }
        try:
            Applications.insert(data).execute()
            return JSONResponse(status_code = 200 ,content = 'ok')
        except Exception as e:
            return JSONResponse(status_code = 400 ,content = e)

    def update_request(self):
        pass

    def update_status(self):
        pass

    def get_requests(self):
        pass

    def delete_request(self):
        pass


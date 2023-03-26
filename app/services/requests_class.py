from app.models.db import database, fn, Applications as ApplicationsDB, Grimoires as GrimoiresDB
from datetime import date
from fastapi.responses import JSONResponse
import uuid


class AdmissionRequest:

    comment = 'Registro Creado'

    def __init__ (self, name = 'Default', last_name = 'Default', dni = 'Default123', 
                  years_old = '1', magic_affinities = '1' ):
        self.__name = name
        self.__last_name = last_name
        self.__dni = dni
        self.__year_old = years_old
        self.__magic_affinities = magic_affinities
        self.__today = date.today()
        #self.comments = 'Registro Creado' if (comment is None or comment == 'string')  else comment
        
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
                'comments': self.comment, 'created_by': self.__name, 'created_at': self.__today, 
                'updated_by': self.__name, 'updated_at': self.__today
                }
        try:
            ApplicationsDB.insert(data).execute()
            return JSONResponse(status_code = 200, content = 'ok')
        except Exception as exep:
            return JSONResponse(status_code = 400, content = str(exep))

    def update_request(self, updated_by):
        pass

    def update_status(self, dni, updated_by, status):
        id_grimoire = GrimoiresDB.select(GrimoiresDB.id).order_by(fn.random()).limit(1)
        updateData = {ApplicationsDB.updated_by: updated_by,
                      ApplicationsDB.updated_at: self.__today,
                      ApplicationsDB.is_approved: status,
                      ApplicationsDB.comments: self.comment,
                      ApplicationsDB.grimoires_id: id_grimoire}
        try:
            res = ApplicationsDB.update(updateData).where((ApplicationsDB.dni == dni) & (ApplicationsDB.is_approved == False)).execute()
            if res == 0:
                return JSONResponse(status_code = 201, content = "No se actualizó ningun registro")
            return JSONResponse(status_code = 200, content = "Se actualizó correctamente")
        except Exception as exep:
            return JSONResponse(status_code = 404, content = str(exep))

    def delete_request(self, dni):
        try:
            res = ApplicationsDB.delete().where(ApplicationsDB.dni == dni).execute()
            if res == 0:
                return JSONResponse(status_code = 201, content = "No se encontro ningun registro con ese DNI")
            return JSONResponse(status_code = 200, content = "Se eliminó correctamente")
        except Exception as exep:
            return JSONResponse(status_code = 404, content = str(exep))
        pass


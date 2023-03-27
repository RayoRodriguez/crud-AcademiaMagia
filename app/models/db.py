import json

from peewee import *

ENVIROMENT = 'DEFAULT'

with open('app/config.json', 'r') as file:
    config = json.load(file)
    print(config)

database = PostgresqlDatabase(
    config[ENVIROMENT]['DB_NAME'],
    user=config[ENVIROMENT]['DB_USER'],
    password=config[ENVIROMENT]['DB_PASSWORD'],
    host=config[ENVIROMENT]['DB_HOST'],
    port=config[ENVIROMENT]['DB_PORT'],
    autorollback=True)


class BaseModel(Model):
    class Meta:
        database = database


class Grimoires(BaseModel):
    grimoire_name = CharField()
    front_name = CharField()

    class Meta:
        table_name = 'grimoires'
        schema = 'magic_academy'


class MagicAffinities(BaseModel):
    name = CharField()

    class Meta:
        table_name = 'magic_affinities'
        schema = 'magic_academy'


class Applications(BaseModel):
    id = CharField(primary_key=True)
    name = CharField()
    last_name = CharField()
    dni = CharField(column_name='DNI')
    years = IntegerField()
    magic_affinities_id = ForeignKeyField(column_name='magic_affinities-id', field='id', model=MagicAffinities)
    grimoires_id = ForeignKeyField(column_name='grimoires-id', field='id', model=Grimoires, null=True)
    is_approved = BooleanField(constraints=[SQL("DEFAULT false")])
    comments = CharField(null=True)
    created_by = CharField(null=True)
    created_at = DateField(null=True)
    updated_by = CharField(null=True)
    updated_at = DateField(null=True)

    class Meta:
        table_name = 'applications'
        indexes = (
            (('id', 'name', 'last_name'), True),
        )
        schema = 'magic_academy'

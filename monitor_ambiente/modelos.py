import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class ReglasAmbiente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    medicion = db.Column(db.String(50))
    periodo = db.Column(db.String(50))
    nivel_estandar = db.Column(db.String(50))
    nivel_bajo = db.Column(db.String(50))
    nivel_alto = db.Column(db.String(50))
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento = db.Column(db.String(50))

class ReglasAmbienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ReglasAmbiente

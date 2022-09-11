import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class ReglasServicosSalud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    servicio = db.Column(db.String(50))
    temporizador = db.Column(db.String(50))
    nivel_estandar = db.Column(db.String(50))
    nivel_bajo = db.Column(db.String(50))
    nivel_alto = db.Column(db.String(50))
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class ReglasServicosSaludSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ReglasServicosSalud

import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class ReglasAperturas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    objeto_apertura = db.Column(db.String(50))
    temporizador = db.Column(db.String(50))
    hora_apertura = db.Column(db.String(50))
    hora_cierre = db.Column(db.String(50))
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class ReglasAperturasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ReglasAperturas

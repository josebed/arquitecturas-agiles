import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class ReglasAperturas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(30))
    usuario = db.Column(db.String(50))
    objeto = db.Column(db.String(50))
    monitor = db.Column(db.String(50))
    cerrada = db.Column(db.String(50))
    abierta = db.Column(db.String(50))
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class ReglasAperturasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ReglasAperturas

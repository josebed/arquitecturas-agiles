import datetime

import pytz
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()
class HearbeatTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(50))
    fecha_creacion = db.Column(db.DateTime)

class HearbeatSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HearbeatTable

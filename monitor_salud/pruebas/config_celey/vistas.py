from flask import request
from flask_restful import Resource
from modelos import db, HearbeatTable
import datetime
import pytz
class OrderListResource(Resource):
    def post(self):
        nuevo_usuario = HearbeatTable(
            mensaje=request.json["mensaje"],
            fecha_creacion=datetime.datetime.now(tz=pytz.timezone('America/Bogota'))
        )

        db.session.add(nuevo_usuario)
        db.session.commit()




class VistaRoot(Resource):
    def get(self):
        a = HearbeatTable.query.order_by(HearbeatTable.fecha_creacion.desc()).first().mensaje
        return {"MicroService": a}
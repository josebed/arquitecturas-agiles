from base64 import encode
import code
from datetime import datetime
import sqlite3

from core.add_hash import generate_hash
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from modelos import db, ReglasServicosSalud, ReglasServicosSaludSchema
import logging

FORMAT = '%(asctime)s ~ %(levelname)s ~ %(message)s'
logging.basicConfig(filename='monitoring_health_all_events.log', filemode="w", format=FORMAT)

class AgregarRegla(Resource):

    @jwt_required()
    def get(self, id_regla):
        return [ReglasServicosSaludSchema.dump(ap) for ap in
                db.session.query().with_entities().filter(ReglasServicosSalud.id == id_regla).all()]
    
    @jwt_required()
    def post(self,id_usuario):

            db_connection = sqlite3.connect("../usuarios/usuarios.db")
            cur = db_connection.cursor()
            cur.execute('SELECT codigo_seguridad from usuario where id ={}'.format(id_usuario))
            usuario = cur.fetchone()
            if not usuario:
                return {"code": 404, "message": "Not found"}
            db_connection.close()
            codigo_seguridad = usuario[0]  

            hash_enviado= request.json["hash"]
            request_regla = request.json
            request_regla.pop("hash")
            codigo_hash = generate_hash(request_regla, codigo_seguridad)
            
            if (hash_enviado != codigo_hash):
                log_data = {"clientip": "127.0.0.1", "id_usuario":id_usuario}
                logging.error("Data alterada", extra=log_data)
                return {"code": 2010, "message": "Acción no realizada"}
            nuevo_regla = ReglasServicosSalud(
                id_usuario=id_usuario,
                servicio=request.json["servicio"],
                temporizador=request.json["temporizador"],
                nivel_estandar=request.json["nivel_estandar"],
                nivel_bajo=request.json["nivel_bajo"],
                nivel_alto=request.json["nivel_alto"],
                fecha_creacion= datetime.now(),
            )
            db.session.add(nuevo_regla)
            db.session.commit()

            return {"mensaje": "Regla creada exitosamente", "id": nuevo_regla.id}

    @jwt_required()
    def put(self, id_regla):

        codigo_seguridad = '123456'
        hash_enviado= request.json["hash"]
        request_regla = request.json
        request_regla.pop("hash")
        codigo_hash = generate_hash(request_regla, codigo_seguridad)

        if (hash_enviado != codigo_hash):
            print("Data alterada")
            return {"code": 2010, "message": "Acción no realizada"}

        nuevo_regla = ReglasServicosSalud.query.get_or_404(id_regla)
        nuevo_regla.temporizador = request.json.get("temporizador", nuevo_regla.temporizador)
        nuevo_regla.nivel_estandar = request.json.get("nivel_estandar", nuevo_regla.nivel_estandar)
        nuevo_regla.nivel_bajo = request.json.get("nivel_bajo", nuevo_regla.nivel_bajo)
        nuevo_regla.nivel_alto = request.json.get("nivel_alto", nuevo_regla.nivel_alto)
        db.session.commit()
        return ReglasServicosSaludSchema.dump(nuevo_regla)

class VistaRoot(Resource):
    def get(self):
        return {"MicroService": "Monitor Salud v1"}
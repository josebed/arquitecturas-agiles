
import sqlite3

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from modelos import db, ReglasAmbiente, ReglasAmbienteSchema
from monitor_ambiente import logger
from core.hash import generate_hash


class AgregarRegla(Resource):
    
    @jwt_required
    def get(self, id_regla):
        return [ReglasAmbiente.dump(ap) for ap in
                db.session.query().with_entities().filter(ReglasAmbienteSchema.id == id_regla).all()]
    
    @jwt_required
    def post(self, id_usuario):

            db_connection = sqlite3.connect("../usuarios/usuarios.db")
            cur = db_connection.cursor()
            cur.execute('SELECT codigo_seguridad from usuario where id ={}'.format(id_usuario))
            usuario = cur.fetchone()
            if usuarion is None:
                return {'code':404, "message": "not found"}
            db_connection.close()

            codigo_seguridad = usuario[0]
            hash_enviado = request.json['hash']
            request_regla = request.json.pop('hash')
            codigo_hash = generate_hash(request_regla, codigo_seguridad)

            if hash_enviado != codigo_hash:
                log_data = {'clientip': '127.0.0.1', 'id_usuario': id_usuario}
                logger.error("Data alterada", extra=log_data)
                return {"code": 2010, "message": "Accion no realizada"}

            try:
                nuevo_regla = ReglasAmbiente(
                    usuario=request.json["usuario"],
                    medicion=request.json["medicion"],
                    periodo=request.json["periodo"],
                    nivel_estandar=request.json["nivel_estandar"],
                    nivel_bajo=request.json["nivel_bajo"],
                    nivel_alto=request.json["nivel_alto"]
                )
                db.session.add(nuevo_regla)
                db.session.commit()

                return {"mensaje": "Regla creada exitosamente", "id": nuevo_regla.id}
            except Exception as e:
                logger.error(f'This is an ERROR message {e}')
                return {"mensaje": f"falta {e}"}
    
    @jwt_required
    def put(self, id_regla):

        codigo_seguridad = "123456"
        hash_enviado = request.json['hash']
        request_regla = request.json.pop('hash')
        codigo_hash = generate_hash(request_regla, codigo_seguridad)

        if (hash_enviado != codigo_hash):
            print("Data alterada")
            return {'code': 2010, "message": "Acción no realizada"}

        nuevo_regla = ReglasAmbiente.query.get_or_404(id_regla)
        nuevo_regla.periodo = request.json.get("periodo", nuevo_regla.periodo)
        nuevo_regla.nivel_estandar = request.json.get("nivel_estandar", nuevo_regla.nivel_estandar)
        nuevo_regla.nivel_bajo = request.json.get("nivel_bajo", nuevo_regla.nivel_bajo)
        nuevo_regla.nivel_alto = request.json.get("nivel_alto", nuevo_regla.nivel_alto)

        db.session.commit()
        return ReglasAmbienteSchema.dump(nuevo_regla)

    def delete(self):
        pass

class VistaRoot(Resource):
    def get(self):
        return {"MicroService": "Monitor Ambiente v1"}

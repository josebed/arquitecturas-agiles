import code
from core.add_hash import generate_hash
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from modelos import db, ReglasAperturas, ReglasAperturasSchema
import logging

FORMAT = '%(asctime)s; %(clientip)s; usuario=%(id_usuario)s; %(message)s'
logging.basicConfig(filename='security_monitor_aperturas.log', format=FORMAT, filemode="w")
logging.getLogger('root').setLevel(logging.ERROR)
logging.getLogger('werkzeug').setLevel(logging.ERROR)


class AgregarRegla(Resource):

    def get(self, id_regla):
        return [ReglasAperturasSchema.dump(ap) for ap in
                db.session.query().with_entities().filter(ReglasAperturas.id == id_regla).all()]
    
    #@jwt_required()
    def post(self,id_usuario):

            codigo_seguridad = '123456'
            hash_enviado= request.json["hash"]
            request_regla = request.json
            request_regla.pop("hash")
            codigo_hash = generate_hash(request_regla, codigo_seguridad)
            
            if (hash_enviado != codigo_hash):
                log_data = {"clientip": "127.0.0.1", "id_usuario":id_usuario}
                logging.error("Data alterada", extra=log_data)
                return {"code": 2010, "message": "Acción no realizada"}
            nuevo_regla = ReglasAperturas(
                id_usuario=id_usuario,
                objeto_apertura=request.json["objeto_apertura"],
                temporizador=request.json["temporizador"],
                hora_apertura=request.json["hora_apertura"],
                hora_cierre=request.json["hora_cierre"],
            )
            db.session.add(nuevo_regla)
            db.session.commit()

            return {"mensaje": "Regla creada exitosamente", "id": nuevo_regla.id}

    #@jwt_required()
    def put(self, id_regla):

        codigo_seguridad = '123456'
        hash_enviado= request.json["hash"]
        request_regla = request.json
        request_regla.pop("hash")
        codigo_hash = generate_hash(request_regla, codigo_seguridad)

        if (hash_enviado != codigo_hash):
            print("Data alterada")
            return {"code": 2010, "message": "Acción no realizada"}

        nuevo_regla = ReglasAperturas.query.get_or_404(id_regla)
        nuevo_regla.temporizador = request.json.get("temporizador", nuevo_regla.temporizador)
        nuevo_regla.hora_apertura = request.json.get("hora_apertura", nuevo_regla.hora_apertura)
        nuevo_regla.hora_cierre = request.json.get("hora_cierre", nuevo_regla.hora_cierre)
        db.session.commit()
        return ReglasAperturasSchema.dump(nuevo_regla)

class VistaRoot(Resource):
    def get(self):
        return {"MicroService": "Monitor Aperturas v1"}

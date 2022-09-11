from flask import request
from flask_restful import Resource
from modelos import db, ReglasAperturas, ReglasAperturasSchema
# from monitor_aperturas import logger

class AgregarRegla(Resource):

    def get(self, id_regla):
        return [ReglasAperturasSchema.dump(ap) for ap in
                db.session.query().with_entities().filter(ReglasAperturas.id == id_regla).all()]

    def post(self):

            nuevo_regla = ReglasAperturas(
                usuario=request.json["usuario"],
                objeto_apertura=request.json["objeto_apertura"],
                temporizador=request.json["temporizador"],
                hora_apertura=request.json["hora_apertura"],
                hora_cierre=request.json["hora_cierre"],
            )
            db.session.add(nuevo_regla)
            db.session.commit()

            return {"mensaje": "Regla creada exitosamente", "id": nuevo_regla.id}


    def put(self, id_regla):
        nuevo_regla = ReglasAperturas.query.get_or_404(id_regla)
        nuevo_regla.temporizador = request.json.get("temporizador", nuevo_regla.temporizador)
        nuevo_regla.hora_apertura = request.json.get("hora_apertura", nuevo_regla.hora_apertura)
        nuevo_regla.hora_cierre = request.json.get("hora_cierre", nuevo_regla.hora_cierre)
        db.session.commit()
        return ReglasAperturasSchema.dump(nuevo_regla)

class VistaRoot(Resource):
    def get(self):
        return {"MicroService": "Monitor Aperturas v1"}

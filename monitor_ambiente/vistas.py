import logging

from flask import request
from flask_restful import Resource
from modelos import db, ReglasAmbiente, ReglasAmbienteSchema
from monitor_ambiente import logger


class AgregarRegla(Resource):

    def get(self, id_regla):
        return [ReglasAmbiente.dump(ap) for ap in
                db.session.query().with_entities().filter(ReglasAmbienteSchema.id == id_regla).all()]

    def post(self):
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

    def put(self, id_regla):
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

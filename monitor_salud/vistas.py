from flask import request
from flask_restful import Resource
from modelos import db, ReglasServicosSalud, ReglasServicosSaludSchema
from monitor_salud import logger
class AgregarRegla(Resource):

    def get(self, id_regla):
        return [ReglasServicosSalud.dump(ap) for ap in
                db.session.query().with_entities().filter(ReglasServicosSalud.id == id_regla).all()]

    def post(self):
            try:
                nuevo_regla = ReglasServicosSalud(
                    usuario=request.json["usuario"],
                    servicio=request.json["servicio"],
                    temporizador=request.json["temporizador"],
                    nivel_estandar=request.json["nivel_estandar"],
                    nivel_bajo=request.json["nivel_bajo"],
                    nivel_alto=request.json["nivel_alto"],
                )
                db.session.add(nuevo_regla)
                db.session.commit()

                return {"mensaje": "Regla creada exitosamente", "id": nuevo_regla.id}
            except Exception as e:
                logger.error(f'This is an ERROR message {e}')
                return {"mensaje": f"falta {e}"}

    def put(self, id_regla):
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

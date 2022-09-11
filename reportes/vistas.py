from flask import request
from flask_restful import Resource
from modelos import db, ReglasAperturas, ReglasAperturasSchema

class AgregarRegla(Resource):

    def post(self):
            try:
                nuevo_regla = ReglasAperturas(
                    tipo='apertura',
                    usuario=request.json["usuario"],
                    objeto=request.json["objeto"],
                    monitor=request.json["monitor"],
                    cerrada=request.json["cerrada"],
                    abierta=request.json["abierta"],
                )
                db.session.add(nuevo_regla)
                db.session.commit()

                return {"mensaje": "Regla creada exitosamente", "id": nuevo_regla.id}
            except Exception as e:
                print(e)
                return {"mensaje": f"falta {e}"}

    def put(self, id_regla):
        nuevo_regla = ReglasAperturas.query.get_or_404(id_regla)
        nuevo_regla.cerrada = request.json.get("cerrada", nuevo_regla.cerrada)
        nuevo_regla.abierta = request.json.get("abierta", nuevo_regla.abierta)
        db.session.commit()
        return ReglasAperturasSchema.dump(nuevo_regla)

class VistaRoot(Resource):
    def get(self):
        return {"MicroService": "E-PORRA is Ready v1"}

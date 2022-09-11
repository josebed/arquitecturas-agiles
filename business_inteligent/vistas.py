from flask import request
from flask_restful import Resource
# from modelos import db, ReglasAperturas, ReglasAperturasSchema

class AgregarRegla(Resource):


    def post(self):
        pass

    def put(self, id_regla):
        pass

class VistaRoot(Resource):
    def get(self):
        return {"MicroService": "Business Analitics v1"}

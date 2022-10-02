from flask import request
from flask_restful import Resource
# from modelos import db, ReglasAperturas, ReglasAperturasSchema
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
class AgregarRegla(Resource):


    def post(self):
        pass

    def put(self, id_regla):
        pass

class VistaRoot(Resource):
    @jwt_required()
    def get(self):
        return {"MicroService": "Business Analitics v1"}

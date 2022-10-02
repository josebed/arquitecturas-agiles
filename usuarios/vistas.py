import random
from flask import request
from flask_restful import Resource
from modelos import db,Usuario
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token

class VistaLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
        usuario.codigo_seguridad = str(random.randrange(100000, 900000))
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"mensaje": "Inicio de sesión exitoso",
                    "token": token_de_acceso,
                    "usuario_id": usuario.id,
                    "codigo_seguridad": usuario.codigo_seguridad
                    }



class VistaRoot(Resource):
    def get(self):
        return {"MicroService": "Business Analitics v1"}

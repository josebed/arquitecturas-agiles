import random
from flask import request
from flask_restful import Resource
from modelos import db,Usuario
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
import logging

class VistaLogIn(Resource):

    def post(self):
        logger = logging.getLogger('Login accesos')
        logger.setLevel(logging.ERROR)
        handler = logging.FileHandler('log_login_app.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == request.json["contrasena"]).first()
        if usuario is None:
            usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"]).first()
            if usuario is None:
                logger.error(f'Intento fallido de loging usuario incorrecta')
                return "El usuario no existe", 404
            usuario.erro_login = usuario.erro_login + 1
            db.session.commit()
            logger.error(f'Intento fallido de loging contrasena incorrecta')
            return "El contrasena no existe", 404
        else:

            usuario.codigo_seguridad = str(random.randrange(100000, 900000))
            db.session.commit()
            token_de_acceso = create_access_token(identity=usuario.id)
            logger.error(f'Login exitoso')
            return {"mensaje": "Inicio de sesión exitoso",
                    "token": token_de_acceso,
                    "usuario_id": usuario.id,
                    "codigo_seguridad": usuario.codigo_seguridad
                    }



class VistaRoot(Resource):
    def get(self):
        return {"MicroService": "Business Analitics v1"}

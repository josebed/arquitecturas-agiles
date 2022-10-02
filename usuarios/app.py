from flask import Flask, request, jsonify
from modelos import db
from flask_restful import Api
from vistas import VistaLogIn, VistaRoot
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
api = Api(app)

api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaRoot, '/')

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5080)
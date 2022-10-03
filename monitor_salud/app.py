from flask import Flask
from modelos import db
from flask_restful import Api
from vistas import AgregarRegla, VistaRoot
from trace import Trace
from vistas import AgregarRegla, VistaRoot
from flask_jwt_extended import JWTManager
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitor_salud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'key-secret'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
api = Api(app)

api.add_resource(AgregarRegla, '/monitor_salud/<int:id_usuario>/reglas')
api.add_resource(VistaRoot, '/')

jwt = JWTManager(app)

if __name__ == '__main__':
    logging.basicConfig(filename='log_monitor_salud.log')
    logging.getLogger().setLevel(logging.ERROR)
    app.run(debug=False, host='0.0.0.0', port=5003)
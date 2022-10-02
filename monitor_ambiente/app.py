from flask import Flask, request, jsonify
from modelos import db
from flask_restful import Api
from vistas import AgregarRegla, VistaRoot
import time
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitor_ambiente.db'
app.config['JWT_SECRET_KEY'] = "clave_secreta"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
api = Api(app)

api.add_resource(AgregarRegla, '/monitor_ambiente/reglas')
api.add_resource(VistaRoot, '/')

if __name__ == '__main__':
    logging.basicConfig(filename="log_motitor_ambiente.log")
    app.run(debug=True, host='0.0.0.0', port=5010)
from trace import Trace
from flask import Flask, request, jsonify
from sqlalchemy import false
from modelos import db
from flask_restful import Api
from vistas import AgregarRegla, VistaRoot
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitor_aperturas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
api = Api(app)

api.add_resource(AgregarRegla, '/monitor_aperturas/<int:id_usuario>/reglas')
api.add_resource(VistaRoot, '/')

if __name__ == '__main__':
    logging.basicConfig(filename='log_monitor_aperturas.log')
    logging.getLogger().setLevel(logging.ERROR)
    app.run(debug=False, host='0.0.0.0', port=5002)
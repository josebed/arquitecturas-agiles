from flask import Flask, request, jsonify
from modelos import db
from flask_restful import Api
from vistas import OrderListResource, VistaRoot
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hearbeat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
api = Api(app)



api.add_resource(OrderListResource, '/hearbeat')
api.add_resource(VistaRoot, '/')

if __name__ == '__main__':

    # logging.basicConfig(filename='config_celey/example.log', encoding='utf-8', level=logging.ERROR)
    # logging.error('Errores de servicio')
    app.run(debug=True, host='0.0.0.0', port=5020)
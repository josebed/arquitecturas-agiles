from flask import Flask, request, jsonify
from flask_restful import Resource
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import logging
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heartbeat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()
api = Api(app)

class Hearbeat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(50), unique=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class OrderListResource(Resource):
    def post(self):
        nuevo_usuario = Hearbeat(
            mensaje=request.json["mensaje"],
        )
        db.session.add(nuevo_usuario)
        db.session.commit()


api.add_resource(OrderListResource, '/hearbeat')


if __name__ == '__main__':

    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.ERROR)
    logging.error('Errores de servicio')
    app.run(debug=True, host='0.0.0.0', port=5002)
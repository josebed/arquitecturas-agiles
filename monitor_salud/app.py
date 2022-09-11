from flask import Flask, request, jsonify
from modelos import db
from flask_restful import Api
from vistas import AgregarRegla, VistaRoot

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitor_aperturas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
api = Api(app)

api.add_resource(AgregarRegla, '/monitor_salud/reglas')
api.add_resource(VistaRoot, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
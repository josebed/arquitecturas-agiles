from flask import Flask
from flask_restful import Api
from vistas import ConsultarReglaApertura
app = Flask(__name__)
app_context = app.app_context()
app_context.push()
api = Api(app)
api.add_resource(ConsultarReglaApertura, '/monitor_aperturas/reglas/<id_regla>')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5004)
from flask_restful import Resource
import sqlite3


class ConsultarReglaApertura(Resource):

    def get(self, id_regla):
        db_connection = sqlite3.connect("../monitor_aperturas/monitor_aperturas.db")
        cur = db_connection.cursor()
        cur.execute('SELECT * from reglas_aperturas where id ={}'.format(id_regla))
        regla = cur.fetchone()
        if not regla:
            return {"code": 404, "message": "Not found"}
        db_connection.close()
        return {"id": regla[0], "usuario": regla[1], "objeto_apertura": regla[2], "temporizador": regla[3],
                "hora_apertura": regla[4], "hora_cierre": regla[5], "fecha_creacion": regla[6]}
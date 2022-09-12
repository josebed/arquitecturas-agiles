
import requests
import time
from faker import Faker
from faker.generator import random
import random
from datetime import datetime, timedelta

class TestApuesta():

    def setUp(self):
        self.data_factory = Faker()
        return  {
            "usuario": self.data_factory.name(),
            "objeto_apertura": self.data_factory.word(),
            "temporizador": str(self.data_factory.random_int(100, 200)),
            "hora_apertura":  str(self.data_factory.random_int(100, 200)),
            "hora_cierre": str(self.data_factory.random_int(100, 200))}

def consulta_calculadora(url, pyload, metodo):

    # for position in range(len(request_calculator)):

    url = url

    payload = pyload

    response = requests.request(metodo, url=url, json=payload)
    if response.status_code == 200:
        tiempo_respuesta = response.elapsed.total_seconds()
        codigo_erro = 200
        id_re=response.json()['id']
        reporte = requests.request("GET", url=f'http://localhost:5004/monitor_aperturas/reglas/{id_re}')
        if reporte.status_code == 200:
            reporte_status = reporte.status_code
        else:
            reporte_status = reporte.status_code
    else:
        codigo_erro = response.status_code
        tiempo_respuesta = response.elapsed.total_seconds()
        reporte_status = -1

    return tiempo_respuesta, codigo_erro, str(datetime.now()), reporte_status

if __name__ == "__main__":
    tiempo_respuesta__ = []
    codigo_erro__ = []
    tiempo_reporte = []
    tiempo_general = []
    for i in range(100):
        if random.randrange(0, 100) > 75:
            url="http://localhost:5002/monitor_aperturas/reglas"
            pyload=TestApuesta().setUp()
            metodo="POST"
            tiempo_respuesta, codigo_erro, tiempo, reporte_status = consulta_calculadora(url, pyload, metodo)
            tiempo_respuesta__.append(tiempo_respuesta)
            codigo_erro__.append(codigo_erro)
            tiempo_reporte.append(reporte_status)
            tiempo_general.append(tiempo)
        elif 75 > random.randrange(0, 100) > 55:
            url = f"http://localhost:5002/monitor_aperturas/reglas{Faker().word()}"
            pyload = TestApuesta().setUp()
            metodo = "POST"
            tiempo_respuesta, codigo_erro, tiempo, reporte_status = consulta_calculadora(url, pyload, metodo)
            tiempo_respuesta__.append(tiempo_respuesta)
            codigo_erro__.append(codigo_erro)
            tiempo_reporte.append(reporte_status)
            tiempo_general.append(tiempo)
        elif 55 > random.randrange(0, 100) > 35:
            url = "http://localhost:5002/monitor_aperturas/reglas"
            pyload = TestApuesta().setUp()
            metodo = ["POST","GET","PUT","DELET"][random.randrange(0, 3)]
            tiempo_respuesta, codigo_erro, tiempo, reporte_status = consulta_calculadora(url, pyload, metodo)
            tiempo_respuesta__.append(tiempo_respuesta)
            codigo_erro__.append(codigo_erro)
            tiempo_reporte.append(reporte_status)
            tiempo_general.append(tiempo)
        elif random.randrange(0, 100) < 35:
            url = "http://localhost:5002/monitor_aperturas/reglas"
            pyload = TestApuesta().setUp()
            llave= ["usuario", "objeto_apertura",  "temporizador", "hora_apertura", "hora_cierre"][random.randrange(0, 4)]
            pyload.pop(llave, None)
            metodo = "POST"
            tiempo_respuesta, codigo_erro, tiempo, reporte_status = consulta_calculadora(url, pyload, metodo)
            tiempo_respuesta__.append(tiempo_respuesta)
            codigo_erro__.append(codigo_erro)
            tiempo_reporte.append(reporte_status)
            tiempo_general.append(tiempo)


    print( tiempo_respuesta__ ,
    codigo_erro__,
    tiempo_reporte,
    tiempo_general)






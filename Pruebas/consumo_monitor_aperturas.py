
import requests

from faker import Faker
from faker.generator import random
import random


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
    else:
        codigo_erro = response.status_code
        tiempo_respuesta = response.elapsed.total_seconds()

    return tiempo_respuesta, codigo_erro

if __name__ == "__main__":
    tiempo_respuesta__ = []
    codigo_erro__ = []
    for i in range(100):
        if random.randrange(0, 100) > 75:
            url="http://localhost:5002/monitor_aperturas/reglas"
            pyload=TestApuesta().setUp()
            metodo="POST"
            tiempo_respuesta, codigo_erro= consulta_calculadora(url, pyload, metodo)
            tiempo_respuesta__.append(tiempo_respuesta)
            codigo_erro__.append(codigo_erro)
        elif 75 > random.randrange(0, 100) > 55:
            url = f"http://localhost:5002/monitor_aperturas/reglas{Faker().word()}"
            pyload = TestApuesta().setUp()
            metodo = "POST"
            tiempo_respuesta, codigo_erro = consulta_calculadora(url, pyload, metodo)
            tiempo_respuesta__.append(tiempo_respuesta)
            codigo_erro__.append(codigo_erro)
        elif 55 > random.randrange(0, 100) > 35:
            url = "http://localhost:5002/monitor_aperturas/reglas"
            pyload = TestApuesta().setUp()
            metodo = ["POST","GET","PUT","DELET"][random.randrange(0, 3)]
            tiempo_respuesta, codigo_erro = consulta_calculadora(url, pyload, metodo)
            tiempo_respuesta__.append(tiempo_respuesta)
            codigo_erro__.append(codigo_erro)
        elif random.randrange(0, 100) < 35:
            url = "http://localhost:5002/monitor_aperturas/reglas"
            pyload = TestApuesta().setUp()
            llave= ["usuario", "objeto_apertura",  "temporizador", "hora_apertura", "hora_cierre"][random.randrange(0, 4)]
            pyload.pop(llave, None)
            metodo = "POST"
            tiempo_respuesta, codigo_erro = consulta_calculadora(url, pyload, metodo)
            tiempo_respuesta__.append(tiempo_respuesta)
            codigo_erro__.append(codigo_erro)

    print(tiempo_respuesta__, codigo_erro__)






from faker import Faker
import faker
import requests

from faker.generator import random
import random
from datetime import datetime

from typing import Dict, Any
import hashlib
import json
import logging


FORMAT = '%(asctime)s, usuario=%(id_usuario)s, %(message)s'
logging.basicConfig(filename='pruebas_monitor_aperturas.log', format=FORMAT, filemode="w")
logging.getLogger('root').setLevel(logging.ERROR)
logging.getLogger('werkzeug').setLevel(logging.ERROR)

def generate_hash(req_json: Dict[str, Any], codigo_seguridad):
    codigo_hash = hashlib.md5()
    json_ecoded= json.dumps(req_json, sort_keys=True).encode()
    codigo_seguridad_encoded = codigo_seguridad.encode()
    codigo_hash.update(json_ecoded)
    codigo_hash.update(codigo_seguridad_encoded)
    return codigo_hash.hexdigest()

class TestAperturas():

    def setUp(self):
        self.data_factory = Faker()
        return  {
            "usuario": self.data_factory.name(),
            "objeto_apertura": self.data_factory.word(),
            "temporizador": str(self.data_factory.random_int(100, 200)),
            "hora_apertura":  str(self.data_factory.random_int(100, 200)),
            "hora_cierre": str(self.data_factory.random_int(100, 200))}

if __name__ == "__main__":
    
    id_usuario = 1
    codigo_seguridad = '123456'
    usuario_token = "asdfghjklqwertyuiopzxcvbnm"
    data_factory = Faker()
    url="http://localhost:5002/monitor_aperturas/{}/reglas".format(id_usuario)

    for i in range(100):

        payload=TestAperturas().setUp()
        request_hash = generate_hash(payload, codigo_seguridad)
        payload["hash"] = request_hash
        caso_aleatorio = random.randrange(0, 100)
        if caso_aleatorio > 66:            
            response = requests.request("POST", url=url, json=payload)
            
        elif caso_aleatorio > 33:
           payload["objeto_apertura"] = data_factory.word()
           response = requests.request("POST", url=url, json=payload)
           if(response.status_code == 200):
                log_data = {"id_usuario":id_usuario}
                logging.error("Se introdujo tampering", extra=log_data)

        else:
            log_data = {"id_usuario":id_usuario}
            logging.error("Se introdujo spoofing", extra=log_data)
            token_enviar = usuario_token + "a"
            response = requests.request("POST", url=url, json=payload)







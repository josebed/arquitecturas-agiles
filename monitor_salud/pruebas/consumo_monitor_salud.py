from faker import Faker
import requests

from faker.generator import random
import random

from typing import Dict, Any
import hashlib
import json
import logging


FORMAT = '%(asctime)s, usuario=%(id_usuario)s, %(message)s'
logging.basicConfig(filename='pruebas_monitor_salud.log', format=FORMAT, filemode="w")
logging.getLogger('root').setLevel(logging.ERROR)
logging.getLogger('werkzeug').setLevel(logging.ERROR)

def generate_hash(req_json: Dict[str, Any], codigo_seguridad):
    codigo_hash = hashlib.md5()
    json_ecoded= json.dumps(req_json, sort_keys=True).encode()
    codigo_seguridad_encoded = codigo_seguridad.encode()
    codigo_hash.update(json_ecoded)
    codigo_hash.update(codigo_seguridad_encoded)
    return codigo_hash.hexdigest()

def login(num_usuario):
    json_login = {
        "usuario": "usuario" + num_usuario,
        "contrasena": "12345"
    }
    url = "http://localhost:5080/login"

    response_login = requests.post(url = url, json=json_login)
    if(response_login.status_code ==200):
        return response_login.json()
    return False


class TestSalud():

    def setUp(self):
        self.data_factory = Faker()
        return  {
            "usuario": self.data_factory.name(),
            "servicio": self.data_factory.word(),
            "temporizador": str(self.data_factory.random_int(100, 200)),
            "nivel_estandar":  str(self.data_factory.random_int(100, 200)),
            "nivel_bajo": str(self.data_factory.random_int(100, 200)),
            "nivel_alto": str(self.data_factory.random_int(100, 200))}

if __name__ == "__main__":
    
    data_factory = Faker()

    for i in range(100):
        
        num_usuario = str(data_factory.random_int(1, 5))         

        login_data = login(num_usuario)
        if (not login_data):
            continue

        id_usuario = login_data['usuario_id']
        codigo_seguridad = login_data['codigo_seguridad']
        usuario_token = login_data["token"]

        headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(usuario_token)}
        url="http://localhost:5003/monitor_salud/{}/reglas".format(id_usuario)

        payload=TestSalud().setUp()
        request_hash = generate_hash(payload, codigo_seguridad)
        payload["hash"] = request_hash
        caso_aleatorio = random.randrange(0, 100)
        if caso_aleatorio > 66:            
            response = requests.request("POST", headers=headers, url=url, json=payload)
            
        elif caso_aleatorio > 33:
           payload["servicio"] = data_factory.word()
           response = requests.request("POST", headers=headers, url=url, json=payload)
           if(response.status_code == 200):
                log_data = {"id_usuario":id_usuario}
                logging.error("Se introdujo tampering", extra=log_data)

        else:
            log_data = {"id_usuario":id_usuario}
            logging.error("Se introdujo spoofing", extra=log_data)
            headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(usuario_token + "a")}            
            response = requests.request("POST", url=url, json=payload)

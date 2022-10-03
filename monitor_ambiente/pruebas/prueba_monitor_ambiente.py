
from faker import Faker
import logging
from core.hash import generate_hash
import requests
import random




FORMAT = '%(asctime)s, usuario=%(id_usuario)s, %(message)s'
logging.basicConfig(filename='pruebas_monitor_ambiente.log', format=FORMAT, filemode="w")
logging.getLogger('root').setLevel(logging.ERROR)
logging.getLogger('werkzeug').setLevel(logging.ERROR)



def login(num_usuario):
    json_login = {
        "usuario": "usuario" + num_usuario,
        "contrasena": "12345"
    }
    url = "http://localhost:5080/login"

    response_login = requests.post(url=url, json=json_login)
    if response_login.status_code == 200:
        return response_login.json()
    return False

class TestAmbiente:
    
    def setUp(self):
        self.data_factory = Faker()
        return {
            "usuario": str(self.data_factory.name()),
            "medicion": str(self.data_factory.random_int(100, 200)),
            "periodo":  str(self.data_factory.random_int(100, 200))
        }


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
        url="http://localhost:5010/monitor_ambiente/{}/reglas".format(id_usuario)

        payload=TestAmbiente().setUp()
        print(payload)
        request_hash = generate_hash(payload, codigo_seguridad)
        payload["hash"] = request_hash
        caso_aleatorio = random.randrange(0, 100)
        if caso_aleatorio > 66:            
            response = requests.request("POST", headers=headers, url=url, json=payload)
            
        elif caso_aleatorio > 33:
           payload["objeto_ambiente"] = data_factory.word()
           response = requests.request("POST", headers=headers, url=url, json=payload)
           if(response.status_code == 200):
                log_data = {"id_usuario":id_usuario}
                logging.error("Se introdujo tampering", extra=log_data)

        else:
            log_data = {"id_usuario":id_usuario}
            logging.error("Se introdujo spoofing", extra=log_data)
            headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(usuario_token + "a")}            
            response = requests.request("POST", url=url, json=payload)


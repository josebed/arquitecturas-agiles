import requests
import random
import logging

from faker import Faker

logger = logging.getLogger('Login accesos')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('pruebas_login.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def login(usuario, contrasena):
    json_login = {
        "usuario": usuario,
        "contrasena": contrasena
    }
    url = "http://localhost:5080/login"

    response_login = requests.post(url=url, json=json_login)
    if (response_login.status_code == 200):
        return 200
    return False


if __name__ == "__main__":

    data_factory = Faker()

    for i in range(100):
        caso_aleatorio = random.randrange(0, 100)
        if caso_aleatorio < 30:
            usuario = 'admin'
            contrasena = 'admin'
            login(usuario, contrasena)
            log_data = {'usuario': usuario}
            logger.error(f'Login Exitoso')

        elif caso_aleatorio < 60:
            usuario = data_factory.name()
            contrasena = str(data_factory.random_int(100, 200))
            login(usuario, contrasena)
            log_data = {'usuario': usuario}
            logger.error(f'Usuario o contrasena equivocadas')

        else:
            usuario = ['admin', 'user1', 'user2'][random.randrange(0, 3)]
            contrasena = str(data_factory.random_int(100, 200))
            login(usuario, contrasena)
            log_data = {'usuario': usuario}
            logger.error(f'Contrasena incorrecta')



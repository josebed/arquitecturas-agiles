from celery import Celery
from .modelos import HearbeatTable
from datetime import datetime, timedelta
import logging
import dateutil.parser
from celery.schedules import crontab
BROKER_URL = 'redis://localhost:6379'

app = Celery('tasks', broker=BROKER_URL)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(10.0, add.s(1, 1))


@app.task
def add(x, y):
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler('log_hearbeat_app.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    fecha_cad1 = str(HearbeatTable.query.order_by(HearbeatTable.fecha_creacion.desc()).first().fecha_creacion)
    fecha_cad2 = str(datetime.now())
    fecha1 = datetime.strptime(fecha_cad1, '%Y-%m-%d %H:%M:%S.%f')
    fecha2 = datetime.strptime(fecha_cad2,  '%Y-%m-%d %H:%M:%S.%f')
    res = fecha2 - fecha1
    resta_segundos = res / timedelta(seconds=1)
    print(fecha1, fecha2)
    logger.error(f'This is an exito message')
    if resta_segundos > 10:
        logger.error(f'This is an ERROR message')
    print("aqui")


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))



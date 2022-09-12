from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
import random
import requests
import logging

BROKER_URL = 'redis://localhost:6379'

app = Celery('tasks', broker=BROKER_URL)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(10.0, add.s(1, 1), expires=10)


@app.task
def add(x, y):
    if random.randrange(0, 100) > 75:
        url = " http://localhost:5020/hearbeat"
        pyload = {"mensaje": "ok"}
        metodo = "POST"
        requests.request(metodo, url=url, json=pyload)
    else:
        logger = logging.getLogger('mylogger')
        logger.setLevel(logging.ERROR)
        handler = logging.FileHandler('log_hearbeat_consumer_app.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.error(f'This is an ERROR message')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))




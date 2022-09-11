from celery import Celery
from datetime import timedelta
from celery.schedules import crontab
BROKER_URL = 'redis://localhost:6379'

app = Celery('tasks', broker=BROKER_URL)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(1.0, add.s(1, 1), expires=10)


@app.task
def add(x, y):
    z = x + y
    print(z)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))



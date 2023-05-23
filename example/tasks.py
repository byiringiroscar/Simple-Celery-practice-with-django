from celery import shared_task
from time import sleep
from celery import Celery

# app = Celery('tasks', backend='redis://127.0.0.1:6379', broker='redis://127.0.0.1:6379')
# app.conf.broker_url = 'redis://127.0.0.1:6379/0'



@shared_task(bind=True)
def go_to_sleep(self, duration):
    sleep(duration)
    return 'Done'
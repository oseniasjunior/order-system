from celery import shared_task
from core import actions


@shared_task(bind=True, max_retries=3, queue='celery')
def populate_test(self):
    try:
        actions.TestActions.populate()
    except Exception as exc:
        self.retry(exc=exc, countdown=2 ** self.request.retries)

from __future__ import absolute_import

import os
from celery import Celery

app = Celery('codeTesting_project', broker='amqp://', backend='amqp://', include=['codetesting_app.tasks'])

@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))

# Optional configuration, see the application user guide.
app.conf.update(
	CELERY_TASK_SERIALIZER='json',
	CELERY_ACCEPT_CONTENT=['json'],
	CELERY_RESULT_SERIALIZER='json',
)

if __name__ == '__main__':
	app.start()
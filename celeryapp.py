from celery import Celery
from mail import send_email
app = Celery('proj',
             broker='redis://redis:6379/0',
             backend='redis://redis:6379/0',
             )

@app.task
def send_email_t(meeting):
    send_email(meeting)



# if __name__ == '__main__':
#     app.start()

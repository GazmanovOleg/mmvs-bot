from celery import Celery
from mail import send_email
app = Celery('proj',
             broker='redis://redis:6379/0',
             backend='redis://redis:6379/0',
             )

# Optional configuration, see the application user guide.
#app.conf.update(
#    result_expires=3600,
#)



@app.task
async def send_email_t(meeting):
    await send_email(meeting)



# if __name__ == '__main__':
#     app.start()

# IgRZJE=5%Uzq
import base64
import smtplib, ssl
import emails
import datetime
from aMgnt.models import *
from rAsset.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, DEFAULT_FROM_EMAIL, EMAIL_PORT, EMAIL_HOST

from celery.decorators import task

@task(autoretry_for=(Exception,),retry_jitter=True,retry_backoff=True,max_retries=1)
def send_general_incidents_email_notifications(recipient_email_list=['test@rokelbank.sl']):
    #Implement a way to return list of sucessful and unsucessful email addresses
    # so it can be logged by celery in db and Django admin interface.

    #Create email message
    rokel_logo = base64.b64encode(open("aMgnt/static/aMgnt/assets/logo/RCB.jpg", "rb").read())
    context = {'year': str(datetime.datetime.now().year), 'rokel_logo': rokel_logo.decode('utf-8')} 
    email_template = open('aMgnt/email_notification_templates/GeneralIncidentsEmail.html').read()
    for val in context:
        email_template = email_template.replace('{{ '+ val +' }}',context[val])
    message = emails.html(
        html=email_template,
        subject='Incidents Notification',
        mail_from=('RCBankPortal', EMAIL_HOST_USER),
        )

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Send email notification to whom it may concern.
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=context) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        for recipient_email in recipient_email_list:
            server.sendmail(EMAIL_HOST_USER,recipient_email,message.as_string())
        server.quit()

    return 'Email notifications sucessfully sent'

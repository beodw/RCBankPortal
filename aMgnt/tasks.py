# IgRZJE=5%Uzq
import base64
import smtplib, ssl
import emails
import datetime
from aMgnt.models import *
from django_celery_beat.models import *
from django_celery_results.models import TaskResult
from rAsset.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, DEFAULT_FROM_EMAIL, EMAIL_PORT, EMAIL_HOST

from celery.decorators import task

@task(autoretry_for=(Exception,),retry_jitter=True,default_retry_delay= 8 * 60 * 60,retry_backoff=False,max_retries=3)#change to 21 tries for weekly notifications.
def send_general_incidents_email_notifications(recipient_email_list=["beodwilson@gmail.com"]):
    #Email sent weekly. Retries every 8 hours, i.e. 3 times a day, until success.
    #Create email message
    forwarded_incident =  GeneralIncident.objects.filter(resolved=2)# resolved is 2 when forwarded to supervisor.
    
    today = datetime.date.today()

    if forwarded_incident:
        context = { 
                    'year': str(today.year),
                } 
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

        return 'Email notifications successfully sent'
    else:
        return 'There are no incidents forwarded to a supervisor.'

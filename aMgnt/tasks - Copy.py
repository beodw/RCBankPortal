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

@task(autoretry_for=(Exception,),retry_jitter=False,default_retry_delay= 8 * 60 * 60,retry_backoff=False,max_retries=3)#change to 21 tries for weekly notifications.
def send_general_incidents_email_notifications(recipient_email_list=['beodwilson@gmail.com']):
    #Have a task scheduled weekly.
    #Have exactly one worker execute the task retrying each day until success.
    #If there is no success on the 7th day then task is considered to have failed. 
    #Show notification in the admin section stating that no emails were sent for that week due to an error.
    #The worker, checks if the most recent successful invocation, if there exists any, is less than a week ago
    #---> reschedule task for a week from the success date of the afore mentioned invocation. 
    #otherwise send the email.

    today = datetime.date.today()

    #Check if the most recent successful invocation, if there exists any, is less than a week ago.
    #if date done is less than a week then set it to a week from that date and save()
    task_result = TaskResult.objects.filter(status='SUCCESS').last()

    elapsed_time = today -  task_result.date_done.date()

    periodic_task = PeriodicTask.objects.get(name="Send General Incidents Notification")


    interval_schedule = IntervalSchedule.objects.get(id=periodic_task.interval_id)

    # a_week = datetime.timedelta(days=7)
    a_day = datetime.timedelta(days=7)

    if elapsed_time < a_day: #last success less than a week ago so reschedule next date and revoke current task.
        
        # interval_schedule.every = (7 - elapsed_time.days) + 1
        interval_schedule.every = (1 - elapsed_time.days) + 1

        interval_schedule.period = 'days'

        interval_schedule.save()

        # return "It has not been a week since last successful notification."

        return "It has not been a day since last successful notification."

    #Create email message
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
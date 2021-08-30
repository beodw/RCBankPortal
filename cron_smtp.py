import schedule
import time
import smtplib, ssl

def job():
    host_name = 'aetrf.tech'
    port = 465  # For SSL on SMTP
    username = 'noreply@rokelbank.sl'
    password = 'P@33w0rd54321'

    #Message details
    subject = 'This is a test'
    message_body = 'There are unresolved incidents. Please give them some attention.'
    from_addr = 'noreply@rokelbank.sl'
    to_addr = 'test@rokelbank.sl'

    message = 'Subject: {}\nFrom: {}\n{}'.format(subject,from_addr, message_body)

    # Create a secure SSL context
    context = ssl.create_default_context()

    #Send email to email server.
    with smtplib.SMTP_SSL(host_name, port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr,to_addr,message)
        server.quit()

# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.at("10:30").do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
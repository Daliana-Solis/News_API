import smtplib, ssl  #email library

def send_email(message):
    #gmail accounts
    host = "smtp.gmail.com"
    port = 465

    #username = gmail
    #password -- gmail created password
    username = "X"
    password = "X"

    #receiver = gmail
    receiver = "X"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
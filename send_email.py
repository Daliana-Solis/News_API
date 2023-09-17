import smtplib, ssl  #email library

def send_email(message):
    #gmail accounts
    host = "smtp.gmail.com"
    port = 465

    username = "daliana.solis29@gmail.com"
    password = "gvpn jxut ilap nsye"

    receiver = "daliana.solis29@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
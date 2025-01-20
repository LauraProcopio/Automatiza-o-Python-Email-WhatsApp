import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = 'email' # Seu e-mail
    password = 'senha'  # Evite armazenar a senha diretamente no código

    # Configuração do servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    # Criação da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Adição do corpo do e-mail
    msg.attach(MIMEText(body, 'plain'))

    # Envio do e-mail
    server.send_message(msg)
    server.quit()

# Chamada da função para enviar um e-mail de teste
send_email('email teste', 'Corpo do e-mail', 'email_destino')



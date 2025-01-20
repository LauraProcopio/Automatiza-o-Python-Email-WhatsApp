import csv
import smtplib
import email.message
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr

email_enviados = []
email_enviados_antes = []
email_assunto = 'Feliz Dia do Estagiário!'

def enviar_email(nome_estagiario, to, image_path) -> None:
    # Verifica se o email já foi enviado
    if to in email_enviados + email_enviados_antes:
        print(f'Email enviado anteriormente - {to}')
        return

    # Criando o objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['Subject'] = email_assunto
    msg['From'] = formataddr(('nome', 'email'))  # Seu email
    msg['To'] = to

    # Corpo do email em HTML
    email_corpo = f'''
    <html>
<body style="font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; padding: 20px;">
    <div style="background-color: #ffffff; border-radius: 10px; padding: 20px; max-width: 600px; margin: auto;">
        <h2 style="color: #333333;">Feliz Dia do Estagiário!</h2>
        <p style="font-size: 18px; color: #555555;">
            <strong style="color: #2c3e50;">{nome_estagiario}</strong>,<br>
            Talento e dedicação fazem a diferença!
        </p>
        <p style="font-size: 16px; color: #777777; line-height: 1.6;">
            Nesta semana, comemoramos o Dia do Estagiário, uma data especial para reconhecer o esforço, a dedicação e a energia que você traz ao IFMT.<br>
            Agradecemos por sua contribuição diária e esperamos que esta experiência seja apenas o início de uma carreira brilhante e repleta de conquistas.
        </p>
        <img src="cid:imagem1" style="width: 500px; height: 500px; border-radius: 10px; margin-top: 20px;">
    </div>
</body>
</html>
    '''
    
    # Anexando o corpo ao email
    msg.attach(MIMEText(email_corpo, 'html'))

    # Anexando a imagem
    with open(image_path, 'rb') as img:
        mime = MIMEImage(img.read())
        mime.add_header('Content-ID', '<imagem1>')
        mime.add_header('Content-Disposition', 'inline', filename=f'{nome_estagiario}.png')
        msg.attach(mime)

    # Enviando o email
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('email', 'senha')  # Senha gerada pelo Google
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        s.quit()
        
        email_enviados.append(to)
        print(f'Email enviado - {to}')

        # Salva o email no arquivo de email enviado
        with open('emailenviado.txt', 'a') as arquivo:
            arquivo.writelines(f'{to}\n')
    
    except Exception as e:
        print(f'Erro ao enviar email para {to}: {e}')

# Abre o arquivo de emails enviados
try:
    with open('emailenviado.txt', 'r') as arquivo:
        linha = arquivo.readlines()
        email_enviados_antes = [email.replace('\n', '') for email in linha]  
except FileNotFoundError:
    # Cria o arquivo de email enviado, caso não exista
    with open('emailenviado.txt', 'w') as arquivo:
        ...

# Lê o arquivo CSV que contém o nome, email e caminho da imagem personalizada
with open('planilhaestagiarios3.csv', 'r', encoding='utf8', newline='') as arquivo:
    linha = csv.reader(arquivo)
    lPessoas = [x for x in linha] # percorre as linhas do arquivo

# Percorre a lista de emails     
for pessoa in lPessoas:
    nome_estagiario = pessoa[0]  # Nome do estagiário
    email_estagiario = pessoa[1]  # Email do estagiário
    image_path = pessoa[2]  # Caminho da imagem personalizada

    # Chama a rotina de envio de email passando o nome, email e imagem
    enviar_email(nome_estagiario, email_estagiario, image_path)
    sleep(2)
    
    
    

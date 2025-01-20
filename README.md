# Automatização de Envio de Mensagens e E-mails com Python

Este repositório contém scripts Python para a automatização do envio de e-mails e mensagens via WhatsApp, com o objetivo de simplificar processos de comunicação e melhorar a eficiência. Os scripts utilizam bibliotecas confiáveis como **smtplib**, **selenium**, **pandas** e **urllib**, permitindo automação de tarefas repetitivas tanto para e-mails quanto para mensagens no WhatsApp Web.

---

## Funcionalidades

### 1. **Envio de E-mails Automático**
- Envia mensagens em massa via e-mail.
- Utiliza um arquivo CSV com os endereços de e-mail dos destinatários.
- Verifica se o e-mail já foi enviado anteriormente, evitando duplicações.

### 2. **Envio de Mensagens pelo WhatsApp Web**
- Envia mensagens personalizadas em massa via WhatsApp.
- Usa Selenium para controlar o navegador Chrome e acessar o WhatsApp Web.
- Carrega contatos e mensagens a partir de um arquivo Excel.

---

## Tecnologias Utilizadas

### Linguagem
- **Python**

### Bibliotecas
- **smtplib**: Para envio de e-mails.
- **selenium**: Para automação de envio de mensagens no WhatsApp Web.
- **pandas**: Para manipulação de dados (CSV/Excel).
- **urllib**: Para codificação de texto na URL do WhatsApp.

---

## Como Usar

### 1. **Envio de E-mails**
1. Prepare um arquivo **CSV** com os endereços de e-mail dos destinatários.
2. Defina o **assunto** e o **corpo** do e-mail no código.
3. Execute o script para enviar as mensagens.

### 2. **Envio de Mensagens via WhatsApp**
1. Prepare um arquivo **Excel** com os contatos no seguinte formato:
   - Nome
   - Número de telefone
   - Mensagem personalizada
2. Altere os parâmetros de número do WhatsApp e mensagem no código, conforme necessário.
3. Execute o script para enviar as mensagens.

import schedule
import time
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


# Carrega as variáveis de ambiente
load_dotenv()

# Dados do e-mail
EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")

# Lista de links
LINKS = [
    os.getenv("LINK1"),
    os.getenv("LINK2")
]


def rotina_dev():
    """Função que abre os sites de estudos e envia um e-mail motivacional."""

    # Abre os sites configurados
    for link in LINKS:
        if link:
            webbrowser.open(link)
            print(f"Abrindo {link}")

    # Corpo do e-mail
    assunto = "Automação de Estudos — Executando a build da sua evolução."
    corpo = """
Olá, desenvolvedora!

O ambiente está configurado, os processos estão prontos e o terminal te espera.

É hora de compilar conhecimento, debugar obstáculos e versionar sua própria evolução.

O deploy da sua jornada começa AGORA. Bora codar, aprender e construir um futuro extraordinário — linha por linha, commit por commit.

Seu código roda, seu mundo funciona e seu sucesso tá em deploy contínuo.

O mundo é open-source. Bora construir o seu repositório de conquistas!

#KeepCoding
    """

    # Configura a mensagem
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = EMAIL_DESTINO
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    # Envia o e-mail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL, SENHA)
        servidor.send_message(msg)
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")


# Agenda a rotina para rodar todos os dias às 19:30
schedule.every().day.at("19:30").do(rotina_dev)

print("Automação da Dev rodando...")

# Loop infinito para manter a automação ativa
while True:
    schedule.run_pending()
    time.sleep(60)

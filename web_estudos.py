import schedule
import time
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


load_dotenv()


# Dados de Email
EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")

print("Email:", EMAIL)
print("Senha:", SENHA)
print("Email destino:", EMAIL_DESTINO)


# Função que abre os sites e manda o e-mail
def rotina_dev():
    # Abre os sites
    webbrowser.open("https://www.alura.com.br")
    webbrowser.open("https://www.grancursosonline.com.br")

    # Monta a mensagem
    assunto = "Automação de estudos — Executando a build da sua evolução."
    corpo = """
    Olá, desenvolvedora!

    O ambiente está configurado, os processos estão prontos e o terminal te espera.

    É hora de compilar conhecimento, debugar obstáculos e versionar sua própria evolução.

    O deploy da sua jornada começa AGORA. Bora codar, aprender e construir um futuro extraordinário — linha por linha, commit por commit.

    Seu código roda, seu mundo funciona e seu sucesso tá em deploy contínuo.

    O mundo é open-source. Bora construir o seu repositório de conquistas!

    #KeepCoding 
    """

    # Configura o e-mail
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = EMAIL_DESTINO
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    # Envia o e-mail via SMTP Gmail 
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL, SENHA)
        servidor.send_message(msg)
        servidor.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Agenda para rodar todo dia às 19:30
schedule.every().day.at("19:30").do(rotina_dev)

print("Automação da Dev rodando...")

while True:
    schedule.run_pending()
    time.sleep(60)

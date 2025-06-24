import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = "doutoradev@gmail.com"
SENHA = "mzly zmkh wrky qolj"  # Sua senha de app
EMAIL_DESTINO = "wellen.acarvalho@gmail.com"

msg = MIMEMultipart()
msg['From'] = EMAIL
msg['To'] = EMAIL_DESTINO
msg['Subject'] = "Teste rápido Doutora Dev 🚀"

corpo = "Se você recebeu esse email, a automação está funcionando 100%! 💖"

msg.attach(MIMEText(corpo, 'plain'))

try:
    print("Tentando enviar email...")
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(EMAIL, SENHA)
    servidor.send_message(msg)
    servidor.quit()
    print("Email enviado com sucesso! 🎉")
except Exception as e:
    print(f"Erro ao enviar email: {e}")

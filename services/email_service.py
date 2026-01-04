import smtplib
import email.message
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv(("EMAIL_PASSWORD"))

assunto = "Confirmação de Email"

corpo = """
<p>Prezados</p>
<p>Segue email automático</p>"""

def enviar_email (destinatario):
    msg = email.message.Message()
    msg["Subject"] = assunto
    msg["From"] =  EMAIL_ADRESS
    msg["To"] = destinatario
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo)

    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(EMAIL_ADRESS, EMAIL_PASSWORD)
        s.sendmail(EMAIL_ADRESS, [destinatario], msg.as_string().encode("utf-8"))
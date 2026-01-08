import smtplib
import email.message
from dotenv import load_dotenv
import os
import random

load_dotenv()

EMAIL_ADRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv(("EMAIL_PASSWORD"))

def enviar_email(destinatario):
    codigo_gerado = random.randint(1000, 9999)

    assunto = "Confirmação de Email"

    corpo = f"""
        <p>Prezado</p>
        <p>Segue código de verificação <strong>{codigo_gerado}</strong></p>
    """

    msg = email.message.Message()
    msg["Subject"] = assunto
    msg["From"] = EMAIL_ADRESS
    msg["To"] = destinatario
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo)

    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(EMAIL_ADRESS, EMAIL_PASSWORD)
        s.sendmail(EMAIL_ADRESS, [destinatario], msg.as_string().encode("utf-8"))

    return codigo_gerado


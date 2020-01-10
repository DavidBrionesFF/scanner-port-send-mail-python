import datetime
import re
import smtplib, ssl
from util.properties import appContext, ContextApplication


def getMailConnection(smtp_server, port, username, passwod):
    context = ssl.create_default_context()
    server = None
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)  # Asegurar la conexion
        server.login(username, passwod)
        print("Connextion succefuly!")
    except Exception as e:
        # Imprimir error al mensaje
        print("Connextion error!")
        print(e)

    return server

def getTemplate(nameTemplate):
    file = open("templates/" + nameTemplate, "r", encoding='utf-8')
    data = ""

    for line in file.readlines():
        data += line
    data = data.encode('utf-8')
    regex_interpolation = r'(?is){{+([A-Za-z0-9sW.-]{1,})}}' + ''

    data = re.sub(r'(?is){{date}}', str(datetime.datetime.now()), data.decode('utf-8'))
    data = re.sub(r'(?is){{port}}', str(ContextApplication.port_context), data.encode().decode())

    for case in re.findall(regex_interpolation, data.encode().decode()):
        sub_regex = r'(?is){{' + str(case) + '}}'
        value = appContext.getPropertie(case)
        data = re.sub(
            sub_regex,
            value.encode().decode(),
            data)
    return data.encode('utf-8')

def sendMail(nameTemplate):
    message = getTemplate(nameTemplate)
    connection = getMailConnection(
        username=appContext.getPropertie("bytepl.mail.username"),
        passwod=appContext.getPropertie("bytepl.mail.password"),
        smtp_server=appContext.getPropertie("bytepl.mail.server"),
        port=appContext.getPropertie("bytepl.mail.port")
    )
    connection.sendmail(
        appContext.getPropertie("bytepl.mail.username"),
        appContext.getPropertie("bytepl.application.until-client"),
        message
    )
# Scanner_port_send_mail_python
Escanea puertos con Python y envia correos

Debemos de configurar las propiedades del templates/application.properties

# Variables de contexto
bytepl.application.name=Scanner Port for Lab Byte PL # Tema de los servicios
bytepl.application.until-client= # Corre donde se recibe los puertos abiertos

# Propiedades de llegar el correo
bytepl.mail.username= # Nombre de usuario de correo
bytepl.mail.password= # Contrasena de correo
bytepl.mail.server= # Servidor de correo
bytepl.mail.port= # Puerto del servidor de correo

# Escaneo de puertos
bytepl.scan.port-start=80 # Puerto donde inicia el escaneo
bytepl.scan.port-end=91 # Puerto donde finaliza el escaneo

# Hosts
Luego debemos de agregar los host a escanear en el archivo templates/hosts

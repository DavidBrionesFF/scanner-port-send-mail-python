from errno import ECONNREFUSED
from functools import partial
from multiprocessing import Pool
import socket

from util.mail import sendMail
from util.properties import appContext, ContextApplication

NUM_CORES = 4

def ping(host, port):
       try:
           socket_req = socket.socket()
           socket_req.connect((host, port))
           print(str(port) + " Open")
           ContextApplication.port_context = port
           sendMail("message_welcome.txt")
           socket_req.close()
           return port
       except socket.error as err:
           if err.errno == ECONNREFUSED:
               return False
           raise


def scan_ports(host):
       p = Pool(NUM_CORES)
       ping_host = partial(ping, host)
       return filter(bool, p.map(ping_host, range(
                        int(appContext.getPropertie('bytepl.scan.port-start')),
                        int(appContext.getPropertie('bytepl.scan.port-end')))
                     ))
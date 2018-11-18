import socket
from threading import *
import logging
import os
import signal

log = logging.getLogger(__name__)
LOGFORMAT = "%(asctime)s | %(levelname)-2s | %(threadName)-2s | %(module)-2s | %(funcName)-2s | %(message)s"
logging.basicConfig(format=LOGFORMAT, level=logging.DEBUG)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clients = [] # Maintain a list of clients
host = socket.gethostname()
#quit = False
port = 9999

log.info("Host: %s" % str(host))
log.info("Port: %s" % str(port))

serversocket.bind((host, port))
# Que up to 5 requests
serversocket.listen(5)

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
            received_this = str(self.sock.recv(1024).decode())
            log.info('Client sent: ' + str(received_this))
            emergency = "No Emergency Inputted"
            if(received_this.lower() == "shelter"):
                log.info("SHELTER!")
                emergency = "shelter"
            elif(received_this.lower() == "evacuate"):
                log.info("EVACUATE!")
                emergency = "evacuate"
            elif(received_this.lower() == "lockdown"):
                log.info("LOCKDOWN!")
                emergency = "lockdown"
            elif(received_this.lower() == "lockout"):
                log.info("LOCKOUT!")
                emergency = "lockout"
            elif(received_this.lower() == "activeshooter"):
                log.info("ACTIVE SHOOTER!")
                emergency = "activeshooter"
            self.sock.send(("Received data: " + str(emergency)).encode('utf-8'))
            log.info("Self: " + str(self.sock))
            if(emergency != "No Emergency Inputted"):
                for client in clients:
                    if(client == self.sock):
                        continue
                    log.info("Client: " + str(client))
                    client.send(("Received data: " + str(emergency)).encode('utf-8'))

print ('server started and listening')

try:
    while True:
        clientsocket, address = serversocket.accept()
        clients.append(clientsocket)
        client(clientsocket, address)
except KeyboardInterrupt:
    serversocket.close()
    
    

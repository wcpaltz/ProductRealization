# import socket programming library 
import socket 
import time

# import thread modules 
from _thread import *
import threading 

# Other imports
import logging

# Logging
log = logging.getLogger(__name__)
LOGFORMAT = "%(asctime)s | %(levelname)-2s | %(threadName)-2s | %(module)-2s | %(funcName)-2s | %(message)s"
logging.basicConfig(format=LOGFORMAT, level=logging.DEBUG)

clients = [] # Maintain a list of clients
alerts_list = ["lockdown", "lockout", "evacuate", "shelter", "medical", "activeshooter"]
current_emergency = "na"
#received = ""

def threaded(c, my_pid):
    """
    Functionality:
        Needed a simple way communicate with clients separately.
        Each time this function is called a new thread is created.
        And the only time this thread is closed is when the client
        designates its closure. This thread also sends alerts to
        all the other clients that are connected to the server
        if certain parameters are met.
    Input:
        c       : socket object (connection)
        my_pid  : int
    Output:
        N/A
    """
    global current_emergency
    if(current_emergency != "na"):
        c.send((str(current_emergency)).encode('utf-8'))

    try:
        while True: 
            # data received from client 
            received = str(c.recv(1024).decode())
            log.info("Received: " + str(received))

            # if there is no data, close client and remove
            # from the clients list, this may populate twice
            # since the client has technically two threads
            if not received: 
                log.info("pid: [" + str(my_pid) + "] has disconnected") 
                for client in clients:
                    if(client == c):
                        clients.remove(client)
                    log.info("Removed client with pid: " + str(my_pid))
                break
            elif(received in alerts_list):
                # Send alert to entire client base
                current_emergency = received
                log.info("Current Emergency : " + str(current_emergency))
                for client in clients:
                    client.send((str(received)).encode('utf-8'))
            elif(received == "reset"):
                current_emergency = received
                for client in clients:
                    client.send((str(received)).encode('utf-8'))
            else:
                # Do Nothing
                pass
                
                
        # close connection 
        c.close()
    except:
        log.warning("Client closed unexpectedly [Shutting Down Client]")
        c.close()
        
def Main(): 
    """
    Functionality:
        Needed a simple way to create a server and listen for new
        connections from clients. This function will continue to
        loop until the socket is closed, in which it will shut down 
        the server gracefully. A new thread will also be created 
        everytime a client connects to the server. A list of all the
        clients will also be collected as long as the server is running.
    Input:
        N/A
    Output:
        N/A
    """
    #initializing variables
    host = "" 
    global clients
    global alerts_list
    # reserving port 49000
    # can be whatever port you'd like
    port = 49000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    s.bind((host, port)) # bind the socket to the address
    log.info("socket binded to port: " + str(port)) 
   
    s.listen(5) # put the socket into listening mode
    log.info("socket is listening") 
    log.info(socket.gethostname())
    # for loop until client wants to exit 
    while True: 
        c, addr = s.accept() # establish client connection
        
        clients.append(c) # add new client to clients list
        log.info("Total Clients Connected: " + str(len(clients)))
        log.info("Connected to : " + str(addr[0]) + ":" + str(addr[1])) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c, addr[1]))
#        start_new_thread(current_emergency, ())
    
    # shut down server
    s.close() 
  
  
if __name__ == '__main__':
    """
    Functionality:
        Calls Main(), when script is called locally
    Input:
        N/A
    Output:
        N/A
    """
    Main()
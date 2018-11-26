# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 

clients = [] # Maintain a list of clients
#print_lock = threading.Lock() 


# thread fuction 
def threaded(c, my_pid):
    while True: 
        # data received from client 
        data = str(c.recv(1024).decode())
        if not data: 
            print("pid: [" + str(my_pid) + "] has disconnected") 
            for client in clients:
                if(client == c):
                    clients.remove(client)
                print("Removed client with pid: " + str(my_pid))
            # lock released on exit 
#            print_lock.release() 
            break
        else:
            for client in clients:
                client.send(("Received: " + str(data)).encode('utf-8'))
  
    # connection closed 
    c.close() 
        
def Main(): 
    host = "" 
    global clients
    
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 49000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
        clients.append(c)
        print(c.getsockname())
        print("Total Clients Connected: " + str(len(clients)))
        # lock acquired by client 
#        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c, addr[1]))
#        print_lock.release()
    s.close() 
  
  
if __name__ == '__main__': 
    Main()
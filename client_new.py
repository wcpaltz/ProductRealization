# Import socket module 
import socket 
import time

# import thread module 
from _thread import *
import threading 

def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 49000
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    start_new_thread(receive_data, (s,))
    
    while True:
        # message you send to server 
        message = input('Enter Emergency Below: \n')
        
        # message sent to server
        s.send(message.encode('ascii')) 
        
        time.sleep(2)
        # ask the client whether he wants to continue 
        ans = input('\nIs the emergency still happening? (y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    # close the connection 
    s.close() 


def receive_data(s):
    while True:
        # messaga received from server
        data = s.recv(1024)
        if not data:
            break
            
        # print the received message 
        # here it would be a reverse of sent message 
        print('\nALERT: Received from the server :',str(data.decode('ascii')))
        
    s.close()
  
if __name__ == '__main__': 
    Main()
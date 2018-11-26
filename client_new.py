# Import socket module 
import socket 
import time

# import thread module 
from _thread import *
import threading 

def Main():
    """
    Functionality:
        Needed a simple way to connect to a socket on a designated 
        server. This function will continue to loop until the 
        connection is closed, in which it will close the connection
        gracefully. A thread will also be created to receive data
        from the server. 
    Input:
        N/A
    Output:
        N/A
    """
    
    # IP (local host)
    # this can be changed
    host = '127.0.0.1'
  
    # Define port that's to be connected to
    port = 49000
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server with local IP
    s.connect((host,port)) 
  
    start_new_thread(receive_data, (s,))
    
    while True:
        # message you send to server 
        message = input('Enter Emergency Below: \n')
        
        # send message to server
        s.send(message.encode('ascii')) 

        # sleep to receive data from server
        # since it is on another thread
        time.sleep(1)
        
        # client want to continue?
        ans = input('\nIs the emergency still happening? (y/n) :') 
        if ans == 'y': 
            continue
        else:
            break
            
    s.close() # close the connection 


def receive_data(s):
    """
    Functionality:
        Needed a simple way asynchronously receive data from 
        the server the client is connected to. A new thread 
        is create since sending and receiving are two seperate 
        tasks. Without a tread the server would not be able to 
        send alerts to the client asynchronously. 
    Input:
        s : socket
    Output:
        N/A
    """
    try:
        while True:
            # messaga received from server
            data = s.recv(1024)
            if not data:
                break

            # print the received message 
            # here it would be a reverse of sent message 
            print('\nALERT: Received from the server :',str(data.decode('ascii')))    
        s.close() # close the connection 
    except:
        # if exception occurs
        s.close() # close the connection 

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
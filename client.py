import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'Wills-MacBook-Pro.local'
port = 9999
s.connect((host,port))
    
def main():
    def send_data(send_this):
        s.send(send_this.encode()) 
#        data = ''
#        data = s.recv(1024).decode()
#        print (data)

    while True:
        data = input('Enter Input Below: \n')
        if(data == "quit"):
            break
        send_data(data)
        time.sleep(1)

    s.close()

def receive_data():
    while True:
        data = s.recv(1024).decode()
        if(data != ""):
            print(str(data))
#            print("inside receive_data")
        
    
if __name__ == '__main__':
    t1 = threading.Thread(target=main, args=[])
    t2 = threading.Thread(target=receive_data, args=[])
    t1.start()
    t2.start()
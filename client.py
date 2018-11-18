import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'Wills-MacBook-Pro.local'
    port = 9999
    s.connect((host,port))
    
    def send_data(send_this):
        s.send(send_this.encode()) 
        data = ''
        data = s.recv(1024).decode()
        print (data)
    
    
    while True:
        data = input('Enter: ')
        if(data == "quit"):
            break
        send_data(data)

    s.close()

if __name__ == '__main__':
    main()
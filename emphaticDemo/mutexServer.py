import socket, os  
import threading             # Import socket module

mutex = threading.Lock()

def mutexThread(client):              
    picture = ""
    while True:                       
        print("Enter name for new file")
        picture = input()          
        infile = open(picture,'wb')
        #print('Got connection from', addr)
        print("Incoming file...")
        download = client.recv(1024)
        while (download):
            print("File downloading")
            infile.write(download)
            download = client.recv(1024)
        if not download:
            print('Nothing to download')
            mutex.release()
            break
        infile.close()
        print("File received successfully!")
        client.close()  

def Main():
    s = socket.socket()         
    host = socket.gethostname() 
    port = 50001                 
    s.bind((host, port))       
    s.listen(5)   
    while True:
        client, addr = s.accept() 
        mutex.acquire()
        print("Connected to:", addr[0], ":", addr[1])
        newThread = threading.Thread(target=mutexThread(client), name="newThread")  
        newThread.start()
    s.close()

if __name__ == '__main__':
    Main()

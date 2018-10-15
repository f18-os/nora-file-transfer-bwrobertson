
import socket 
  
  
def Main(): 
    host = socket.gethostname()
    port = 50002
  
    mutexSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    mutexSocket.connect((host,port)) 
    fileFound = False
    file = ""
    while True: 
        while(fileFound == False):
            file = input("Please enter the file you want to send\n")
            try:
                outfile = open(file,'rb')
                fileFound = True
            except IOError:
                print("File not found. Please enter correct file name!")
        print("Uploading file...")
        upload = outfile.read(1024)
        while(upload):
            print("Uploading file...")
            mutexSocket.send(upload)
            upload = outfile.read(1024) 
        outfile.close()
        print(file + " Upload complete!")
        data = mutexSocket.recv(1024) 
  
        print('Received from the server :',str(data)) 
   
        again = input('\nSend another message(y/n) :') 
        if again == 'y': 
            continue
        else: 
            break
    mutexSocket.close() 
  
if __name__ == '__main__': 
    Main() 

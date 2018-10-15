

import socket 

from _thread import *
import threading 
  
print_lock = threading.Lock() 
  
def threaded(mutexCli): 
    picture = ""
    while True: 
        picture = input("Enter name for new file\n")
        infile = open(picture, 'wb')
        download = mutexCli.recv(1024) 
        while (download):
            print("File downloading")
            infile.write(download)
            download = mutexCli.recv(1024)
        infile.close()
        print(picture + "Download Complete!")
        if not data: 
            print('Closing') 
              
            print_lock.release() 
            break
  
        data = data[::-1] 
  
        mutexCli.send(data) 
  
    mutexCli.close() 
  
  
def Main(): 
    host = socket.gethostname() 
  
    port = 50002
    mutexServe = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    mutexServe.bind((host, port)) 
    print("Socket bound!", port) 
  
    mutexServe.listen(5) 
    print("Socket listening!") 
  
    while True: 
  
        mutexCli, addr = mutexServe.accept() 
  
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        start_new_thread(threaded, (mutexCli,)) 
    mutexServe.close() 
  
  
if __name__ == '__main__': 
    Main() 

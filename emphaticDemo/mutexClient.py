import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 50001                 # Reserve a port for your service.

s.connect((host, port))
fileFound = False
while(fileFound == False):
	print("Please enter the file you want to send") 
	picture = input() #designates the file you want to send
	try:
		outfile = open(picture,'rb')
		fileFound = True
	except IOError:
		print("File not found. Please enter correct file name!")
print('Uploading file...')
upload = outfile.read(1024) #sends the file 100 bytes at a time
while (upload):
    print('Uploading file...') #Lets the user know that the process is...processing
    s.send(upload)
    upload = outfile.read(1024)
outfile.close()
print("Upload complete!")
s.close 

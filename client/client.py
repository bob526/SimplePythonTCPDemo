from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort) )
filename = raw_input('What file do you want to download?\n')

message = 'GET '+filename

clientSocket.send(message.encode())

binaryFileStr = clientSocket.recv(1024)

if 'Server:' in binaryFileStr[0:7]:
    print(binaryFileStr)
else:
    requestFileptr = open(filename, 'wb')
    requestFileptr.write(binaryFileStr)
    requestFileptr.close()

clientSocket.close()

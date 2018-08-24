from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The Server is Ready!')

while True:
    connectionSocket, addr = serverSocket.accept()

    message = connectionSocket.recv(1024).decode()
    print('Receive message: '+message)

    #Check format correct or not
    if 'GET' in message[0:3]:
        #'GET 'array index is 0,1,2,3->So the filename should start in idx 4
        requestFilename = message[4:]
        print('Client want to download: '+requestFilename)

        try:
            fileptr = open(requestFilename, 'rb')
            binaryStr = fileptr.read()

            #In my opinion, no need for encode, because it's binary
            connectionSocket.send(binaryStr)
        except IOError:
            errMesg = 'Server: Error: Can\'t open '+requestFilename
            print(errMesg)
            connectionSocket.send(errMesg)



    else:
        FormatwrongMesg = 'The message is wrong.'
        print(FormatwrongMesg)
        connectionSocket.send(FormatwrongMesg)

    connectionSocket.close()

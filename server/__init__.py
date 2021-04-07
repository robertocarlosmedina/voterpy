from socket import *
from dataBase import JsonFiles

## ____ ON BUILDING ______


cand = JsonFiles("./server/dataBase/candidates.json")
# print(cand.get())

class Server:
    serverName = "localhost"
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) ## I the port is in use this instruction will and
                                                         ## the process in the port to make it able to be use
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(1)

    print('The server id on state Run.')
    def runServer(self):
        while True:
            connectionSocket, addr = self.serverSocket.accept()
            sentence = connectionSocket.recv(1024).decode()
            connectionSocket.send(str(cand.getById(int(sentence))).encode())
            connectionSocket.close()

server = Server()
server.runServer()


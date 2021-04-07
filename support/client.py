from socket import *

class User:
    serverName = 'localhost'
    serverPort = 12000
    menssages = None
    
    def serverConectAndSend(self, sentence):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.serverName, self.serverPort))
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        self.menssages = modifiedSentence.decode()
        clientSocket.close()
        return self.menssages
    
cli  = User()
print(cli.serverConectAndSend("1"))
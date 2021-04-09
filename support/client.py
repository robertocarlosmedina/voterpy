from socket import *

class User:
    serverName = 'localhost'
    serverPort = 12000
    menssages = None
    original_path = "./server/dataBase/"
    path = ""
    # comands = {"get":2,"getById":2,"post":1, "put":2, "delete":4}
    
    def serverConectAndSend(self, sentence):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.serverName, self.serverPort))
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        self.menssages = modifiedSentence.decode()
        clientSocket.close()
        return self.menssages
    
cli  = User()

# _______ SOME EXAMPLE'S IN EXECUTION ___________

# print(cli.serverConectAndSend("candidates/post id=10,name=ricardo,voteCounted=2"))
# print(cli.serverConectAndSend("candidates/putById 10,voteCounted,12"))
# print(cli.serverConectAndSend("candidates/getById 10"))
# print(cli.serverConectAndSend("candidates/delete 3"))
print(cli.serverConectAndSend("candidates/get"))

# print("\n")
# print(cli.serverConectAndSend("voters/post id=3,name=Roberto,voted=False"))
print(cli.serverConectAndSend("voters/get"))
# print(cli.serverConectAndSend("voters/putById 1,name,verify"))



# _______ THE REQUEST METHODS POSSIBLE ______

# sentence = "voters/get"
# sentence = "voters/getById id"
# sentence = "voters/post id=3,name=roberto,voteCounted=3"
# sentence = "voters/putById id,atribute,value"
# sentence = "voters/delete id"
# sentence = "voters/deleteAll"

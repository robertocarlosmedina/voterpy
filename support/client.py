from socket import *

class Client:
    serverName = 'localhost'
    serverPort = 12000
    message = None
    original_path = "./server/dataBase/"
    path = ""
    # comands = {"get":2,"getById":2,"post":1, "put":2, "delete":4}
    
    def serverConectAndSend(self, request):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.serverName, self.serverPort))
        clientSocket.send(request.encode())
        modifiedSentence = clientSocket.recv(1024)
        self.message = modifiedSentence.decode()
        clientSocket.close()
        return self.message
    
cli  = Client()

# _______ SOME EXAMPLE'S IN EXECUTION ___________

## working on the candidates json
print("- candidates.json")
# print(cli.serverConectAndSend("candidates/post name=sonia,voteCounted=0"))
# print(cli.serverConectAndSend("candidates/putById 10,voteCounted,12"))
# print(cli.serverConectAndSend("candidates/getById 10"))
# print(cli.serverConectAndSend("candidates/delete 3"))
print(cli.serverConectAndSend("candidates/get"))

## working on the voters json
print("\n")
print("- voter.json")
# print(cli.serverConectAndSend("voters/post name=ricardo,voted=False"))
# print(cli.serverConectAndSend("voters/putById 1,name,verify"))
# print(cli.serverConectAndSend("voters/getById 10"))
# print(cli.serverConectAndSend("voters/delete 3"))
print(cli.serverConectAndSend("voters/get"))




# _______ THE REQUEST METHODS POSSIBLE ______

# request = "jsonFileName/get"
# request = "jsonFileName/getById id"
# request = "jsonFileName/post atribute1=value,atribute2=value,atribute3=value"
# request = "jsonFileName/putById id,atribute,value"
# request = "jsonFileName/delete id"
# request = "jsonFileName/deleteAll"

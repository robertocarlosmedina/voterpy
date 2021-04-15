from socket import *
from sys import base_exec_prefix, set_asyncgen_hooks
from dataBase import JsonFiles

## ____ ON BUILDING ______

class Server:
    serverName = "localhost"
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) ## I the port is in use this instruction will and
                                                         ## the process in the port to make it able to be use
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(1)

    path="candidates"
    dataBase = JsonFiles("./server/dataBase/"+path+".json")
    print('The server id on state Run.')
    requestTypes = {"get 0":dataBase.get, "getById 1": dataBase.getById,"post 1":dataBase.post # dict that store all the requeste method whit their argument number
                    ,"putById 3":dataBase.putById,"delete 1":dataBase.delete, "deleteAll 0":dataBase.deleteAll} # and also store the function related to them

    def runServer(self):
        # running the server and wait for connections
        while True:
            connectionSocket, addr = self.serverSocket.accept()
            # to take note that the value 1024 is to limite the memori size off content transfered, so it can be incrise to more data trafic
            sentence = connectionSocket.recv(4096).decode()
            connectionSocket.send(str(self.readingRequest(sentence)).encode())
            connectionSocket.close()
        
    # Method to check the request methods and the atributes / values send    
    def readingRequest(self, sentence):
        # imagine the sentence sent is: "candidates/post id=10,name=ricardo,voteCounted=2"
        # the steps will show what happen to variable according to this example
        sentence = sentence.split(" ") # ["candidates/post","id=10,name=ricardo,voteCounted=2"]
        dataBaseName, requestType = sentence[0].split("/")[0], sentence[0].split("/")[1] # candidates, post
        if dataBaseName not in self.path: # verify if the json file is the same, and if not change it
            self.path = dataBaseName
            self.dataBase.changeJsonPath("./server/dataBase/"+self.path+".json")

        for key, value in self.requestTypes.items(): # running the key and the value in the dict off all the request method
            if key.split(" ")[0] == requestType: # verify if the method is equal to post
                # the following conditions is to verify how many arguments the method had, to send them to the method related to the request method
                if key.split(" ")[1] == '0':
                    return value()
                elif key.split(" ")[1] == '1':
                    return value(sentence[1])
                elif key.split(" ")[1] == '2':
                    atributes = sentence[1].split(",")
                    return value(atributes[0],atributes[1])
                elif key.split(" ")[1] == '3':
                    atributes = sentence[1].split(",")
                    return value(atributes[0],atributes[1],atributes[2])

# Running the server
server = Server()
server.runServer()

from socket import *
import json
import re

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
    


# _______ SOME EXAMPLE'S IN EXECUTION ___________

## working on the candidates json
print("- candidates.json")
# print(cli.serverConectAndSend("candidates/post name=sonia,voteCounted=0"))
# print(cli.serverConectAndSend("candidates/putById 10,voteCounted,12"))
# print(cli.serverConectAndSend("candidates/getById 10"))
# print(cli.serverConectAndSend("candidates/delete 3"))
# [print(data) for data in cli.serverConectAndSend("candidates/get")]

## working on the voters json
print("\n")
print("- voter.json")
# print(cli.serverConectAndSend("voters/post name=ricardo,voted=False,age=18"))
# print(cli.serverConectAndSend("voters/putById 1,name,verify"))
# print(cli.serverConectAndSend("voters/getById 10"))
# print(cli.serverConectAndSend("voters/delete 3"))

# To be finished
# dictc=json.loads(cli.serverConectAndSend("voters/get"))

def changing(string):
    newString = ''
    for i in string:
        if re.search('"', i, re.IGNORECASE):
            newString += "'"
        elif re.search("'", i, re.IGNORECASE):
            newString += '"'
        else:
            newString += i
    return newString

def checkingBoolean(string):
    true, false="True","False"
    aux = [letter for letter in string]
    if re.search(true, string, re.IGNORECASE):
        index = string.index(true)
        string = string.split()
        for letter in true:
            aux[index]=letter.lower()
            index+=1

    elif re.search(false, string, re.IGNORECASE):
        index = string.index(false)
        string = string.split()
        for letter in false:
            aux[index]=letter.lower()
            index+=1
    
    string = ''
    for letter in aux:
        string += letter
    return string
def convertingToDict(message):
    allData = []
    dt = [data for data in message[1:-1].split(",")]
    allData = []
    som = ""
    for data in dt:
        if re.search('}', data, re.IGNORECASE):
            som +=data
            som = checkingBoolean(som)
            allData.append(json.loads(changing(som)))
            som = ""
        else:
            som += data+","
    
    return allData

cli  = Client()
allData = convertingToDict(cli.serverConectAndSend("voters/get"))
print(allData[1])





# _______ THE POSSIBLE  REQUEST METHODS ______

# request = "jsonFileName/get"
# request = "jsonFileName/getById id"
# request = "jsonFileName/post atribute1=value,atribute2=value,atribute3=value"
# request = "jsonFileName/putById id,atribute,value"
# request = "jsonFileName/delete id"
# request = "jsonFileName/deleteAll"

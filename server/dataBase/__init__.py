import json
import time
import random

# class to manipulate all the json file's
class JsonFiles:
    def __init__(self, path):
        self.data = None
        self.path = path
        self.idCandidates = 1
        self.idVoters = 1
        self.readONJson()
    
    # method post to store in the json file
    def post(self, newOne):
        newOne = newOne.split(",")
        newOne.insert(0,"id="+self.generateNewId())

        newDict = {}
        i = 0
        for atribute in newOne:
            atribute = atribute.split("=")
            newDict[atribute[0]]=self.verType(atribute[1])
            i+=1
        self.data.append(newDict)
        self.writeONJson()
        return True
    
    # Method to generate a new user id
    def generateNewId(self):
        newId = ''
        keys="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ## string of all  the letters in the alphabet, in upper and lower case.
        
        for _ in range(0,2):
            localtime = time.localtime(time.time())
            for _ in range(0,3):
                if localtime.tm_sec >= 12:
                    newId += keys[random.randint(0, self.possitiveSinalConvert(localtime.tm_sec - 12))]
                else:
                    newId += keys[random.randint(0, self.possitiveSinalConvert(localtime.tm_min-12))]
        localtime = time.localtime(time.time())
        newId += str(self.idVoters)+str(self.idCandidates)+str(localtime.tm_mday*random.randint(0, 100))+\
            str(localtime.tm_sec)+str(localtime.tm_min*random.randint(0, 1000))+str(keys[random.randint(0,40)])
        for _ in range(0,6):
            newId += str(keys[random.randint(0,47)])
        return newId
    
    # Method to verigy the sinal of the value
    def possitiveSinalConvert(self, sinal):
        if sinal < 0:
            return sinal*(-1)
        return sinal

    # Method to convert to string or to boolean according to string variable
    def verType(self, item):
        try:
            return int(item)
        except:
            pass
        
        if item == "True":
            return bool(item)
        elif item == "False":
            return not bool(item)
            
        else:
            return item

    # method similar to put, to change a item in the json file
    def putById(self, id, atribute, newValue):
        for data in self.data:
            if data["id"]==id:
                data[atribute] = newValue
                self.writeONJson()
                return True
        return False
    
    # method to delete an item in the json file
    def delete(self, id):
        i = 0
        for data in self.data:
            if data["id"] == id:
                self.data.pop(i)
                self.writeONJson()
                return True
            i+=1
        return False
    
    # method to delete all the items in the json file
    def deleteAll(self):
        self.data = []
        self.writeONJson()
        return True

    # method to get all the data in the json file
    def get(self):
        return self.data

    # method to get a specific data in the json file
    def getById(self, id):
        for data in self.data:
            if data["id"]==id:
                return data
        return None
    
    # method to read all the items in the json file
    def readONJson(self):
        self.data = []
        with open(self.path) as json_file:
            self.data = json.load(json_file)
        json_file.close()
        
        # putting the id starting in zero
        self.idCandidates = self.idVoters = 1

        # verify in what is the value of the last  id
        for _ in self.data:
            if self.path == "./server/dataBase/voters.json":
                self.idVoters += 1
            else: 
                self.idCandidates += 1

    # method to write the changes on the json file
    def writeONJson(self):
        with open(self.path,'w') as f:
            json.dump(self.data, f, indent=4)
        f.close()
        self.readONJson()

    # method to change the directory of the json file, or change the json storage
    def changeJsonPath(self, newPath):
        self.path = newPath
        self.readONJson()

## ___  Aria reserver for test's  ____
      
# cand = JsonFiles("./server/dataBase/voters.json")
# # cand.deleteAll()
# print(cand.generateNewId())
# print(cand.path)
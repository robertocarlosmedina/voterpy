import json

# class to manipulate all the json file's
class JsonFiles:
    def __init__(self, path):
        self.data = None
        self.path = path
        self.readONJson()
    
    # method post to store in the json file
    def post(self, newOne):
        newOne = newOne.split(",")
        newDict = {}
        i = 0
        for atribute in newOne:
            atribute = atribute.split("=")
            newDict[atribute[0]]=self.verType(atribute[1])
            i+=1
        self.data.append(newDict)
        self.writeONJson()
        return True
    
    # Method to convert to string or to boolean according to string variable
    def verType(self, item):
        try:
            return int(item)
        except:
            pass
        
        if item == "True" or item == "False":
            return bool(item)
        else:
            return item

    # method similar to put, to change a item in the json file
    def putById(self, id, atribute, newValue):
        for data in self.data:
            if data["id"]==int(id):
                data[atribute] = newValue
                self.writeONJson()
                return True
        return False
    
    # method to delete an item in the json file
    def delete(self, id):
        i = 0
        for data in self.data:
            if data["id"] == int(id):
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
            if data["id"]==int(id):
                return data
        return None
    
    # method to read all the items in the json file
    def readONJson(self):
        with open(self.path) as json_file:
            self.data = json.load(json_file)
        json_file.close()

    # method to write the changes on the json file
    def writeONJson(self):
        with open(self.path,'w') as f:
            json.dump(self.data, f, indent=4)
        f.close()

    # method to change the directory of the json file, or change the json storage
    def changeJsonPath(self, newPath):
        self.path = newPath
        self.readONJson()
        
# cand = JsonFiles("./server/dataBase/candidates.json")
# cand.deleteAll()
# print(cand.get())
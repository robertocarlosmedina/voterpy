import json

# class to manipulate all the json file's
class JsonFiles:
    def __init__(self, path):
        self.data = None
        self.path = path
        self.readONJson()
    
    # method post to store in the json file
    def post(self, newOne):
        self.data.append(newOne)
        self.writeONJson()

    # method similar to put, to change a item in the json file
    def putById(self, id, atribute, newValue):
        self.data[id][atribute] = newValue
        self.writeONJson()
    
    # method to delete an item in the json file
    def delete(self, id):
        self.data.pop(id)
        self.writeONJson()
    
    # method to delete all the items in the json file
    def deleteAll(self):
        self.data = []
        self.writeONJson()

    # method to get all the data in the json file
    def get(self):
        return self.data

    # method to get a specific data in the json file
    def getById(self, id):
        return self.data[id]
    
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
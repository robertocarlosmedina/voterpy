import json

class Candidates:
    def __init__(self):
        self.data = None
        self.readONJson()
    
    def post(self, newOne):
        self.data.append(newOne)
        self.writeONJson()

    def putById(self, id, atribute, newValue):
        self.data[id][atribute] = newValue
        self.writeONJson()
    
    def delete(self, id):
        self.data.pop(id)
        self.writeONJson()

    def get(self):
        return self.data
    
    def readONJson(self):
        with open("./server/dataBase/candidates.json") as json_file:
            self.data = json.load(json_file)
        json_file.close()

    def writeONJson(self, filename="./server/dataBase/candidates.json"):
        with open(filename,'w') as f:
            json.dump(self.data, f, indent=4)
        f.close()

# test
# cand = Candidates()
# print(cand.get())

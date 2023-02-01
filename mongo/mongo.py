from pymongo import MongoClient
class Mongo:
    def __init__(self, ip):
        self.client = MongoClient(ip)
        
    def listdbs(self):
        print(self.client.list_database_names())

    def listCollections(self):
        
        self.db = self.client.prueba
        print(self.db.list_collection_names())

    def WriteDocument(self,data):# data must be adict
        self.db = self.client.WorldEye
        self.transactions = self.db.prueba
        self.response = self.transactions.insert_one(data)
        print(self.response.inserted_id)



    def WriteMany(self,DataArray):
        self.db = self.client.WorldEye
        self.transactions = self.db.prueba
        self.response = self.transactions.insert_many(DataArray)
        print(self.response.inserted_ids)





# client = mongo('170.187.188.121')
# client.WriteDocument(dict)

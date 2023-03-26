from pymongo import MongoClient


class Mongo:
    def __init__(self, ip):

        self.client = MongoClient(ip)

    # lista todas las bases de datos

    def listdbs(self):
        print(self.client.list_database_names())

    # lista todas las coleccioines de una base (es case sensitive)
    def listCollections(self, DBname: str):
        collection = self.client[DBname]
        print(collection.list_collection_names())

    # Escribe en una colección, los datos deben de ser un diccionario
    def WriteDocument(self,db:str ,collection:str, data):  # data must be adict
        self.db = self.client[db]
        self.transactions = self.db[collection]
        self.response = self.transactions.insert_one(data)
        print(self.response.inserted_id)

    def WriteMany(self,db:str ,collection:str, dataArray):
        self.db = self.client[db]
        self.transactions = self.db[collection]
        self.response = self.transactions.insert_many(dataArray)
        print(self.response.inserted_ids)

from pymongo import MongoClient
from itertools import islice
import json
import time

client = MongoClient('localhost', 27017)
db = client.admin    
collection = db.Main

def get10():
    dict = {}
    dataArray = []
    for data in islice(collection.find({},{'_id': False}),10) :
        dataArray.append(data)
    
    return dataArray


def getPort(port)->dict:

    query = { "ports.port": port }
    exclude = {"_id" : False}
    results = collection.find(query,exclude, limit=25)
    
    response = []

    for x in results:
        response.append(x)
    return json.loads(json.dumps(response))

    
def query(query:str):
    query={
        'tokens': 'http'
    }
    exclude = {"_id" : False}
    results = collection.find(query,exclude, limit=25)
    response = []
    for x in results:
        response.append(x)
    return json.loads(json.dumps(response))


    

import meilisearch
import json, orjson

client = meilisearch.Client('http://localhost:7700')

json_file = open('jsonParser\generated.json', 'r', encoding='utf-8')
ip = json.load(json_file)
print("json loaded")
client.index('repetidas').add_documents(ip)
 
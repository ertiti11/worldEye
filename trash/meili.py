import meilisearch
import json

client = meilisearch.Client('http://localhost:7700')

json_file = open('jsonParser\generated.json')
ip = json.load(json_file)
client.index('Generated').add_documents(ip)
 
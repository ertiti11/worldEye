import meilisearch
import json

client = meilisearch.Client('http://localhost:7700')

json_file = open('ipss.json')
ip = json.load(json_file)
client.index('maxports').add_documents(ip)
 
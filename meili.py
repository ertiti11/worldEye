import meilisearch
import json

client = meilisearch.Client('http://localhost:7700')

json_file = open('ips.json')
ip = json.load(json_file)
client.index('id_test2').add_documents(ip)
 
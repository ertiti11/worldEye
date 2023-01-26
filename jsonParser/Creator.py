import json
import uuid
a_file = open("jsonParser\ipss.json", "r")
json_object = json.load(a_file)

count = 0
data = {}
datas =[]




jsonn=[]

for i in range(0,len(json_object)):
    ip = json_object[i]["ip"] # = 23.45.59.219
    ports = json_object[i]["ports"] #  =80
    id = uuid.uuid4() # 1234-1234-51-2334
    try:
        services = ports[0]['service'] # http
    except KeyError:
        pass


    data['id'] = str(id)
    data['ip'] = ip
    data['ports'] = ports
    try:
        data['ports'][0]['service'] = services['name']
    except:
        pass
    
    datas.append(json.dumps(data))
# datas = json.dumps(str(datas))

# # datas = json.dumps(datas, indent=4)
# print(datas)

# jsonData = json.dumps(datas,indent=4)
# print(jsonData)


# myList = [{'a': 54}, {'b': 41, 'c':87}]
# jsonString = json.dumps(myList, indent=4)
# print(jsonString)


# import json


# data['key'] = 'value'
# json_data = json.dumps(data)
# print(json_data)




# for i in json_object:

#     dict = json_object[count]
#     dict["id"] = count
#     a_file.close()
#     # json_object = json.dumps(dict)
#     #json_object = json.dumps(dict, indent=4)ç
#     data.append(dict) 
    
#     count +=1


with open('jsonParser\ipss2.json', 'w') as outfile:
    outfile.write(str(datas))
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

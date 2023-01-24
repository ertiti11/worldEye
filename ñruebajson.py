import json
a_file = open("topcustom.json", "r")
json_object = json.load(a_file)

count = 0
data =[]
for i in json_object:

    dict = json_object[count]
    dict["id"] = count
    a_file.close()
    # json_object = json.dumps(dict)
    #json_object = json.dumps(dict, indent=4)ç
    data.append(dict) 
    
    count +=1
json_string = json.dumps(data)

with open('ipss.json', 'w') as outfile:
    outfile.write(json_string)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

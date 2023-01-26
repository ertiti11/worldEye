import orjson

class Compositor:
    def __init__(self):
        pass
        

    def masscan2Json(self, file):
        import json
        import uuid
        a_file = open(file, "r")
        json_object = json.load(a_file)

        data = {}

        datas = []

        for i in range(0,len(json_object)):
            ip = json_object[i]["ip"] # = 23.45.59.219
            ports = json_object[i]["ports"] #  = 80
            
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
                data['ports'][0]['banner'] = services['banner']
            except:
                pass
            
            datas.append(data)
            data ={}
        datas = orjson.dumps(datas, option=orjson.OPT_NAIVE_UTC)    
        
            
        with open('jsonParser\generated.json', 'wb') as f:
            f.write(datas)




compositor = Compositor()

ddd  = compositor.masscan2Json('jsonParser\ipss.json')
import orjson
from reverseIP import reverseIP
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
            # try:
            #     hostname = reverseIP(ip)
            #     data['hostname'] = hostname
            # except:
            #     pass
            
                pass
            data['id'] = str(id)
            data['ip'] = ip
            
            data['ports'] = ports
            try:
                data['ports'][0]['service'] = services['name']
                data['ports'][0]['banner'] = services['banner']
                
                data['tokens'] = self.tokenizer(services['banner'])
            except:
                pass
            
            datas.append(data)
            data ={}
            print(i)
        datas = orjson.dumps(datas, option=orjson.OPT_NAIVE_UTC | orjson.OPT_INDENT_2)
        
            
        with open('jsonParser\generated.json', 'wb') as f:
            f.write(datas)
        print("hecho")

    def tokenizer(self, string):
        test_list = [string]
        res = [sub.split() for sub in test_list]
        return res


compositor = Compositor()

compositor.masscan2Json('jsonParser\ips.json')

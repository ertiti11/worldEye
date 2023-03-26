import orjson
from datetime import datetime
import json,logging


class Compositor:
    def __init__(self):
        pass

    def masscan2Json(self, file: str):
        """Recibe como parametro una ruta a un archivo la cual
        sera un archivo sin procesar directamente desde masscan y lo convierte
        en un archivo procesado con su propia estructura de datos.
        """

        inputObject = json.load(open(file, "r"))

        outDict = {}

        outArray = []

        for i in range(0, len(inputObject)):
            ip = inputObject[i]["ip"]  # = 23.45.59.219
            date = datetime.fromtimestamp(int(inputObject[i]["timestamp"])).strftime('%d-%m-%y')
            ports = inputObject[i]["ports"]  # = 80
            try:
                services = ports[0]['service']  # http

            except KeyError:

                pass

            outDict['ip'] = ip
            outDict['date'] = date
            outDict['ports'] = ports

            try:
                outDict['ports'][0]['service'] = services['name']
                outDict['ports'][0]['banner'] = services['banner']
                outDict['tokens'] = self.tokenizer(services['banner'])
            except:
                pass

            outArray.append(outDict)
            outDict = {}

        outArray = orjson.dumps(
            outArray, option=orjson.OPT_NAIVE_UTC | orjson.OPT_INDENT_2)

        

        with open('./{}.json'.format(str(datetime.now().strftime('%d-%m-%y_%H_%M'))), 'wb') as f:
            f.write(outArray)
        return outArray
    def tokenizer(self, raw:str)-> str:
        """Recibe como parametro todas las palabras del resultado
        de masscan y los separa por espacios y hace palabras separadas
        con ellas
        """
        
        # tokenList = rawString.split()
        return raw.split()
        




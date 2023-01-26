import orjson, datetime
import numpy as np
import json
data = {
    "type": "job",
    "created_at": datetime.datetime(1970, 1, 1),
    "status": "🆗",
    "payload": np.array([[1, 2], [3, 4]]),
}
array  = []
for i in range(0,10000000):
    array.append(data)


datas = orjson.dumps(array, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
datas  = orjson.loads(datas)

print(datas)
# datas2 = json.dumps(str(array), indent=4)
# print(datas2)
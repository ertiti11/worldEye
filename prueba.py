from mongo.mongo import Mongo
from jsonParser.Compositor import Compositor
import json

# compositor = Compositor()

# compositor.masscan2Json("./RawData/aws.json")


compositor = Compositor()
data = compositor.masscan2Json('./RawData/aws.json')
compositor = Compositor()
data = compositor.masscan2Json('./RawData/aws.json')
# client = Mongo('localhost')
# data = json.loads(data)
# client.WriteMany("WorldEye", "Main", data)
from mongo.mongo import Mongo
from jsonParser.Compositor import Compositor


compositor = Compositor()

compositor.masscan2Json("./RawData/aws.json")




client = Mongo('localhost')

client.listdbs()
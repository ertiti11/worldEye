from mongo import Mongo
from Compositor import Compositor


compositor = Compositor()
data = compositor.masscan2Json('Data\generated.json')
client = Mongo('localhost')

client.WriteMany(data)
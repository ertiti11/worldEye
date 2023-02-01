from mongo import Mongo
from Compositor import Compositor


compositor = Compositor()
data = compositor.masscan2Json('mongo\generated.json')
client = Mongo('170.187.188.121')

client.WriteMany(data)
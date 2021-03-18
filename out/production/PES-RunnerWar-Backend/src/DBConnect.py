import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://lluis-vacares:Hondarincon98!@runnerwar.yuhsa.mongodb.net/RunnerWar?retryWrites=true&w=majority")

db = client['RunnerWar']
print(client.list_database_names())

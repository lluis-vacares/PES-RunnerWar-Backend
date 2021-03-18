import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://lluis-vacares:runnerwar@runnerwar.yuhsa.mongodb.net/RunnerWar?retryWrites=true&w=majority")
#print(client.get_database("RunnerWar").list_collection_names())

#print(client.list_database_names())
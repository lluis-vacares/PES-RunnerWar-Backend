import pymongo

from src import Cuenta

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/RunnerWar?retryWrites=true&w=majority")
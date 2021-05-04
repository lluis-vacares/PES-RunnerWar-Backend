import json

import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Mensaje"]


def create_message(sender, receiver, chat, date, time):
    aux = 0
    for x in col.find({"sender": sender, "receiver": receiver, "chat": chat, "date": date, "time": time}, {"_id": 0}):
        aux = x
    if aux == 0:
        doc = {
            "sender": sender,
            "receiver": receiver,
            "chat": chat,
            "date": date,
            "time": time
        }
        col.insert_one(doc)
        y = {"codi": 200}
        z = json.dumps(doc)
        z = json.loads(z)
        z.update(y)
        return z
    else:
        return {
            "sender": None,
            "receiver": None,
            "chat": None,
            "date": None,
            "time": None
        }


def get_all_messages(sender, receiver):
    a = []
    for x in col.find({"sender": sender, "receiver": receiver}, {"_id": 0}):
        a.append(x)
    for y in col.find({"sender": receiver, "receiver": sender}, {"_id": 0}):
        a.append(y)
    js = json.dumps(a)
    return js
import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Chat"]


def create_chat(email, date, participant):
    aux = 0
    n = email + "/" + participant
    for x in col.find({"_id": n}):
        aux = x
    if aux == 0:
        doc = {
            "_id": n,
            "created_at": date,
            "created_by": email,
            "participants": [email, participant]
        }
        col.insert_one(doc)
        y = {"codi": 200}
        z = json.dumps(doc)
        z = json.loads(z)
        z.update(y)
        return z
    else:
        return {
            "_id": None,
            "created_at": None,
            "created_by": None,
            "participants": None,
            "codi": 500}


def delete_chat(email, participant):
    n = email + "/" + participant
    col.delete_one({"_id": n})
    return {"codi": 200}
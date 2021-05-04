import json

import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Actividad"]


def create(name, date):
    aux = 0
    for x in col.find({"accountname": name, "date": date}):
        aux = x
    if aux == 0:
        doc = {
            "accountname": name,
            "date": date,
            "km": 0
        }
        col.insert_one(doc)
    return consult_activity(name, date)


def consult_activity(name, date):
    aux = 0
    for x in col.find({"accountname": name, "date": date}, {"_id": 0}):
        aux = x
    if aux == 0:
        return {"accountname": None, "date": None, "km": None, "codi": 500}
    else:
        y = {"codi": 200}
        z = json.dumps(aux)
        z = json.loads(z)
        z.update(y)
        return z


def update_activity(name, date, km):
    aux = 0
    for x in col.find({"accountname": name, "date": date}):
        aux = x
    if aux == 0:
        return {"accountname": None, "date": None, "km": None, "codi": 500}
    else:
        myquery = {"accountname": name, "date": date}
        newvalues = {"set": {"km": km}}
        col.update_one(myquery, newvalues)
        return {"accountname": name, "date": date, "km": km, "codi": 200}

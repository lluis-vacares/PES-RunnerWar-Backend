import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Cuenta"]


def consult_email(attribute):
    aux = 0
    for x in col.find({"_id": attribute}):
        return x
    if aux != 0:
        s1 = json.dumps(aux)
        z = json.loads(s1)
        y = {"codi": 200}
        z.update(y)
        return z
    else:
        return {"_id": None, "password": None, "accountname": None, "coins": None, "points": None, "faction": None,
                "codi": 500}


def consult_accountname(attribute):
    aux = 0
    for x in col.find({"accountname": attribute}):
        aux = x
    if aux != 0:
        z = aux
        y = {"codi": 200}
        z.update(y)
        return z
    else:
        return {"_id": None, "password": None, "accountname": None, "coins": None, "points": None, "faction": None,
                "codi": 500}


def create(email, name, password, faction):
    aux = 0
    for x in col.find({"accountname": name}, {"_id": 0, "accountname": 1}):
        aux = x
    if aux == 0:
        doc = {
            "_id": email,
            "password": password,
            "accountname": name,
            "coins": 0,
            "points": 0,
            "faction": faction
        }
        y = {"codi": 200}
        z = json.dumps(doc)
        z = json.loads(z)
        z.update(y)
        return z
    else:
        return {"_id": None,
                "password": None,
                "accountname": None,
                "coins": None,
                "points": None,
                "faction": None,
                "codi": 500}


def login(email, password):
    aux = 0
    for x in col.find({"_id": email, "password": password}):
        aux = x
    if aux == 0:
        return {"_id": None,
                "password": None,
                "accountname": None,
                "coins": None,
                "points": None,
                "faction": None,
                "codi": 500
                }
    else:
        return consult_email(email)


def edit(item, new, id):
    aux = 0
    for x in col.find({"accountname": new}, {"_id": 0, "accountname": 1}):
        aux = x
    if aux == 0:
        new = {"$set": {item: new}}
        col.update_one({"_id": id}, new)
    return consult_email(id)


def delete(attribute):
    query = {"_id": attribute}
    col.delete_one(query)
    return {"codi": 200}

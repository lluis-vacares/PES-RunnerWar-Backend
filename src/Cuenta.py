import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Cuenta"]


def consult_email(attribute):
    aux = 0
    for x in col.find({"_id": attribute}):
        aux = x
    if aux != 0:
        s1 = json.dumps(aux)
        z = json.loads(s1)
        y = {"codi": 200}
        z.update(y)
        return z
    else:
        return {"_id": None, "password": None, "accountname": None, "coins": None, "points": None, "faction": None,
                "codi": 500}


def consult_other_account(accountname):
    aux = 0
    for x in col.find({"accountname": accountname}, {"password": 0}):
        aux = x
    if aux != 0:
        s1 = json.dumps(aux)
        z = json.loads(s1)
        y = {"codi": 200}
        z.update(y)
        return z
    else:
        return {"_id": None, "accountname": None, "coins": None, "points": None, "faction": None,
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
    aux = col.count_documents({"accountname": name})
    if aux == 0:
        doc = {
            "_id": email,
            "password": password,
            "accountname": name,
            "coins": 0,
            "points": 0,
            "faction": faction
        }
        col.insert_one(doc)
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


def update(item, new, id):
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

def update_faccion(email, faccion):
    aux = 0
    for x in col.find({"_id": email }):
        aux = x
    if aux == 0:
        return { "codi": 500}
    else:
        myquery = {"_id": email}
        newvalues = {"$set": {"faction": faccion}}
        col.update_one(myquery, newvalues)
        return {"codi": 200}

def add_points(email, points):
    aux = 0
    for x in col.find({"_id": email}):
        aux = x
    if aux == 0:
        return {
                "_id": None,
                "password": None,
                "accountname": None,
                "points": None,
                "faction": None,
                "codi": 500
                }
    else:
        myquery = {"_id": email}
        newvalues = {"$inc": {"points": points}}
        col.update_one(myquery, newvalues)
        return consult_email(email)

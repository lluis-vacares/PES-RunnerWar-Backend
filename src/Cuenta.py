import datetime
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
                "last_connection": None,
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
                "last_connection": None,
                "codi": 500}


def consult_accountname(attribute):
    aux = 0
    for x in col.find({"accountname": attribute}):
        aux = x
    if aux >= 0:
        z = aux
        y = {"codi": 200}
        z.update(y)
        return z
    else:
        return {"_id": None, "password": None, "accountname": None, "coins": None, "points": None, "faction": None,
                "last_connection": None, "codi": 500}


def create(email, name, password, faction, last_connection):
    aux = col.count_documents({"accountname": name})
    aux += col.count_documents({"_id": email})
    if aux == 0:
        doc = {
            "_id": email,
            "password": password,
            "accountname": name,
            "coins": 0,
            "points": 0,
            "faction": faction,
            "last_connection": last_connection
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
                "last_connection": None,
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
                "last_connection": None,
                "codi": 500
                }
    else:
        return consult_email(email)


def update(item, new, id):
    aux = 0
    for x in col.find({"accountname": new}):
        aux = x
    if aux == 0:
        new = {"$set": {item: new}}
        col.update_one({"_id": id}, new)
        return consult_email(id)
    else:
        return {"_id": None,
                "password": None,
                "accountname": None,
                "coins": None,
                "points": None,
                "faction": None,
                "last_connection": None,
                "codi": 500}

def delete(attribute):
    query = {"_id": attribute}
    col.delete_one(query)
    db.Amigo.delete_many({"Amigo1": attribute})
    db.Amigo.delete_many({"Amigo2": attribute})
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
                "last_connection": None,
                "codi": 500
                }
    else:
        myquery = {"_id": email}
        newvalues = {"$inc": {"points": points}}
        col.update_one(myquery, newvalues)
        return consult_email(email)


def update_last_connection(email, last_connection):
    aux = 0
    for x in col.find({"_id": email }):
        aux = x
    if aux == 0:
        return { "codi": 500}
    else:
        myquery = {"_id": email}
        newvalues = {"$set": {"last_connection": last_connection}}
        col.update_one(myquery, newvalues)
    return {"codi": 200}


def daily_login(email):
    aux = 0
    for x in col.find({"_id": email}):
        aux = x
    if aux != 0:
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        if aux["last_connection"] != today:
            update_last_connection(email, today)
            add_points(email, 20)
            return {"codi": 200}
        else:
            return {"codi": 500}
    else:
        return {"codi": 500}


def get_all_users():
    a = []
    for x in col.find({}, {"password": 0}).sort("coins", -1):
        a.append(x)
    js = json.dumps(a)
    return js


def add_coins(email, coins):
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
            "last_connection": None,
            "codi": 500
        }
    else:
        myquery = {"_id": email}
        newvalues = {"$inc": {"coins": coins}}
        col.update_one(myquery, newvalues)
        return consult_email(email)
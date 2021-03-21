import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/RunnerWar?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Cuenta"]


def create(email, name, password, faction):
    if col.find({"username": name}) is None:
        doc = {
            "_id": email,
            "password": password,
            "username": name,
            "coins": "0",
            "points": "0",
            "faction": faction
        }
        col.insert_one(doc)
        return 1
    return None


def edit(item, old, new):
    query = {item: old}
    aux = {item: new}
    if col.find(aux) is None:
        new = {"$set": aux}
        col.update_one(query, new)
        return 1
    return None


def delete(attribute):
    query = {"_id": attribute}
    col.delete_one(query)


def consult(item, attribute):
    aux = col.find({item: attribute})
    for x in aux:
        return x
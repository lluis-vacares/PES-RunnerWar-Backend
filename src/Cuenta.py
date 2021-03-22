import pymongo

client = pymongo.MongoClient("mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Cuenta"]


def consult(attribute):
    return col.find({"_id": attribute})


def create(email, name, password, faction):
    aux = 0
    for x in col.find({"username": name}, { "_id": 0, "username": 1}):
        aux = x
    if aux == 0:
        doc = {
            "_id": email,
            "password": password,
            "username": name,
            "coins": "0",
            "points": "0",
            "faction": faction
        }
        col.insert_one(doc)
        return consult(email)
    return None


def edit(item, old, new, id):
    if col.find({item: new}) is None:
        new = {"$set": {item: new}}
        col.update_one({item: old}, {item: new})
        return consult(id)
    return None


def delete(attribute):
    query = {"_id": attribute}
    col.delete_one(query)
    return 200
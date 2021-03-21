import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/RunnerWar?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Faccion"]


def create(name, color, description):
    doc = {
        "_id": name,
        "color": color,
        "description": description,
    }
    col.insert_one(doc)
    return 1


def edit(item, old, new):
    query = {item: old}
    aux = {item: new}
    new = {"$set": aux}
    col.update_one(query, new)
    return 1


def delete(attribute):
    query = {"_id": attribute}
    col.delete_one(query)
    return 1


def consult(item, attribute):
    aux = col.find({item: attribute})
    for x in aux:
        return x
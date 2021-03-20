import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/RunnerWar?retryWrites=true&w=majority")

db = client["RunnerWar"]


def create_account(email, password, name, faction):
    col = db["Cuenta"]
    doc = {
        "_id": email,
        "email": "NULL",
        "password": password,
        "username": name,
        "coins": "0",
        "points": "0",
        "faction": faction
    }
    return col.insert_one(doc)


def edit_account(old, new):
    col = db["Cuenta"]
    query = {
        "username": old
    }
    new = {
        "$set":
            {
                "username": new
            }
    }
    col.update_one(query, new)


def delete_account(email):
    col = db["Cuenta"]
    query = {
        "email": email
    }
    return col.delete_one(query)
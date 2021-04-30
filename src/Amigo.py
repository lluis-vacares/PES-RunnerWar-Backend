import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Amigo"]


def search(email1, email2):
    aux = col.count_documents({"Amigo1": email1, "Amigo2": email2})
    aux += col.count_documents({"Amigo1": email2, "Amigo2": email1})
    if aux > 0:
        return {"codi": 200}
    else:
        return {"codi": 500}


def aggregate(email1, email2):
    doc = {
        "Amigo1": email1,
        "Amigo2": email2,
    }
    col.insert_one(doc)
    return {"codi": 200}


def delete(email1, email2):
    col.find_one_and_delete({"Amigo1": email1, "Amigo2": email2})
    col.find_one_and_delete({"Amigo1": email2, "Amigo2": email1})
    return {"codi": 200}
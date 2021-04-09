import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Actividad"]


def create(name, date):
    aux = 0
    for x in col.find({"accountname": name}, {"date": date}):
        aux = x
    if aux == 0:
        doc = {
            "accountname": name,
            "date": date,
            "km": 0
        }
        col.insert_one(doc)
        return consult_activity(name, date)
    return {"codi": 500}


def consult_activity(name, date):
    aux = 0
    for x in col.find({"accountname": name, "date": date}):
        aux = x
    if aux == 0:
        return {"codi": 500}
    elif aux != 0:
        return aux
    else:
        return {"codi": 500}


def update_activity(name, date, km):
    aux = 0
    for x in col.find({"accountname": name, "date": date}):
        aux = x
    if aux == 0:
        return {"codi": 500}
    else:
        myquery = {"accountname": name, "date": date}
        newvalues = {"$inc": {"km": km}}
        col.update_one(myquery, newvalues)
        return {"codi": 200}

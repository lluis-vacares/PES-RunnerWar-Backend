import pymongo
import json


client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Amigo"]


def search(accountname1, accountname2):
    aux = col.count_documents({"Amigo1": accountname1, "Amigo2": accountname2})
    aux += col.count_documents({"Amigo1": accountname2, "Amigo2": accountname1})
    if aux > 0:
        return {"codi": 200}
    else:
        return {"codi": 500}


def aggregate(accountname1, accountname2):
    doc = {
        "Amigo1": accountname1,
        "Amigo2": accountname2,
    }
    col.insert_one(doc)
    return {"codi": 200}


def delete(accountname1, accountname2):
    col.find_one_and_delete({"Amigo1": accountname1, "Amigo2": accountname2})
    col.find_one_and_delete({"Amigo1": accountname2, "Amigo2": accountname1})
    return {"codi": 200}


def get_friends(accountname):
    #get the number of friends
    numfriends = col.count_documents({"Amigo1": accountname})
    numfriends += col.count_documents({"Amigo2": accountname})

    #get every friend
    accountnames = []
    for person in col.find({"Amigo1": accountname}):
        accountnames.append(person['Amigo2'])
    for person in col.find({"Amigo2": accountname}):
        accountnames.append(person['Amigo1'])

    #get account information
    friends = []
    friends.append({"numfriends": numfriends})
    for name in accountnames:
        for x in db.Cuenta.find({"accountname": name}, {"_id": 0, "password": 0}):
            friends.append(x)

    return json.dumps(friends)
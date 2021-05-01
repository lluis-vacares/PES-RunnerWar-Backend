import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Lugar_Interes"]


def create_lugar_interes(nombre, latitud, longitud, descripcion):
    aux = 0
    for x in col.find({"_id": nombre, "latitud": latitud, "longitud": longitud}, {"_id": 1, "accountname": 1}):
        aux = x
    if aux == 0:
        doc = {
            "_id": nombre,
            "latitud": latitud,
            "longitud": longitud,
            "descripcion": descripcion
        }
        col.insert_one(doc)
        y = {"codi": 200}
        z = json.dumps(doc)
        z = json.loads(z)
        z.update(y)
        return z
    else:
        return {
            "_id": None,
            "latitud": None,
            "longitud": None,
            "descripcion": None,
            "codi": 500}


def delete_lugar_interes(nombre):
    col.delete_one({"_id": nombre})
    return {"codi": 200}


def consult_lugar_interes(nombre):
    aux = 0
    for x in col.find({"_id": nombre}):
        aux = x
    if aux != 0:
        s1 = json.dumps(aux)
        z = json.loads(s1)
        y = {"codi": 200}
        z.update(y)
        return z
    else:
        return {"_id": None, "latitud": None, "longitud": None, "descripcion": None,
                "codi": 500}


def get_all_lugar_interes():
    a = []
    for x in col.find():
        a.append(x)
    js = json.dumps(a)
    return js

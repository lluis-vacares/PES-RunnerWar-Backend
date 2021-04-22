import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Lugar_Interes"]


def create_lugar_interes(latitud, longitud, puntuacion):
    aux = 0
    for x in col.find({"latitud": latitud, "longitud": longitud}, {"_id": 0, "accountname": 1}):
        aux = x
    if aux == 0:
        doc = {
            "latitud": latitud,
            "longitud": longitud,
            "puntuacion": puntuacion
        }
        col.insert_one(doc)
        y = {"codi": 200}
        z = json.dumps(doc)
        z = json.loads(z)
        z.update(y)
        return z
    else:
        return {
            "latitud": None,
            "longitud": None,
            "puntuacion": None,
            "codi": 500}


def delete_lugar_interes(latitud, longitud):
    col.delete_one({"latitud": latitud, "longitud": longitud})
    return {"codi": 200}


def consult_lugar_interes(latitud, longitud):
    aux = 0
    for x in col.find({"latitud": latitud, "longitud": longitud}, {"_id": 0, "latitud": 1, "longitud": 1,
                                                                   "puntuacion": 1}):
        aux = x
    if aux != 0:
        s1 = json.dumps(aux)
        z = json.loads(s1)
        y = {"codi": 200}
        z.update(y)
        return z
    else:
        return {"latitud": None, "longitud": None, "puntuacion": None,
                "codi": 500}



import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Zona_Confrontacion"]


def create_zona_confrontacion(nombre, latitud, longitud, puntuacion, descripcion):
    aux = 0
    for x in col.find({"_id": nombre}):
        aux = x
    if aux == 0:
        doc = {
            "_id": nombre,
            "latitud": latitud,
            "longitud": longitud,
            "puntuacion": puntuacion,
            "descripcion": descripcion,
            "dominant_team": None,
            "red_occupation": 0,
            "blue_occupation": 0,
            "yellow_occupation": 0,
            "green_occupation": 0
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
            "puntuacion": None,
            "descripcion": None,
            "dominant_team": None,
            "red_occupation": None,
            "blue_occupation": None,
            "yellow_occupation": None,
            "green_occupation": None,
            "codi": 500}


def delete_zona_confrontacion(nombre):
    col.delete_one({"nombre": nombre})
    return {"codi": 200}


def consult_zona_confrontacion(nombre):
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
        return {
            "_id": None,
            "latitud": None,
            "longitud": None,
            "puntuacion": None,
            "descripcion": None,
            "dominant_team": None,
            "red_occupation": None,
            "blue_occupation": None,
            "yellow_occupation": None,
            "green_occupation": None,
            "codi": 500}


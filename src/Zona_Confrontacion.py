import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Zona_Confrontacion"]


def create_zona_confrontacion(nombre, punto1, punto2, punto3, punto4, puntuacion, descripcion):
    aux = 0
    for x in col.find({"_id": nombre}):
        aux = x
    if aux == 0:
        doc = {
            "_id": nombre,
            "punto1": punto1,
            "punto2": punto2,
            "punto3": punto3,
            "punto4": punto4,
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
            "punto1": None,
            "punto2": None,
            "punto3": None,
            "punto4": None,
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
            "punto1": None,
            "punto2": None,
            "punto3": None,
            "punto4": None,
            "puntuacion": None,
            "descripcion": None,
            "dominant_team": None,
            "red_occupation": None,
            "blue_occupation": None,
            "yellow_occupation": None,
            "green_occupation": None,
            "codi": 500}


def get_all_zona_confrontacion():
    a = []
    for x in col.find():
        a.append(x)
    js = json.dumps(a)
    return js


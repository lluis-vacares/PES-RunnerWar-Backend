import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://runnerwar:runnerwar@runnerwar.yuhsa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["RunnerWar"]
col = db["Zona_Confrontacion"]
us_col = db["Cuenta"]

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


def donate_points(email, points, zc_name):
    user = us_col.find_one({"_id": email})
    zc = col.find_one({"_id": zc_name})

    if user["points"] < points:
        return {"codi": 500}
    else:
        myquery = {"_id": email}
        newvalues = {"$inc": {"points": -points}}
        us_col.update_one(myquery, newvalues)
        if user["faction"] == "red":
            myquery = {"_id": zc_name}
            newvalues = {"$inc": {"red_occupation": points}}
            col.update_one(myquery, newvalues)
        elif user["faction"] == "blue":
            myquery = {"_id": zc_name}
            newvalues = {"$inc": {"blue_occupation": points}}
            col.update_one(myquery, newvalues)
        elif user["faction"] == "yellow":
            myquery = {"_id": zc_name}
            newvalues = {"$inc": {"yellow_occupation": points}}
            col.update_one(myquery, newvalues)
        elif user["faction"] == "green":
            myquery = {"_id": zc_name}
            newvalues = {"$inc": {"green_occupation": points}}
            col.update_one(myquery, newvalues)
        update_winner(zc_name)
        return {"codi": 200}


def update_winner(zc_name):
    zc = col.find_one({"_id": zc_name})
    red = zc["red_occupation"]
    blue = zc["blue_occupation"]
    green = zc["green_occupation"]
    yellow = zc["yellow_occupation"]

    if red > blue and red > green and red > yellow:
        myquery = {"_id": zc_name}
        newvalues = {"$set": {"dominant_team": "red"}}
        col.update_one(myquery, newvalues)
    elif blue > red and blue > green and blue > yellow:
        myquery = {"_id": zc_name}
        newvalues = {"$set": {"dominant_team": "blue"}}
        col.update_one(myquery, newvalues)
    elif green > red and green > blue and green > yellow:
        myquery = {"_id": zc_name}
        newvalues = {"$set": {"dominant_team": "green"}}
        col.update_one(myquery, newvalues)
    elif yellow > red and yellow > green and yellow > blue:
        myquery = {"_id": zc_name}
        newvalues = {"$set": {"dominant_team": "yellow"}}
        col.update_one(myquery, newvalues)
    else:
        myquery = {"_id": zc_name}
        newvalues = {"$set": {"dominant_team": None}}
        col.update_one(myquery, newvalues)
    return {"codi": 200}
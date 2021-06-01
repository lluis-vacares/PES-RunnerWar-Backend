from flask import Flask, request
from src import Cuenta, Amigo
from src import Actividad
from src import Lugar_interes
from src import Zona_Confrontacion
from src import Chat

import datetime

app = Flask(__name__)


@app.route('/create', methods=['POST'])
def create_account():
    email = request.json["email"]
    accountname = request.json["accountname"]
    password = request.json["password"]
    faction = request.json["faction"]
    last_connection = datetime.datetime.now().strftime("%x")

    return Cuenta.create(email, accountname, password, faction, str(last_connection))


@app.route('/update_accountname', methods=['PUT'])
def update_accountname():
    email = request.json["email"]
    accountname = request.json["accountname"]
    return Cuenta.update("accountname", accountname, email)


@app.route('/delete', methods=['POST'])
def delete_account():
    email = request.json["email"]
    return Cuenta.delete(email)


@app.route('/login', methods=['POST'])
def log_in():
    email = request.json["email"]
    password = request.json["password"]
    return Cuenta.login(email, password)


@app.route('/consult/email', methods=['GET'])
def consult_email():
    email = request.args('email')
    return Cuenta.consult_email(email)


@app.route('/consult/accountname', methods=['POST'])
def consult_accountname():
    accountname = request.args('accountname')
    return Cuenta.consult_accountname(accountname)


@app.route('/consult/other/account', methods=['POST'])
def consult_other_account():
    accountname = request.json["accountname"]
    return Cuenta.consult_other_account(accountname)


@app.route('/update/cuenta/faction', methods=['POST'])
def update_faction():
    email = request.json["email"]
    faction = request.json["faction"]
    return Cuenta.update_faccion(email, faction)


@app.route('/points/add', methods=['PUT'])
def add_points():
    email = request.json["email"]
    points = request.json["points"]
    return Cuenta.add_points(email, points)


@app.route('/coins/add', methods=['PUT'])
def add_coins():
    email = request.json["email"]
    coins = request.json["coins"]
    return Cuenta.add_coins(email, coins)


@app.route('/users', methods=['GET'])
def get_all_users():
    return Cuenta.get_all_users()


@app.route('/cuenta/last_connection/update', methods=['PUT'])
def update_last_connection():
    email = request.json["email"]
    last_connection = datetime.datetime.now()
    x = last_connection.strftime("%d/%m/%Y")
    return Cuenta.update_last_connection(email, x)


@app.route('/daily_login', methods=['POST'])
def daily_login():
    email = request.json["email"]
    return Cuenta.daily_login(email)


@app.route('/create/activity', methods=['POST'])
def create_activity():
    accountname = request.json["accountname"]
    date = request.json["date"]
    return Actividad.create(accountname, date)


@app.route('/update/activity', methods=['PUT'])
def update_activity():
    accountname = request.json["accountname"]
    date = request.json["date"]
    km = request.json["km"]
    return Actividad.update_activity(accountname, date, km)


@app.route('/consult/activity', methods=['GET'])
def consult_activity():
    accountname = request.args.get('accountname')
    date = request.args.get('date')
    return Actividad.consult_activity(accountname, date)


@app.route('/create/lugar_interes', methods=['POST'])
def create_lugar_interes():
    nombre = request.json["nombre"]
    latitud = request.json["latitud"]
    longitud = request.json["longitud"]
    descripcion = request.json["descripcion"]
    return Lugar_interes.create_lugar_interes(nombre, latitud, longitud, descripcion)


@app.route('/delete/lugar_interes', methods=['POST'])
def delete_lugar_interes():
    nombre = request.json["nombre"]
    return Lugar_interes.delete_lugar_interes(nombre)


@app.route('/consult/lugar_interes', methods=['GET'])
def consult_lugar_interes():
    nombre = request.args('nombre')
    return Lugar_interes.consult_lugar_interes(nombre)


@app.route('/lugar_interes', methods=['GET'])
def get_all_lugar_interes():
    return Lugar_interes.get_all_lugar_interes()


@app.route('/create/zona_confrontacion', methods=['POST'])
def create_zona_confrontacion():
    nombre = request.json["nombre"]
    punto1 = request.json["punto1"]
    punto2 = request.json["punto2"]
    punto3 = request.json["punto3"]
    punto4 = request.json["punto4"]
    puntuacion = request.json["puntuacion"]
    descripcion = request.json["descripcion"]
    return Zona_Confrontacion.create_zona_confrontacion(nombre, punto1, punto2, punto3, punto4, puntuacion, descripcion)


@app.route('/delete/zona_confrontacion', methods=['POST'])
def delete_zona_confrontacion():
    nombre = request.json["nombre"]
    return Zona_Confrontacion.delete_zona_confrontacion(nombre)


@app.route('/consult/zona_confrontacion', methods=['GET'])
def consult_zona_confrontacion():
    nombre = request.args['nombre']
    return Zona_Confrontacion.consult_zona_confrontacion(nombre)


@app.route('/zona_confrontacion', methods=['GET'])
def get_all_zona_confrontacion():
    return Zona_Confrontacion.get_all_zona_confrontacion()


@app.route('/donate', methods=['PUT'])
def donate_points():
    email = request.json["email"]
    points = request.json["points"]
    zc_name = request.json["zc_name"]
    return Zona_Confrontacion.donate_points(email, points, zc_name)


@app.route('/leaderboard/factions', methods=['GET'])
def faction_leaderboard():
    return Zona_Confrontacion.get_all_faction_points()


# Connexion Amigo
@app.route('/add_friend', methods=['POST'])
def add_friend():
    email1 = request.json["email1"]
    email2 = request.json["email2"]
    return Amigo.aggregate(email1, email2)


@app.route('/search_friend', methods=['POST'])
def search_friendship():
    email1 = request.json['email1']
    email2 = request.json['email2']
    return Amigo.search(email1, email2)


@app.route('/delete_friend', methods=['POST'])
def delete_friend():
    email1 = request.json["email1"]
    email2 = request.json["email2"]
    return Amigo.delete(email1, email2)


@app.route('/friends', methods=['POST'])
def get_friends():
    email = request.json["email"]
    return Amigo.get_friends(email)


@app.route('/chat/create', methods=['POST'])
def create_chat():
    email = request.json["email"]
    date = request.json["date"]
    participant = request.json["participant"]
    return Chat.create_chat(email, date, participant)


@app.route('/chat/delete', methods=['POST'])
def delete_chat():
    email = request.json["email"]
    participant = request.json["participant"]
    return Chat.delete_chat(email, participant)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

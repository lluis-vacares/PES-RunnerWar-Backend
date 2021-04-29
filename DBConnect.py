from flask import Flask, request
from src import Cuenta
from src import Actividad
from src import Lugar_interes
from src import Zona_Confrontacion

app = Flask(__name__)


@app.route('/create', methods=['POST'])
def create_account():
    email = request.json["email"]
    accountname = request.json["accountname"]
    password = request.json["password"]
    faction = request.json["faction"]
    return Cuenta.create(email, accountname, password, faction)


@app.route('/update_accountname', methods=['PUT'])
def update_accountname():
    email = request.json["email"]
    accountname = request.json["accountname"]
    return Cuenta.edit("accountname", accountname, email)


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
    email = request.json["email"]
    return Cuenta.consult_email(email)


@app.route('/consult/accountname', methods=['GET'])
def consult_accountname():
    accountname = request.json["accountname"]
    return Cuenta.consult_accountname(accountname)


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
    accountname = request.json["accountname"]
    date = request.json["date"]
    return Actividad.consult_activity(accountname, date)


@app.route('/create/lugar_interes', methods=['POST'])
def create_lugar_interes():
    latitud = request.json["latitud"]
    longitud = request.json["longitud"]
    puntuacion = request.json["puntuacion"]
    return Lugar_interes.create_lugar_interes(latitud, longitud, puntuacion)


@app.route('/delete/lugar_interes', methods=['POST'])
def delete_lugar_interes():
    latitud = request.json["latitud"]
    longitud = request.json["longitud"]
    return Lugar_interes.delete_lugar_interes(latitud, longitud)


@app.route('/consult/lugar_interes', methods=['GET'])
def consult_lugar_interes():
    latitud = request.json["latitud"]
    longitud = request.json["longitud"]
    return Lugar_interes.consult_lugar_interes(latitud, longitud)


@app.route('/create/zona_confrontacion', methods=['POST'])
def create_zona_confrontacion():
    latitud = request.json["latitud"]
    longitud = request.json["longitud"]
    puntuacion = request.json["puntuacion"]
    equipo_dominante = request.json["equipo_dominante"]
    return Zona_Confrontacion.create_zona_confrontacion(latitud, longitud, puntuacion, equipo_dominante)


@app.route('/delete/zona_confrontacion', methods=['POST'])
def delete_zona_confrontacion():
    latitud = request.json["latitud"]
    longitud = request.json["longitud"]
    return Zona_Confrontacion.delete_zona_confrontacion(latitud, longitud)


@app.route('/consult/zona_confrontacion', methods=['GET'])
def consult_zona_confrontacion():
    latitud = request.json["latitud"]
    longitud = request.json["longitud"]
    return Zona_Confrontacion.consult_zona_confrontacion(latitud, longitud)


@app.route('/update/cuenta/faction', methods=['POST'])
def update_faction():
    accountname = request.json["accountname"]
    faction = request.json["faction"]
    return Cuenta.update_faccion(accountname, faction)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

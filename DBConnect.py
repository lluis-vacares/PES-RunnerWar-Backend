from flask import Flask, request
from src import Cuenta, Amigo
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
    email = request.json["email"]
    return Cuenta.consult_email(email)


@app.route('/consult/accountname', methods=['POST'])
def consult_accountname():
    accountname = request.json["accountname"]
    return Cuenta.consult_accountname(accountname)


@app.route('/consult/other/account', methods=['POST'])
def consult_other_account():
    accountname = request.json["accountname"]
    return Cuenta.consult_other_account(accountname)


@app.route('/update/cuenta/faction', methods=['POST'])
def update_faction():
    accountname = request.json["accountname"]
    faction = request.json["faction"]
    return Cuenta.update_faccion(accountname, faction)


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


@app.route('/consult/activity', methods=['POST'])
def consult_activity():
    accountname = request.json["accountname"]
    date = request.json["date"]
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


@app.route('/consult/lugar_interes', methods=['POST'])
def consult_lugar_interes():
    nombre = request.json["nombre"]
    return Lugar_interes.consult_lugar_interes(nombre)


@app.route('/lugar_interes', methods=['GET'])
def get_all_lugar_interes():
    return Lugar_interes.get_all_lugar_interes()


@app.route('/prova', methods=['GET'])
def prueba():
    return Lugar_interes.prueba()


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


@app.route('/consult/zona_confrontacion', methods=['POST'])
def consult_zona_confrontacion():
    latitud = request.json["latitud"]
    longitud = request.json["longitud"]
    return Zona_Confrontacion.consult_zona_confrontacion(latitud, longitud)


# Connexion Amigo
@app.route('/friend/add', methods=['POST'])
def add_friend():
    email1 = request.json["email1"]
    email2 = request.json["email2"]
    return Amigo.aggregate(email1, email2)


@app.route('/friend/search', methods=['POST'])
def search_friendship():
    email1 = request.json["email1"]
    email2 = request.json["email2"]
    return Amigo.search(email1, email2)


@app.route('/friend/delete', methods=['POST'])
def delete_friend():
    email1 = request.json["email1"]
    email2 = request.json["email2"]
    return Amigo.delete(email1, email2)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

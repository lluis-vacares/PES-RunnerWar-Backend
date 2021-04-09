from flask import Flask, request
from src import Cuenta
from src import Actividad

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


@app.route('/login', methods=['GET'])
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


@app.route('/create_activity', methods=['POST'])
def create_activity():
    accountname = request.json["accountname"]
    date = request.json["date"]
    return Actividad.create(accountname, date)


@app.route('/update_activity', methods=['PUT'])
def update_activity():
    accountname = request.json["accountname"]
    date = request.json["date"]
    km = request.json["km"]
    return Actividad.update_activity(accountname, date, km)


@app.route('/consult/activity', methods=['GET'])
def consult_activity():
    accountname = request.json["accountname"]
    date = request.json["date"]
    return Actividad.consult_activity(accountname,date)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

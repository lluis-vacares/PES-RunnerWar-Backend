from flask import Flask, request
from src import Cuenta

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
    for x in Cuenta.edit("accountname", accountname, email):
        return x


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
    return Cuenta.consult("email", email)


@app.route('/consult/accountname', methods=['GET'])
def consult_accountname():
    accountname = request.json["accountname"]
    return Cuenta.consult("accountname", accountname)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

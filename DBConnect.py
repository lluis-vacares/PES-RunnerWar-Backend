from flask import Flask, redirect, url_for, request
from src import Cuenta

app = Flask(__name__)


@app.route('/create', methods=['POST'])
def Create_account():
    email = request.json["email"]
    accountname = request.json["accountname"]
    password = request.json["password"]
    faction = request.json["faction"]
    for x in Cuenta.create(email, accountname, password, faction):
        return x


@app.route('/update_accountname', methods=['PUT'])
def Update_accountname():
    email = request.json["email"]
    accountname = request.json["accountname"]
    for x in Cuenta.edit("accountname", accountname, email):
        return x


@app.route('/delete', methods=['POST'])
def Delete_account():
    email = request.json["email"]
    return Cuenta.delete(email)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
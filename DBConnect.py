from flask import Flask, redirect, url_for, request

from src import Cuenta

app = Flask(__name__)


@app.route('/create',methods = ['POST'])
def Create_account():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    faction = request.form['faction']
    for x in Cuenta.create(email, username, password, faction):
        return x

if __name__ == '__main__':
    app.run(debug = True)
import pyotp
import sqlite3
import hashlib
import uuid
from flask import Flask, request

app = Flask(__name__)
dbname = 'ET'
@app.route('/')
def index():
    return 'Examen Transversal'

@app.route('/signup/v1', methods=['GET', 'POST'])
def signupv1():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            HASH       TEXT    NOT NULL);''')
    conn.commit()
    try:
        hash_value = hashlib.sha256(request.form["password"].encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) "
                  "VALUES ('{0}','{1}')".format(request.form['username'], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return 'El usuario ya esta registrado'
    print('username: ', request.form['username'], 'password: ', request.form['password'], 'hash: ', hash_value)
    return 'Registro exitoso'

def verify_hash(username, password):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    if not records:
        return False
    return records[0] == hashlib.sha256(password.encode()).hexdigest()

@app.route('/login/v1', methods=['GET','POST'])
def login_v1():
    error = None
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            error = 'Login exitoso'
        else:
            error = 'Usuario/contraseña invalidos'
    else:
        error = 'Metodo invalido'
    return error

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9500, ssl_context='adhoc')
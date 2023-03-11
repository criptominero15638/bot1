# A very simple Flask Hello World app for you to get started with...

from FuturosBot import FuturosBot

from flask import request
from flask import Flask
from flask_mysqldb import MySQL
import calendar

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Pytholon!'

#@app.route('/bot', methods=['POST'])
#def bot():
    #parametro = str(request.data, 'UTF-8').lower()
    #bot=FuturosBot()
    #bot.Entrar(parametro)

    #return "OK"

@app.route('/bot', methods=["POST"])
def bot():
    parametros = str(request.data, 'UTF-8').lower()
    bot=FuturosBot()
    bot.Entrar(parametros)

# Generating a timestamp.
    timeStamp = int(round(time.time() * 1000))

    #f= open("salida.txt", "a")
    #f.write(parametro + "\n")
    #f.close()
    return "ok"
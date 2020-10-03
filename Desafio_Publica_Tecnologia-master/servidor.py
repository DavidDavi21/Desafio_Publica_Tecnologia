from flask import Flask, render_template, request, session, redirect, url_for
from peewee import *
from gerenciador import *
from classes import Partida

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"

@app.route("/")
def iniciar():
    return render_template("INDEX.html", partida=Partida.select())

@app.route("/receber_valor", methods=["POST"])
def receber_valor():
    placar = int(request.form["placar_do_jogo"])
    salvar = (organizar_dados(placar, partida=Partida.select()))
    return redirect("/mostrar_dados")

@app.route("/mostrar_dados")
def mostrar_dados():
    return render_template("RESULTADO.html", partida=Partida.select())

@app.route("/zerar_valores")
def zerar_valores():
    deletar = (deletar_dados())
    return redirect("/")

app.run(debug=True)
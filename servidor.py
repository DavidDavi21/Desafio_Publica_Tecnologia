from flask import Flask, render_template, request, session, redirect, url_for
from peewee import *
from gerenciador import organizar_dados
from classes import Partida

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"

@app.route("/")
def iniciar():
    return render_template("INDEX.html")

@app.route("/receber_valor", methods=["POST"])
def receber_valor():
    placar = request.form["placar_do_jogo"]
    print("ei")
    salvar = (organizar_dados(placar))
    print("z")
    return render_template("RESULTADO.html")

@app.route("/salvar_dados")
def salvar(num_jogos, min_temporada, max_temporada, quebra_recorde_max, quebra_recorde_min):
    jogo = Partida.create(num_jogos, placar, min_temporada, max_temporada, quebra_recorde_max, quebra_recorde_min)
    return render_template("RESULTADO.html")

@app.route("/mostrar_dados")
def mostrar_dados():
    return render_template("RESULTADO.html")

app.run(debug=True)
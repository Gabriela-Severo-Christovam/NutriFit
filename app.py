from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector

from flask import session
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("pagina-inicial.html")


@app.route("/paginaprodutos")
def pagina_produtos():
    return render_template("pagina-produtos.html")


app.run()
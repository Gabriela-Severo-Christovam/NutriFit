from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from model.control_usuario import Usuario
from model.control_produto import Produtos

from flask import session
app = Flask(__name__)

@app.route("/")
@app.route("/paginainicial")
def pagina_inicial():
    return render_template("pagina-inicial.html")


@app.route("/paginaprodutos")
def pagina_produtos():
    if "usuario" in session:
        # Recuperar as mensagens
        produtos = Produtos.recuperar_produtos()

        # Enviar as mensagens para o template
        return render_template("pagina-produtos.html", produtos = produtos)
    else:
        return redirect("/paginalogin")

@app.route("/paginalogin")
def paginalogin():
    return render_template("pagina-login.html")   

@app.route("/paginacadastro")
def paginacadastro():
    return render_template("pagina-cadastro.html")   


@app.route("/post/cadastrarusuario", methods= ["POST"])
def post_usuario():
    # Peguei as informações vinda do usuário
    email  = request.form.get("email")
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    endereco = request.form.get("endereco")
    numero = request.form.get("numero")
    senha = request.form.get("senha")

    # Cadastrando a mensagem usando a classe mensagem
    Usuario.cadastro_usuario(email, nome, telefone, endereco, numero, senha)
    
    # Redireciona para o index
    return redirect("/")

@app.route("/post/logar", methods=["POST"])
def post_logar():
    email = request.form.get("email")
    senha = request.form.get("senha")
    
    esta_logado = Usuario.logar(email, senha)

    if esta_logado:
        return redirect('/paginaprodutos')
    else:
        return redirect("/paginalogin")
    
app.run()
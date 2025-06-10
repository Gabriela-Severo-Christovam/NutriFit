from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from model.control_usuario import Usuario
from model.control_produto import Produtos
from model.control_carrinho import Carrinho
from model.control_comentarios import Mensagem

from flask import session
app = Flask(__name__)
app.secret_key = "seila"

@app.route("/")
@app.route("/paginainicial")
def pagina_inicial():
    return render_template("pagina-inicial.html")


@app.route("/paginaprodutos")
def pagina_produtos():
    return redirect("/produtos")

@app.route("/produtos")
def pagina_recuperar():
    produtos = Produtos.recuperar_produtos()
    return render_template("pagina-produtos.html", produtos = produtos)


@app.route("/paginaprodutoespecifico/<cod_produto>")
def pagina_produtos_especifico(cod_produto):
    produtos = Produtos.recuperar_produto_especifico(cod_produto)
    return render_template("pagina-produto-especifico.html", produtos = produtos)


# ROTA QUE SÓ ENTRA NO CARRINHO SE ESTIVER LOGADO
@app.route("/paginacarrinho")
def pagina_carrinho():
    if "usuario" in session: 
        carrinho = Carrinho.recuperar_carrinho()

        return render_template("pagina-compras.html", carrinho = carrinho )
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
    return redirect("/paginalogin")

@app.route("/post/logar", methods=["POST"])
def post_logar():
    email = request.form.get("email")
    senha = request.form.get("senha")
    
    esta_logado = Usuario.logar(email, senha)

    if esta_logado:
        return redirect("/paginainicial")
    else:
        return redirect("/paginalogin")
    
@app.route("/deslogar")
def deslogar():
    session.clear()
    return redirect("/")  

@app.route("/post/cadastrarcomentario", methods = ["POST"])
def post_comentario():
    # Peguei as informações vinda do usuário
    usuario =  session['usuario']  # ENTRE () NOME QUE COLOQUEI NO HTML
    comentario = request.form.get("comentario")

    # Cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrar_mensagem(usuario, comentario)
    
    # Redireciona para o index
    return redirect("/paginaprodutoespecifico/<cod_produto>")


@app.route("/comentario")
def pagina_principal():
    if "usuario" in session:
        #Recuperar as mensagens 
        mensagens = Mensagem.recuperar_mensagems()

        #enviar as mensagens para o template
        return render_template("pagina-produto-especifico.html", mensagens = mensagens)
    else:
        return redirect("/paginaprodutoespecifico/<cod_produto>")
    
# CORRIGIR...
@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/comentario")

@app.route("/put/mensagem/adicionar/curtida/<codigo>")
def adicionar_curtida(codigo):
    Mensagem.adicionar_curtida(codigo)
    return redirect("/comentario")

@app.route("/put/mensagem/deletar/curtida/<codigo>")
def deletar_curtida(codigo):
    Mensagem.deletar_curtida(codigo)
    return redirect("/comentario")


app.run()
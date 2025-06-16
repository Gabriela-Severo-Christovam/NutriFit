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
    produtos = Produtos.recuperar_produtos()
    produto_fotos = Produtos.exibir_produto()
    return render_template("pagina-inicial.html", produtos = produtos, produto_fotos = produto_fotos)

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
    mensagens = Mensagem.recuperar_mensagems()
    return render_template("pagina-produto-especifico.html", produtos = produtos,  mensagens = mensagens)


# ROTA QUE SÓ ENTRA NO CARRINHO SE ESTIVER LOGADO
@app.route("/paginacarrinho")
def pagina_carrinho():
    if "usuario" in session: 
        carrinho = Carrinho.recuperar_carrinho()
        return render_template("pagina-compras.html", carrinho = carrinho )
    else:
        return redirect("/paginalogin")
    

@app.route("/post/addcarrinho/<cod_produto>", methods=["POST"])
def addcarrinho(cod_produto):
    Carrinho.adicionar_carrinho(cod_produto)
    return redirect(f"/produtosespecificocarrinho/{cod_produto}")


@app.route("/produtosespecificocarrinho/<cod_produto>")
def mostrar_produtos(cod_produto):
    produtos = Produtos.recuperar_produto_especifico(cod_produto)
    return render_template('pagina-produto-especifico.html', produtos=produtos)


@app.route("/limparcarrinho/<cod_carrinho>")
def limpar_carrinho(cod_carrinho):
    deletar = Carrinho.deletar_carrinho(cod_carrinho) 
    carrinho = Carrinho.recuperar_carrinho()
    return render_template("pagina-compras.html", deletar=deletar, carrinho=carrinho)


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


@app.route("/post/cadastrarcomentario/<cod_produto>", methods = ["POST"])
def post_comentario(cod_produto):
    # Peguei as informações vinda do usuário

    if "usuario" not in session:
        return redirect("/paginalogin") 
    
    usuario =  session['usuario']  # ENTRE () NOME QUE COLOQUEI NO HTML
    comentario = request.form.get("comentario")

    # Cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrar_mensagem(usuario, comentario)
    Produtos.recuperar_produto_especifico(cod_produto)
    
    # Redireciona para o index
    return redirect(f"/paginaprodutoespecifico/{cod_produto}")


@app.route("/comentario")
def pagina_principal():
    if "usuario" in session:
        #Recuperar as mensagens 
        mensagens = Mensagem.recuperar_mensagems()

        #enviar as mensagens para o template
        return render_template("pagina-produto-especifico.html", mensagens = mensagens)
    else:
        return redirect("/paginaprodutoespecifico/<cod_produto>")
    

app.run(debug=True)
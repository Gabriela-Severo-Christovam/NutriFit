from data.conexao import Conexao
from hashlib import sha256
from flask import session

class Usuario:
    def cadastro_usuario(email, nome, telefone, endereco, numero, senha):
       
        #Criptografando senha
        senha =  sha256(senha.encode()).hexdigest()

        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """INSERT INTO tbUsuario
                    (email, nome, telefone, endereco, numero, senha)
                VALUES
                    (%s, %s, %s, %s, %s, %s)"""
                
        valores = (email, nome, telefone, endereco, numero, senha)
    
        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()


    def recuperar_usuario():

        #Criar conexão 
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = "SELECT email, nome, senha  FROM tbUsuario;"

        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel 
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado
    
    
    def logar(email, senha):

        #Criptografando senha
        senha =  sha256(senha.encode()).hexdigest()

        #Criar conexão 
        conexao = Conexao.criar_conexao()

         # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary=True)

        # Criando o sql que será executado
        sql = "SELECT email, nome FROM tbUsuario WHERE email =  %s AND binary senha = %s;"

        valores = (email, senha)

        #Executando o comando sql
        cursor.execute(sql, valores) 

        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        if resultado:
            session['usuario'] = resultado['email']
            session['nome_usuario'] = resultado['nome']
            return True
        else:
            return False

    def logoff():
        session.clear()
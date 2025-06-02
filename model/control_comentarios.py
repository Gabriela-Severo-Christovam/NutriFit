import datetime
from data.conexao import Conexao 

class Mensagem:
    
    def  cadastrar_mensagem(usuario, comentario):

        data_hora = datetime.datetime.today()
   
   
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """INSERT INTO tbComentarios
                    (nome, data_hora, comentario)
                VALUES
                    (%s, %s, %s)"""
                
        valores = (usuario, data_hora, comentario)
    
        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()


    def recuperar_mensagems():

        #Criar conexão 
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = "SELECT cod_comentario, nome AS usuario, comentario, data_hora, curtidas FROM tbComentarios;"

        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel 
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado
    

    def deletar_mensagem(codigo):
          # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """DELETE FROM tbComentarios WHERE cod_comentario = %s;"""
        valores = (codigo,)

        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()


    def adicionar_curtida(codigo):
        #Criar conexão 
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """UPDATE tbComentarios
               SET curtidas = curtidas + 1
               WHERE cod_comentario = %s;"""

        valores = (codigo,)

        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
    
        # Fecho a conexao com o banco
        conexao.close()

    def deletar_curtida(codigo):

         #Criar conexão 
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """UPDATE tbComentarios
               SET curtidas = curtidas - 1
               WHERE cod_comentario = %s;"""

        valores = (codigo,)

        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
    
        # Fecho a conexao com o banco
        conexao.close()

    
    def ultima_mensagem(nome):
         #Criar conexão 
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = "SELECT comentario FROM tbComentarios WHERE nome = %s ORDER BY data_hora DESC LIMIT 1;"

        valores = (nome, )

        #Executando o comando sql
        cursor.execute(sql, valores)        

        #Recuperando os dados e jogando em uma varialvel 
        resultado = cursor.fetchone()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado

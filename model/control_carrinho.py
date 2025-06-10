from data.conexao import Conexao

class Carrinho:
    def adicionar_carrinho(cod_produto):
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado              
        sql = """INSERT INTO tbCarrinho
                            (cod_produto)
                VALUES
                    (%s);"""
        valores = (cod_produto,)
       
        # Executando o comnado sql
        cursor.execute(sql,valores)
       
        # Confirmo a alteração, SERVE PAR FIXAR ALTERAÇÃO, SE ALTEROU, EXCLUIU OU FEZ UPDATE, OU SEJA SERVE PARA CONFIRMAR ALTERAÇÃO
        conexao.commit()
       
        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def recuperar_carrinho():
     
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary= True)

         # Criando o sql que será executado
        sql = """SELECT
                tbProdutos.nome AS nome_produto,
                tbProdutos.descricao AS descricao_produto,
                tbProdutos.preco,
                tbProdutos.cod_produto,
                tbCarrinho.cod_carrinho AS cod_carrinho,
                tbFotosProdutos.url AS url_foto
            FROM
                tbCarrinho
            INNER JOIN
                tbProdutos ON tbCarrinho.cod_produto = tbProdutos.cod_produto
            INNER JOIN
                tbFotosProdutos ON tbProdutos.cod_produto = tbFotosProdutos.cod_produto;
            GROUP BY tbProdutos.cod_produto;
            """
                   
        # Executando o comnado sql
        cursor.execute(sql)
       
        # Recuperando os dados e guardando em uma variavel
        resultado = cursor.fetchall()
       
        # Fecho a conexao com o banco
        conexao.close()

        return resultado
   
 
    def deletar_carrinho(cod_carrinho):
          # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """DELETE from tbCarrinho WHERE cod_carrinho = %s;"""
                   
        valores = (cod_carrinho,)
       
        # Executando o comnado sql
        cursor.execute(sql,valores)
       
        # Confirmo a alteração, SERVE PAR FIXAR ALTERAÇÃO, SE ALTEROU, EXCLUIU OU FEZ UPDATE, OU SEJA SERVE PARA CONFIRMAR ALTERAÇÃO
        conexao.commit()
       
        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()    
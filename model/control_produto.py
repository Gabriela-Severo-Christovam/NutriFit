from data.conexao import Conexao

class Produtos:
    def recuperar_produtos():
        #Criar conexão
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = """
                SELECT
                    tbProdutos.nome AS nome_produto,
                    tbProdutos.descricao AS descricao_produto,
                    tbProdutos.preco,
                    tbProdutos.cod_produto,
                    tbCategoria.descricao AS categoria_produto,
                    tbFotosProdutos.url AS url_foto
                FROM 
                    tbProdutos
                INNER JOIN tbCategoria
                    ON tbProdutos.cod_categorias = tbCategoria.cod_categorias
                INNER JOIN tbFotosProdutos
                    ON tbProdutos.cod_produto = tbFotosProdutos.cod_produto
			        GROUP BY tbProdutos.cod_produto;"""

        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado
    
    
    def recuperar_produto_especifico(cod_produto):
        #Criar conexão
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = """
            SELECT
                tbProdutos.nome AS nome_produto,
                tbProdutos.descricao AS descricao_produto,
                tbProdutos.preco,
                tbProdutos.cod_produto,
                tbCategoria.descricao AS categoria_produto,
                tbFotosProdutos.url AS url_foto
            FROM 
                tbProdutos
            INNER JOIN tbCategoria
                ON tbProdutos.cod_categorias = tbCategoria.cod_categorias
            INNER JOIN tbFotosProdutos
                ON tbProdutos.cod_produto = tbFotosProdutos.cod_produto
            WHERE 
                tbProdutos.cod_produto = %s;
            """

        valores = (cod_produto, )
        #Executando o comando sql
        cursor.execute(sql, valores)        

        #Recuperando os dados e jogando em uma varialvel
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado
    
    def exibir_produto():
        #Criar conexão
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = """
            SELECT 
                p.nome AS nome_produto,
                f.url
            FROM 
                tbFotosProdutos f
            JOIN 
                tbProdutos p ON f.cod_produto = p.cod_produto
            WHERE 
                f.cod_foto IN (1, 3, 4, 6);"""

      
        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado
    
   
   
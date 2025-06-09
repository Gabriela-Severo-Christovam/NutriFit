import mysql.connector

class Conexao:
    
    def criar_conexao():
        # Criando a conexão com o banco de dados
        # conexao = mysql.connector.connect(host = "bdgodofredo-alexstocco-93db.b.aivencloud.com",
        #                                 port = 27974,
        #                                 user = "3ds",
        #                                 password = "banana",
        #                                 database = "db_feedback")
        
        
        # Criando a conexão com o banco de dados
        # conexao = mysql.connector.connect(host = "localhost",
        #                                 port = 3306,
        #                                 user = "root",
        #                                 password = "root",
        #                                 database = "dbNutriFit")
        
        # conexao = mysql.connector.connect(host = "bdnutrifit-nutrifit.c.aivencloud.com",
        #                                 port = 19284,
        #                                 user = "avnadmin",
        #                                 password = "AVNS_JYqgtjLoovtRs3_GrDj",
        #                                 database = "defaultdb")


        conexao = mysql.connector.connect(host = "msqlnutrifit-bdnutrifit.i.aivencloud.com",
                                        port = 25804,
                                        user = "avnadmin",
                                        password = "AVNS_EdjccFzU2a1ug7FkmRI",
                                        database = "dbNutriFit")

        return conexao
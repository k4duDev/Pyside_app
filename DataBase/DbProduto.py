import sqlite3


class Data_Base():
    def __init__(self, name = "Cosmeticos.db") -> None:
        self.name = name
    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connect(self):
        try:
            self.connection.close()
        except:
            pass

    def Create_Table_Produto(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS Produto
                (

                    Codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Id INTERGE NOT NULL,                    
                    Produto TEXT NOT NULL,
                    Tipo TEXT NOT NULL,
                    Custo TEXT NOT NULL,
                    Preco TEXT NOT NULL as ('')
                    
                );
            
            """)

            # FOREIGN KEY("Id") REFERENCES "Compras"("Id"),
                    # FOREIGN KEY("Custo") REFERENCES "Compras"("Custo"),
                    # FOREIGN KEY("Produto") REFERENCES "Compras"("Produto"),
                    # FOREIGN KEY("Tipo") REFERENCES "Compras"("Tipo")
        except AttributeError:
            print("faça a conexão")
            """ CREATE TABLE track(
                trackid     INTEGER, 
                trackname   TEXT, 
                trackartist INTEGER,
                FOREIGN KEY(trackartist) REFERENCES artist(artistid)
                ); """
       
    def Insert_Produto(self, Id, Produto, Tipo, Custo):

        cursor = self.connection.cursor()
        cursor.execute("""

            INSERT INTO Produto
            (Id, Produto, Tipo, Custo) VALUES(?,?,?,?)
        
        """,(Id, Produto, Tipo, Custo))
        self.connection.commit()


    def Register_Produto(self, fullDataSet):
        
        campos_tabela = ('Id', 'Produto', 'Tipo', 'Custo', 'Preco')

        qntd = ("?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Produto
             {campos_tabela} VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return("Erro")
    

    def Select_All_Produto(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Produto;

            """)
            lista = cursor.fetchall()
            return lista
        except:
            pass

    
    def Select_All_Dados(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                 SELECT Id, Produto, Tipo, Custo FROM Produto;
                
                """)
            lista = cursor.fetchall()
            return lista
        except:
            pass


    def Select_All_ComprasProdutos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                 select Id, Produto, Tipo, Custo from Compras;
                
                """)
            lista = cursor.fetchall()
            return lista
        except:
            pass


    def Atualiza(self):

        try:
            cursor = self.connection.cursor()
            cursor.execute(""" INSERT INTO Produto (Id, Produto, Tipo, Custo)

                select Id, Produto, Tipo, Custo from Compras;

                """)

            self.connection.commit()
            return ("OK")
        
        except:
            return ("Erro")

    def Update_Produto(self, fullDataSet):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Produto SET

                Codigo = '{fullDataSet[0]}',
                Id = '{fullDataSet[1]}',
                Produto = '{fullDataSet[2]}',
                Tipo = '{fullDataSet[3]}',
                custo = '{fullDataSet[4]}',
                Preco = '{fullDataSet[5]}',

                """)  #WHERE codigo = '{fullDataSet[0]}'
 
            self.connection.commit()
            return ("OK")
        
        except:
            return ("Erro")


    def Delete_Produto(self, codigo):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Produto WHERE Codigo = '{codigo}' ")
            self.connection.commit()
            return "Cadastro  excluido com Sucesso!"
        except:
            return "Erro ao Excluir Regitro!"
        
    

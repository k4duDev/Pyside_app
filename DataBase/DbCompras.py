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

    def Create_Table_Compras(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS Compras
                (

                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Data TEXT NOT NULL,                    
                    Produto TEXT NOT NULL,
                    Tipo TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    Custo TEXT NOT NULL                    
                    
                );
            
            """)
        except AttributeError:
            print("faça a conexão")


    def Register_Compras(self, fullDataSet):
        
        campos_tabela = ('Data', 'Produto', 'Tipo', 'Quantidade', 'Custo')

        qntd = ("?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Compras
             {campos_tabela} VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return("Erro")
    

    def Select_All_Compras(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Compras;

            """)
            lista = cursor.fetchall()
            return lista
        except:
            pass

    def Update_Compras(self, fullDataSet):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Compras SET

                Id = '{fullDataSet[0]}',
                Data = '{fullDataSet[1]}',
                Produto = '{fullDataSet[2]}',
                Tipo = '{fullDataSet[3]}',
                Quantidade = '{fullDataSet[4]}',
                Custo = '{fullDataSet[5]}'

                WHERE Id = '{fullDataSet[0]}'""")

            self.connection.commit()
            return ("OK")
        
        except:
            return ("Erro")

    def Delete_Compras(self, id):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Compras WHERE ID = '{id}' ")
            self.connection.commit()
            return "Cadastro  excluido com Sucesso!"
        except:
            return "Erro ao Excluir Regitro!"
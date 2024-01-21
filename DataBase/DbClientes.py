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

    def Create_Table_Clientes(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS Clientes(

                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Data TEXT NOT NULL,                    
                    Nome TEXT NOT NULL,
                    Telefone INTEGER NOT NULL,
                    Endereco TEXT NOT NULL                    
                    
                );
            
            """)
        except AttributeError:
            print("faça a conexão")

    def Insert_Clientes(self, Data, Nome, Telefone, Endereco):

        cursor = self.connection.cursor()
        cursor.execute("""

            INSERT INTO Clientes(Data, Nome, Telefone, Endereco) VALUES(?,?,?,?)
        
        """,(Data, Nome, Telefone, Endereco))
        self.connection.commit()

    def Register_Clientes(self, fullDataSet):
        
        campos_tabela = ('Data', 'Nome', 'Telefone', 'Endereco')

        qntd = ("?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Clientes {campos_tabela} VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return("Erro")
    

    def Select_All_Clientes(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Clientes;

            """)
            lista = cursor.fetchall()
            return lista
        except:
            pass

    def Update_Clientes(self, fullDataSet):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Clientes SET

                Id = '{fullDataSet[0]}',
                Data = '{fullDataSet[1]}',
                Nome = '{fullDataSet[2]}',
                Telefone = '{fullDataSet[3]}',
                Endereco = '{fullDataSet[4]}'

                WHERE Id = '{fullDataSet[0]}'""")

            self.connection.commit()
            return ("OK")
        
        except:
            return ("Erro")


    def Delete_Clientes(self, id):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Clientes WHERE ID = '{id}' ")
            self.connection.commit()
            return "Cadastro  excluido com Sucesso!"
        except:
            return "Erro ao Excluir Regitro!"
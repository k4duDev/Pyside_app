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

    def Create_Table_Vendas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS Vendas(

                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Data TEXT NOT NULL,                    
                    Nome TEXT NOT NULL,
                    Produto TEXT NOT NULL,
                    Quantidade INTEGER NOT NULL,
                    Valor INTEGER NOT NULL,
                    SubTotal INTEGER NOT NULL,
                    Pagamento TEXT NOT NULL                    
                    
                );
            
            """)
        except AttributeError:
            print("faça a conexão")

    def Insert_Vendas(self, Data, Nome, Produto, Quantidade, Valor, SubTotal, Pagamento):

        campos_tabela = ('Data', 'Nome', 'Produto', 'Quantidade', 'Valor', 'SubTotal', 'Pagamento')
        qntd = ("?,?,?,?,?,?,?")

        cursor = self.connection.cursor()
        cursor.execute(f"""

            INSERT INTO Vendas {campos_tabela} VALUES({qntd})
        
        """,(Data, Nome, Produto, Quantidade, Valor, SubTotal, Pagamento))
        self.connection.commit()

    def Register_Vendas(self, fullDataSet):
        
        campos_tabela = ('Data', 'Nome', 'Produto', 'Quantidade', 'Valor', 'SubTotal', 'Pagamento')
        qntd = ("?,?,?,?,?,?,?")

        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Vendas {campos_tabela} VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return("Erro")
    

    def Select_All_Vendas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Vendas;

            """)
            lista = cursor.fetchall()
            return lista
        except:
            pass

    def Update_Vendas(self, fullDataSet):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Vendas SET

                Id = '{fullDataSet[0]}',
                Data = '{fullDataSet[1]}',
                Nome = '{fullDataSet[2]}',
                Produto = '{fullDataSet[3]}',
                Quantidade = '{fullDataSet[4]}',
                Valor = '{fullDataSet[5]}',
                SubTotal = '{fullDataSet[6]}',
                Pagamento = '{fullDataSet[7]}'

                WHERE Id = '{fullDataSet[0]}'""")

            self.connection.commit()
            return ("OK")
        
        except:
            return ("Erro")


    def Delete_Vendas(self, id):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Vendas WHERE ID = '{id}' ")
            self.connection.commit()
            return "Cadastro  excluido com Sucesso!"
        except:
            return "Erro ao Excluir Regitro!"
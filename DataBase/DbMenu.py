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


    def Select_All_Clientes(self):
            try:
                cursor = self.connection.cursor()
                cursor.execute("""

                    SELECT * FROM Clientes;

                """)
                Cli = cursor.fetchall()
                return Cli
            except:
                pass

    def Select_All_Compras(self):
            try:
                cursor = self.connection.cursor()
                cursor.execute("""

                    SELECT * FROM Compras;

                """)
                Com = cursor.fetchall()
                return Com
            except:
                pass

    def Select_All_Estoque(self):
            try:
                cursor = self.connection.cursor()
                cursor.execute("""

                    SELECT Id, Produto, Quantidade FROM Compras;

                """)
                Est = cursor.fetchall()
                return Est
            except:
                pass
    
    def Select_All_Produto(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Produto;

            """)
            Prod = cursor.fetchall()
            return Prod
        except:
            pass

    
    def select_all_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM USUARIOS;

            """)
            User = cursor.fetchall()
            return User
        except:
            pass

    def Select_All_Vendas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Vendas;

            """)
            Ven = cursor.fetchall()
            return Ven
        except:
            pass


    
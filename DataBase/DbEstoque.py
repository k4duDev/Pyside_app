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
        
    def Select_All_Estoque(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT Id, Produto, Quantidade FROM Compras;

            """)
            lista = cursor.fetchall()
            return lista
        except:
            pass
            

#TB_Compras = ('Id', 'Produto', 'Quantidade')
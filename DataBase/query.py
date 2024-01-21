import sqlite3

class sqlite3_db():
    

    def __init__(self, banco = None):
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self,banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            #print ('Conecção Criada com Sucesso!')
        except sqlite3.Error as e:
            print ('Não foi Possivel Conectar-se')

    def close_connect(self):
        try:
            self.conn.close()
        except:
            pass

    def Geral (self,query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()


    def Dados(self,query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
#db = sqlite3_db("Cosmeticos.db")
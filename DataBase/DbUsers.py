import sqlite3


class Data_Base():
    def __init__(self, name = "Cosmeticos.db") -> None:
        self.name = name

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.name)
        except:
            pass

    def close_connect(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS Usuarios(

                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Data DATA NOT NULL,
                    Nome TEXT NOT NULL,
                    Telefone INTEGER NOT NULL,
                    Endereco TEXT NOT NULL,
                    User TEXT UNIQUE NOT NULL,
                    Password TEXT NOT NULL,
                    Access TEXT NOT NULL
                    
                );
            
            """)
        except AttributeError:
            print("faça a conexão")

    def insert_user(self, Data, Nome, Telefone, Endereco, User, Password, Access):

        cursor = self.connection.cursor()
        cursor.execute("""

            INSERT INTO Usuarios(Data, Nome, Telefone, Endereco, User, Password, Access) VALUES(?,?,?,?,?,?,?);
        
        """,(Data, Nome, Telefone, Endereco, User, Password, Access))
        self.connection.commit()

   
    def check_user(self, user, password):

        try: 
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Usuarios;
            
            """)

            for linha in cursor.fetchall():
                if linha[5].upper() == user.upper() and linha[6] == password and linha[7] == "Administrador":
                    return "Administrador"
 
                elif linha[5].upper() == user.upper() and linha[6] == password and linha[7] == "Usuário":        
                    return "user"

                else:
                    continue
            return "sem acesso"
        except:
            pass


    def select_all_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM USUARIOS;

            """)
            lista = cursor.fetchall()
            return lista
        except:
            pass


    def update_users(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE USUARIOS set

            Id = '{fullDataSet[0]}',
            Data = '{fullDataSet[1]}',
            Nome = '{fullDataSet[2]}',
            Telefone = '{fullDataSet[3]}',
            Endereco = '{fullDataSet[4]}',
            User = '{fullDataSet[5]}',
            Password = '{fullDataSet[6]}',
            Access = '{fullDataSet[7]}'

            WHERE Id = '{fullDataSet[0]}'""")

        self.connection.commit() 


    def delete_users(self, id):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM USUARIOS WHERE ID = '{id}' ")
            self.connection.commit()
            return "Cadastro  excluido com Sucesso!"
        except:
            return "Erro ao Excluir Regitro!"
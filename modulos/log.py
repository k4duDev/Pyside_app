from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from PySide2.QtPrintSupport import *
import os,sys
from template.Log import Ui_Login
from modulos.menu import Start
from DataBase.query import sqlite3_db
from DataBase.DbUsers import Data_Base
from modulos.calendario import Data
import time


class Inicio(QDialog): 
    def __init__(self,diaFormat) -> None:
        super(Inicio, self).__init__()
        self.ui = Ui_Login()
        self.tentativas = 0
        self.ui.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        appIcon = QIcon('imagens/cade.png')
        self.setWindowIcon(appIcon)        

        self.ui.Btn_Entrar.clicked.connect(self.checkLogin)

        self.diaFormat = diaFormat

#-------------------   VERIFICA USUARIO   -------------------------------

    def checkLogin(self):
        self.user = self.ui.L_User.text()
        self.password = self.ui.L_Senha.text()

        db = Data_Base()
        db.connect()        
        if self.user == "admin" and self.password == "admin":
            
            self.autenticado = "administrador"
            self.window = Start(self.user,self.autenticado.lower(),diaFormat=self.diaFormat)
            self.window.show()
            self.hide()

        else:
            self.autenticado =  db.check_user(self.user.upper(), self.password)

            if self.autenticado.lower() == "administrador" or self.autenticado.lower() == "user":
                
                self.w = Start(self.user, self.autenticado.lower(),diaFormat=self.diaFormat)
                self.w.show()
                self.hide()
            else:

                if self.tentativas < 3:
                    QMessageBox.warning(QMessageBox(),"Erro ao acessar", f"Login ou senha incorreto \n \n Tentativa: {self.tentativas+1} de 3")
                    self.tentativas += 1
                if self.tentativas == 3:
                    #bloquear o usuário 
                    db.close_connection()
                    sys.exit(0)


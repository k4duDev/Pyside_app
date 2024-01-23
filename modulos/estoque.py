from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
import os,sys
from template.Estoque import Ui_Estoque
import sqlite3
from DataBase.DbEstoque import Data_Base


class Estoq(QDialog):
    def __init__(self,user,autenticado,diaFormat,*args,**argvs):
        super(Estoq, self).__init__(*args,**argvs)
        self.ui = Ui_Estoque()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/Fundo.png")
        self.setWindowIcon(appIcon)

        self.table_Estoque()
        #self.Carregadados()
        self.ui.btn_Voltar.clicked.connect(self.AbrirMenu)
        self.diaFormat = diaFormat
        self.user = user
        self.autenticado = autenticado
    

    def AbrirMenu(self):
        from modulos.menu import Start
        self.menu = Start(user=(self.user),autenticado=(self.autenticado),diaFormat=self.diaFormat)
        self.menu.show()
        self.close()
        
    def table_Estoque(self):

        self.ui.Tab_Estoque.setColumnWidth(0, 50)
        self.ui.Tab_Estoque.setColumnWidth(1, 300)
        self.ui.Tab_Estoque.setColumnWidth(2, 100)
        self.ui.Tab_Estoque.setColumnWidth(3, 100)
        self.ui.Tab_Estoque.setColumnWidth(4, 100)

        db = Data_Base()
        db.connect()
        coletar = db.Select_All_Estoque()
        self.ui.Tab_Estoque.clearContents()        
        self.ui.Tab_Estoque.setRowCount(len(coletar))

        for row, text in enumerate(coletar):

            for column, data in enumerate(text):
                self.ui.Tab_Estoque.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connect()
        
        for row, text in enumerate(coletar):
            for i, column in enumerate(text):
                novalista = []
                #if not novalista:
                novalista.append(column)
                    #novalista = str(novalista)
                quant = novalista[:2]
                print(quant)


    def Carregadados(self):
        db = Data_Base
        db.connect()

        lista = db.Select_All_Estoque()
        self.ui.Tab_Estoque.clearContents()

        self.ui.Tab_Estoque.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.Tab_Estoque.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.Tab_Estoque.setItem(linha,coluna_n,QTableWidgetItem(str(dados)))

        db.close_connect()

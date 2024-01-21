import os,sys
from PySide2 import QtCore
from PySide2.QtCore import Qt, QEasingCurve, QPropertyAnimation
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication, QPushButton, QWidget,QMainWindow
from modulos.clientes import Clients
from modulos.compras import Comp
from modulos.estoque import Estoq
from modulos.produtos import Prod
from modulos.usuarios import Users
from modulos.vendas import Vendas
from modulos.calendario import Data
from template.Menu import Ui_Menu
import matplotlib.pyplot as plt
import numpy as np
from DataBase.DbMenu import Data_Base

class Start(QMainWindow):
    def __init__(self,user,autenticado,diaFormat,*args,**kwargs):
        super(Start, self).__init__(*args,**kwargs)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/MLogo.png")
        self.setWindowIcon(appIcon)
        #self.dd.cal.Calendario.selectionChanged.connect(self.Form)

        self.diaFormat = diaFormat
        print(diaFormat)
#----------------------   NOME DE USUÁRIO  ----------------------------------------------

        #self.Data = diaFormat
        #self.ui.L_Data.setText(self.cal.diaFormat)
        self.usuario = user
        self.ui.L_usuario.setEnabled(False)
        self.ui.L_usuario.setText(self.usuario)

#--------------------   PERMISSAO DE ACESSO AO FORMULARIO DE USUARIOS   ------------------

        self.permissao = autenticado
        if self.permissao == "user":
            self.ui.Btn_Usuarios.setVisible(False)
            self.ui.actionUsuarios.setVisible(False)

        elif self.permissao == "administrador":
            self.ui.Btn_Usuarios.setVisible(True)
            self.ui.actionUsuarios.setVisible(True)

#---------------------------  TOGGLE BUTTON  ------------------------------
        self.ui.BtnToggle.clicked.connect(self.Left_Menu)
        
# ----------------------------   MENU   -----------------------------------
        self.ui.actionFechar.triggered.connect(quit)
        self.ui.actionClientes.triggered.connect(self.AbrirCad)
        self.ui.actionCompras.triggered.connect(self.AbrirComp)
        #self.ui.actionContatos.triggered.connect()
        self.ui.actionEstoque.triggered.connect(self.AbrirEstoque)
        self.ui.actionProdutos.triggered.connect(self.AbrirProdutos)
        #self.ui.actionSobre.triggered.connect()
        self.ui.actionUsuarios.triggered.connect(self.AbrirUsuarios)
        self.ui.actionVendas.triggered.connect(self.AbrirVendas)
        
# -----------------------------  BUTTONS   --------------------------------

        self.ui.Btn_Clientes.clicked.connect(self.AbrirCad)
        self.ui.Btn_Compras.clicked.connect(self.AbrirComp)
        self.ui.Btn_Estoque.clicked.connect(self.AbrirEstoque)
        self.ui.Btn_Produtos.clicked.connect(self.AbrirProdutos)
        self.ui.Btn_Usuarios.clicked.connect(self.AbrirUsuarios)
        self.ui.Btn_Vendas.clicked.connect(self.AbrirVendas)
        self.ui.Btn_Calen.clicked.connect(self.Dia)

#-----------------------------   GRAFICOS  -----------------------------
        
        self.Graficos()

#---------------------------   ABRI O PAINEL COM BOTOES    ----------------

    def Left_Menu(self):

        width = self.ui.LeftMenu.width()

        if width == 0:
            newWidth = 201
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.ui.LeftMenu, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

# ------------------------- METHOR ABRIR FORMULARIOS -------------------

    def AbrirCad(self):
        self.hide()
        self.Cli = Clients(user=(self.usuario),autenticado=(self.permissao))
        self.Cli.show()
        
    def AbrirComp(self):
        self.hide()
        self.Compr = Comp(user=(self.usuario),autenticado=(self.permissao))
        self.Compr.show()

    def AbrirEstoque(self):
        self.Est = Estoq()
        self.Est.show()

    def AbrirProdutos(self):
        self.hide()
        self.Produ = Prod(user=(self.usuario),autenticado=(self.permissao))
        self.Produ.show()

    def AbrirUsuarios(self):
        self.hide()
        self.Usu = Users(user=(self.usuario),autenticado=(self.permissao))
        self.Usu.show()    

    def AbrirVendas(self):
        self.Tela = Vendas(user=(self.usuario),autenticado=(self.permissao))
        self.Tela.show()
    
    def AbrirCalen(self):
        self.hide()
        self.Calen = Clients(user=(self.usuario),autenticado=(self.permissao))
        self.Calen.show()

# ------------------------- METHOR ABRIR GRAFICOS -------------------
        
    def Graficos(self):

        db = Data_Base()
        db.connect()

        Clie = db.Select_All_Clientes()
        Comp = db.Select_All_Compras()
        Esto = db.Select_All_Estoque()
        Produ = db.Select_All_Produto()
        Use = db.select_all_users()
        vend = db.Select_All_Vendas()

        db.close_connect

        jan = 1
        fev = 2
        mar = 3
        abr = 4
        maio = 5
        jun = 6
        jul = 7
        ago = 8
        set = 9
        out = 10
        nov = 11
        dez = 12

        if not Clie:
            pass
        else:
            da = np.column_stack(Clie[0][1])
            print(da)
        
            for row, i in enumerate(Clie):
                dados = []
                dados.append(i)
                
                data = dados[0][1]
                #data = str(data)
                clientes = []
                clientes = dados[0][2]
                #clientes = str(clientes)

        mes = ('jan', 'fev', 'mar', 'abr', 'maio', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')   
        #print(data)#, clientes)       

        #fig = plt.figure()
        #fig, ax = plt.subplots()
        # barras = plt.bar(mes, clientes)
        # plt.bar_label(barras, labels=[clientes])
        # plt.title('Clientes Mensal')
        # plt.ylabel('clientes')
        # plt.xlabel('Meses')
        # #ax.plot([data], [clientes])
        # plt.show()

    def Dia(self):
        self.Dat = Data(diaFormat = (self.diaFormat))  
        self.Dat.show ()
        # self.Carrega()
        
    # def Carrega(self):
    #     #self.di = Calendario()
        
    #     self.dd = Data()
    #     d = str(self.dd.Cal.Calendario.selectedDate())
    #     self.Form = d[21:33]
        
    #     #self.dd.diaFormat = self.dd.Funcao()
    #     self.ui.L_Data.setText(self.Form) 
    #     print(self.Form)
# ------------------------- CALENDARIO -------------------

# class Data(QDialog):
#     def __init__(self,*args,**argvs):
#         super(Data, self).__init__(*args,**argvs)
#         self.Cal = Calendario()
#         self.Cal.setupUi(self)
#         self.setWindowTitle("Mk.Cosmeticos")
#         appIcon = QIcon(u"/imagens/Fundo.png")
#         self.setWindowIcon(appIcon)
        
#         self.Cal.Calendario.selectionChanged.connect(self.Funcao)
#         #self.ui = Ui_Menu()
        
        
#     def Funcao(self):
        
#         self.dia = str(self.Cal.Calendario.selectedDate())
#         self.diaFormat = self.dia[21:33]
#         self.Cal.data.setText(self.diaFormat)
#         #self.ui.L_Data.setText(self.Cal.data)
#         #return self.diaFormat
        
    
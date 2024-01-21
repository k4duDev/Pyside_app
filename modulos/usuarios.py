from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow, QDateEdit
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
import os,sys
from template.Usuarios import Ui_Usuarios
from modulos.calendario import Data
from DataBase.DbUsers import Data_Base


class Users(QDialog):
    def __init__(self,user,autenticado,*args,**argvs):
        super(Users, self).__init__(*args,**argvs)
        self.ui = Ui_Usuarios()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/Fundo.png")
        self.setWindowIcon(appIcon)

        self.user = user
        self.autenticado = autenticado

        # self.ui.Tab_Usuarios.setColumnWidth(1, 218)
        self.Tab_Users()
        self.Table_users()       
        self.ui.btn_Salvar.clicked.connect(self.cad_Users)
        self.ui.btn_Excluir.clicked.connect(self.Deletar_Users)
        self.ui.btn_Limpar.clicked.connect(self.limpar)
        self.ui.btn_Voltar.clicked.connect(self.AbrirMenu)
        self.ui.btn_Data.clicked.connect(self.Dia)

        """ quit = QWidget.actionEvent(quit, self)
        quit.triggered.connect(self.closeEvent) """

        self.ui.Tab_Usuarios.itemSelectionChanged.connect(self.PreencherCampos_Automaticamente)

 
    def PegaSelecaoDaTabela(self):  # pega id seleção da tabela
        valor = self.ui.Tab_Usuarios.item(self.PegaSelecaoDoBanco(), 0) 
        return valor.text() if not valor is None else valor  #deve retornar valor str não memoria

    def PegaSelecaoDoBanco(self):  # pega id seleção do banco
        return self.ui.Tab_Usuarios.currentRow() 

#--------------------------------   CARREGA CAMPOS COM DADOS DA TABELA   ----------------------------------

    def PreencherCampos_Automaticamente(self):
        IdLinhaSelecionada = self.PegaSelecaoDoBanco()

        if self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 0) != None:
            id = self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 0).text()
            self.ui.L_Id.setText(id)

        if self.ui.Tab_Usuarios.item(IdLinhaSelecionada,1) != None:
            data = self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 1).text()
            self.ui.L_Data.setText(data)

        if self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 2) != None:
            nome = self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 2).text()
            self.ui.L_Nome.setText(nome)

        if self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 3) != None:
            telefone = self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 3).text()
            self.ui.L_Telefone.setText(telefone)

        if self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 4) != None:
            endereco = self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 4).text()
            self.ui.L_Endereco.setText(endereco)

        if self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 5) != None:
            usuario = self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 5).text()
            self.ui.L_Usuario.setText(usuario)

        if self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 6) != None:
            senha = self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 6).text()
            self.ui.L_Senha.setText(senha)

        if self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 7) != None:
            permicao = self.ui.Tab_Usuarios.item(IdLinhaSelecionada, 7).text()
            self.ui.Cbb_Permicao.setCurrentText(permicao)
        


#                           FECHA JANELA ATUAL E REABRE A FECHADA
    """ def CloseEvent(self,event):
        reply=QMessageBox.question(self,'Alerta!',"Tem certeza que deseja sair ?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept():
            self.menu.show()  #JANELA Á SER ABERTA
            self.clearMask()
            self.destroy()
        else:
            event.ignore()
    
    
    def closeEvent(self,event):
        self.menu.exec(object) """

    def Tab_Users(self):
        db = Data_Base()
        db.connect()
        db.create_table_users()
        db.close_connect()

    def AbrirMenu(self):
        from modulos.menu import Start
        self.menu = Start(user=(self.user),autenticado=(self.autenticado))
        self.menu.show()
        self.close()
        
    def limpar(self):

        self.ui.L_Id.setText("")
        self.ui.L_Data.setText("")
        self.ui.L_Nome.setText("")
        self.ui.L_Telefone.setText("") 
        self.ui.L_Endereco.setText("")
        self.ui.L_Usuario.setText("")
        self.ui.L_Senha.setText("") 
        self.ui.Cbb_Permicao.setCurrentText("") 

    def cad_Users(self):
    
        data = self.ui.L_Data.text()
        nome = self.ui.L_Nome.text()
        fone = self.ui.L_Telefone.text()
        endereco = self.ui.L_Endereco.text()       
        user = self.ui.L_Usuario.text()
        password = self.ui.L_Senha.text()
        access = self.ui.Cbb_Permicao.currentText() 

        if data == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif nome == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif fone == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif endereco == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif user == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif password == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif access == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        else:

            db = Data_Base()
            db.connect()
            db.insert_user(data, nome, fone, endereco, user, password, access)                        
            self.Table_users()
            self.limpar()
            QMessageBox.information(QMessageBox(),"Cadastro Realizado", "Cadastro Realizado com Sucesso!")
            db.close_connect()



    def Deletar_Users(self):
        db = Data_Base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("EXCLUIR")
        msg.setText("Este registro sera Excluído.")
        msg.setInformativeText(f"Você tem certeza que deseja excluir? \n \n {self.ui.L_Nome}")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.ui.Tab_Usuarios.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_users(id)           

            self.Table_users()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EXCLUIR")
            msg.setText(result)
            msg.exec()

            db.close_connect()
       
        
    def Table_users(self):
        self.ui.Tab_Usuarios.setColumnWidth(0, 70)
        self.ui.Tab_Usuarios.setColumnWidth(1, 70)
        self.ui.Tab_Usuarios.setColumnWidth(2, 170)
        self.ui.Tab_Usuarios.setColumnWidth(3, 100)
        self.ui.Tab_Usuarios.setColumnWidth(4, 100)
        self.ui.Tab_Usuarios.setColumnWidth(5, 100)
        self.ui.Tab_Usuarios.setColumnWidth(6, 100)
        self.ui.Tab_Usuarios.setColumnWidth(7, 100)

        db = Data_Base()
        db.connect()
        coletar = db.select_all_users()
        
        self.ui.Tab_Usuarios.contextMenuPolicy()
        self.ui.Tab_Usuarios.clearContents()
        # self.ui.Tab_Usuarios.setRowCount(len(coletar))

        if not coletar: #== "":
            pass
        else:
            self.ui.Tab_Usuarios.setRowCount(len(coletar))
            for row, text in enumerate(coletar):

                for column, data in enumerate(text):
                    self.ui.Tab_Usuarios.setItem(row, column, QTableWidgetItem(str(data)))
        db.close_connect()

    def Carrega(self):
        #self.di = Calendario()
        self.dd = Data()
        d = str(self.dd.Cal.Calendario.selectedDate())
        self.Form = d[21:32]
        #self.dd.diaFormat = self.dd.Funcao()
        self.ui.L_Data.setText(self.Form)  #(self.diaFormat)
        print(self.Form)

    def Dia(self):
        self.Dat = Data()   #(self.user,self.autenticado)
        self.Dat.show ()
        self.Carrega()

# class Data(QDialog):
#     def __init__(self,*args,**argvs):
#         super(Data, self).__init__(*args,**argvs)
#         self.Cal = Calendario()
#         self.Cal.setupUi(self)
#         self.setWindowTitle("Mk.Cosmeticos")
#         appIcon = QIcon(u"/imagens/Fundo.png")
#         self.setWindowIcon(appIcon)
        
#         #self.user = user
#         #self.autenticado = autenticado
#         self.Cal.Calendario.selectionChanged.connect(self.Funcao)
#         self.ui = Ui_Usuarios()
        
        
#     def Funcao(self):
#         #ge = Clients(user=self.user,autenticado=self.autenticado)
#         self.dia = str(self.Cal.Calendario.selectedDate())
#         diaFormat = self.dia[21:32]
#         self.Cal.data.setText(diaFormat)
#         #ge.ui.L_Data = self.dia[21:32]
#         #ge.ui.L_Data.__setattr__(day,self.dia[21:32])
#         #self.ui.L_Data = self.diaFormat
#         #self.ui.L_Data = self.dia[21:32]
#         #ge.ui.L_Data.setText(str(self.dia[21:32]))
#         return diaFormat
#         #print(ge.ui.L_Data)
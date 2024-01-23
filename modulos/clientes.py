from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow,QLineEdit
from PySide2.QtCore import QCoreApplication, QEvent
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from PySide2.QtPrintSupport import *
import os,sys
from modulos.calendario import Data
#from template.Calendario import Calendario
from template.Clientes import Ui_Clientes
from DataBase.DbClientes import Data_Base


class Clients(QDialog):
    def __init__(self,user,autenticado,diaFormat,*args,**argvs):
        super(Clients, self).__init__(*args,**argvs)
        self.ui = Ui_Clientes()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/Fundo.png")
        self.setWindowIcon(appIcon)

        self.ui.L_Id.isEnabled = False
                        
        self.Tab_Cliente()
        self.table_clients()
        #self.Carrega()
        self.ui.btn_Salvar.clicked.connect(self.Cadastrar_Clientes)
        self.ui.btn_Editar.clicked.connect(self.Edita_Clientes)
        self.ui.btn_Limpar.clicked.connect(self.Limpar)
        self.ui.btn_Excluir.clicked.connect(self.Deletar_Clientes)
        self.ui.btn_Calendario.clicked.connect(self.Dia)
        self.ui.btn_Voltar.clicked.connect(self.AbrirMenu)       
        self.ui.L_Data
        self.diaFormat = diaFormat
        self.user = user
        self.autenticado = autenticado
    
        self.ui.Tab_CadClientes.itemSelectionChanged.connect(self.PreencherCampos_Automaticamente)
        #self.dd.Cal.Calendario.selectionChanged.connect(self.dd.Funcao)


    def Carrega(self):
        #self.di = Calendario()
        self.dd = Data()
        d = str(self.dd.Cal.Calendario.selectedDate())
        self.Form = d[21:33]
        #self.dd.diaFormat = self.dd.Funcao()
        self.ui.L_Data.setText(self.Form)  #(self.diaFormat)
        print(self.Form)
        

    def AbrirMenu(self):
        from modulos.menu import Start
        self.menu = Start(user=(self.user),autenticado=(self.autenticado),diaFormat=self.diaFormat)
        self.menu.show()
        self.close()
        
 
    def PegaSelecaoDaTabela(self):  # pega id seleção da tabela
        valor = self.ui.Tab_CadClientes.item(self.PegaSelecaoDoBanco(), 0) 
        return valor.text() if not valor is None else valor  #deve retornar valor str não memoria

    def PegaSelecaoDoBanco(self):  # pega id seleção do banco
        return self.ui.Tab_CadClientes.currentRow() 

#--------------------------------   CARREGA CAMPOS COM DADOS DA TABELA   ----------------------------------

    def PreencherCampos_Automaticamente(self):
        IdLinhaSelecionada = self.PegaSelecaoDoBanco()

        if self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 0) != None:
            id = self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 0).text()
            self.ui.L_Id.setText(id)

        if self.ui.Tab_CadClientes.item(IdLinhaSelecionada,1) != None:
            data = self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 1).text()
            self.ui.L_Data.setText(data)

        if self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 2) != None:
            nome = self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 2).text()
            self.ui.L_Nome.setText(nome)

        if self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 3) != None:
            telefone = self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 3).text()
            self.ui.L_Telefone.setText(telefone)

        if self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 4) != None:
            endereco = self.ui.Tab_CadClientes.item(IdLinhaSelecionada, 4).text()
            self.ui.L_Endereco.setText(endereco)
        

    def Dia(self):
        self.Dat = Data(diaFormat=self.diaFormat)   #(self.user,self.autenticado)
        self.Dat.show ()
        self.Carrega()


    def Tab_Cliente(self):
        db = Data_Base()
        db.connect()
        db.Create_Table_Clientes()
        db.close_connect()
    

    def Cadastrar_Clientes(self):

        """ db = Data_Base()
        db.connect()

        fullDataSet =(
            
            self.ui.L_Data.text(), self.ui.L_Nome.text(), self.ui.L_Telefone.text(), self.ui.L_Endereco.text()            
        ) """
        #id = self.ui.L_Id.text()
        data = self.ui.L_Data.text()
        nome = self.ui.L_Nome.text()
        fone = self.ui.L_Telefone.text()
        endereco = self.ui.L_Endereco.text()

        # if id == "":
        #     QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
        #     return
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
        
        else:

            db = Data_Base()
            db.connect()

            fullDataSet =(
                
                data, nome, fone, endereco             
            )

            resp = db.Register_Clientes(fullDataSet)

    
            if resp == "OK":
                QMessageBox.information(QMessageBox(),"Cadastro de Clientes","Cadastro Realizado com Sucesso!")            
                db.close_connect()
                self.Limpar()
                self.table_clients()       
                return

            else:
                QMessageBox.information(QMessageBox(),"Cadastro de Clientes","Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
                db.close_connect()
                return
        
        
    def Edita_Clientes(self):

        a= self.ui.L_Id.text()
        b = self.ui.L_Data.text()
        c = self.ui.L_Nome.text()
        d = self.ui.L_Telefone.text()
        e = self.ui.L_Endereco.text()
        
        db = Data_Base()
        db.connect()

        fullDataSet =(
            
            a, b, c, d, e             
        )

        resp = db.Update_Clientes(fullDataSet)
  
        if resp == "OK":

            self.table_clients()
            self.Limpar()
            QMessageBox.information(QMessageBox(),"Editar","Dados Editados com Sucesso!")          
            db.close_connect()

        else:
            QMessageBox.information(QMessageBox(),"Editar","Erro ao Editar, verifique se as informações foram preenchidas corretamente!")
            db.close_connect()
            
        
    def Deletar_Clientes(self):
        db = Data_Base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("EXCLUIR")
        msg.setText("Este registro sera Excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.ui.Tab_CadClientes.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.Delete_Clientes(id)           

            self.table_clients()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EXCLUIR")
            msg.setText(result)
            msg.exec()

            db.close_connect()
            

    def Limpar(self):

        self.ui.L_Id.setText("") 
        self.ui.L_Data.setText("")
        self.ui.L_Nome.setText("")
        self.ui.L_Telefone.setText("")
        self.ui.L_Endereco.setText("")

##################################   TABELA   ########################################################

    def table_clients(self):

        self.ui.Tab_CadClientes.setColumnWidth(0, 70)
        self.ui.Tab_CadClientes.setColumnWidth(1, 70)
        self.ui.Tab_CadClientes.setColumnWidth(2, 190)
        self.ui.Tab_CadClientes.setColumnWidth(3, 100)
        self.ui.Tab_CadClientes.setColumnWidth(4, 230)

        db = Data_Base()
        db.connect()
        coletar = db.Select_All_Clientes()
        self.ui.Tab_CadClientes.clearContents()        
        self.ui.Tab_CadClientes.setRowCount(len(coletar))

        for row, text in enumerate(coletar):

            for column, data in enumerate(text):
                self.ui.Tab_CadClientes.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connect()


    def Carregadados(self):
        db = Data_Base
        db.connect()

        lista = db.Select_All_Clientes()
        self.ui.Tab_CadClientes.clearContents()

        self.ui.Tab_CadClientes.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.Tab_CadClientes.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.Tab_CadClientes.setItem(linha,coluna_n,QTableWidgetItem(str(dados)))

        db.close_connect()


# #--------------------------------------    CALENDARIO    -------------------------------
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
#         self.ui = Ui_Clientes()
        
        
#     def Funcao(self):
#         #ge = Clients(user=self.user,autenticado=self.autenticado)
#         self.dia = str(self.Cal.Calendario.selectedDate())
#         diaFormat = self.dia[21:33]
#         self.Cal.data.setText(diaFormat)
#         #ge.ui.L_Data = self.dia[21:32]
#         #ge.ui.L_Data.__setattr__(day,self.dia[21:32])
#         #self.ui.L_Data = self.diaFormat
#         #self.ui.L_Data = self.dia[21:32]
#         #ge.ui.L_Data.setText(str(self.dia[21:32]))
#         return diaFormat
#         #print(ge.ui.L_Data)
    
    
        
              
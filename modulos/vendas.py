from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
import os,sys
from template.Vendas import Ui_Vendas
from modulos.calendario import Data
import sqlite3
from DataBase.DbVendas import Data_Base

class Vendas(QDialog):
    def __init__(self,user,autenticado,*args,**argvs):
        super(Vendas, self).__init__(*args,**argvs)
        self.ui = Ui_Vendas()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/MLogo.png")
        self.setWindowIcon(appIcon)
        
        self.ui.L_Id.isEnabled = False
                        
        self.Tab_Vendas()
        self.table_Vendas()
        #self.Carrega()
        self.ui.btn_CadCliente.clicked.connect(self.Cadastrar_Vendas)
        #self.ui.btn_Editar.clicked.connect(self.Edita_Vendas)
        self.ui.btn_Limpar.clicked.connect(self.Limpar)
        self.ui.btn_Excluir.clicked.connect(self.Deletar_Vendas)
        self.ui.btn_Data.clicked.connect(self.Dia)
        self.ui.btn_Voltar.clicked.connect(self.AbrirMenu)       
        #self.ui.L_Data

        self.user = user
        self.autenticado = autenticado
    
        self.ui.Tab_Caixa_Vendas.itemSelectionChanged.connect(self.PreencherCampos_Automaticamente)
        #self.dd.Cal.Calendario.selectionChanged.connect(self.dd.Funcao)


    def Carrega(self):
        #self.di = Calendario()
        self.dd = Data()
        d = str(self.dd.Cal.Calendario.selectedDate())
        self.Form = d[21:32]
        #self.dd.diaFormat = self.dd.Funcao()
        self.ui.L_Data.setText(self.Form)  #(self.diaFormat)
        print(self.Form)
        

    def AbrirMenu(self):
        from modulos.menu import Start
        self.menu = Start(user=(self.user),autenticado=(self.autenticado))
        self.menu.show()
        self.close()
        
 
    def PegaSelecaoDaTabela(self):  # pega id seleção da tabela
        valor = self.ui.Tab_Caixa_Vendas.item(self.PegaSelecaoDoBanco(), 0) 
        return valor.text() if not valor is None else valor  #deve retornar valor str não memoria

    def PegaSelecaoDoBanco(self):  # pega id seleção do banco
        return self.ui.Tab_Caixa_Vendas.currentRow() 

#--------------------------------   CARREGA CAMPOS COM DADOS DA TABELA   ----------------------------------

    def PreencherCampos_Automaticamente(self):
        IdLinhaSelecionada = self.PegaSelecaoDoBanco()

        if self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 0) != None:
            id = self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 0).text()
            self.ui.L_Id.setText(id)

        if self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada,1) != None:
            data = self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 1).text()
            self.ui.L_Data.setText(data)

        if self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 2) != None:
            nome = self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 2).text()
            self.ui.L_Nome.setText(nome)

        if self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 3) != None:
            telefone = self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 3).text()
            self.ui.L_Telefone.setText(telefone)

        if self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 4) != None:
            endereco = self.ui.Tab_Caixa_Vendas.item(IdLinhaSelecionada, 4).text()
            self.ui.L_Endereco.setText(endereco)
        

    def Dia(self):
        self.Dat = Data()   #(self.user,self.autenticado)
        self.Dat.show ()
        self.Carrega()


    def Tab_Vendas(self):
        db = Data_Base()
        db.connect()
        db.Create_Table_Vendas()
        db.close_connect()
    

    def Cadastrar_Vendas(self):

        """ db = Data_Base()
        db.connect()

        fullDataSet =(
            
            self.ui.L_Data.text(), self.ui.L_Nome.text(), self.ui.L_Telefone.text(), self.ui.L_Endereco.text()            
        ) """
        id = self.ui.L_Id.text()
        data = self.ui.L_Data.text()
        nome = self.ui.Cbb_nome.currentText()
        prod = self.ui.Cbb_Produto.currentText()
        pag = self.ui.Cbb_Pag.currentText()
        quant = self.ui.L_Quat.text()
        preco = self.ui.L_Valor.text()

        if id == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif data == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif nome == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif prod == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif pag == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif quant == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif preco == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        
        else:

            db = Data_Base()
            db.connect()

            fullDataSet =(
                
                id, data, nome, prod, pag, quant, preco            
            )

            resp = db.Register_Vendas(fullDataSet)

    
            if resp == "OK":
                QMessageBox.information(QMessageBox(),"Cadastro de Vendas","Cadastro Realizado com Sucesso!")            
                db.close_connect()
                self.table_clients()       
                return

            else:
                QMessageBox.information(QMessageBox(),"Cadastro de Vendas","Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
                db.close_connect()
                return
        
        
    def Edita_Vendas(self):

        id = self.ui.L_Id.text()
        data = self.ui.L_Data.text()
        nome = self.ui.Cbb_nome.currentText()
        prod = self.ui.Cbb_Produto.currentText()
        pag = self.ui.Cbb_Pag.currentText()
        quant = self.ui.L_Quat.text()
        preco = self.ui.L_Valor.text()
        
        db = Data_Base()
        db.connect()

        fullDataSet =(
            
            id, data, nome, prod, pag, quant, preco            
        )

        resp = db.Update_Vendas(fullDataSet)
  
        if resp == "OK":

            self.table_clients()
            self.Limpar()
            QMessageBox.information(QMessageBox(),"Editar","Dados Editados com Sucesso!")          
            db.close_connect()

        else:
            QMessageBox.information(QMessageBox(),"Editar","Erro ao Editar, verifique se as informações foram preenchidas corretamente!")
            db.close_connect()
            
        
    def Deletar_Vendas(self):
        db = Data_Base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("EXCLUIR")
        msg.setText("Este registro sera Excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.ui.Tab_Caixa_Vendas.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.Delete_Vendas(id)           

            self.table_clients()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EXCLUIR")
            msg.setText(result)
            msg.exec()

            db.close_connect()
            

    def Limpar(self):

        id = self.ui.L_Id.setText("")
        data = self.ui.L_Data.setText("")
        nome = self.ui.Cbb_nome.setCurrentText("")
        prod = self.ui.Cbb_Produto.setCurrentText("")
        pag = self.ui.Cbb_Pag.setCurrentText("")
        quant = self.ui.L_Quat.setText("")
        preco = self.ui.L_Valor.setText("")

##################################   TABELA   ########################################################

    def table_Vendas(self):

        self.ui.Tab_Caixa_Vendas.setColumnWidth(0, 70)
        self.ui.Tab_Caixa_Vendas.setColumnWidth(1, 70)
        self.ui.Tab_Caixa_Vendas.setColumnWidth(2, 190)
        self.ui.Tab_Caixa_Vendas.setColumnWidth(3, 100)
        self.ui.Tab_Caixa_Vendas.setColumnWidth(4, 230)
        self.ui.Tab_Caixa_Vendas.setColumnWidth(5, 230)
        self.ui.Tab_Caixa_Vendas.setColumnWidth(6, 230)

        db = Data_Base()
        db.connect()
        coletar = db.Select_All_Vendas()
        self.ui.Tab_Caixa_Vendas.clearContents()        
        self.ui.Tab_Caixa_Vendas.setRowCount(len(coletar))

        for row, text in enumerate(coletar):

            for column, data in enumerate(text):
                self.ui.Tab_Caixa_Vendas.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connect()


    def Carregadados(self):
        db = Data_Base
        db.connect()

        lista = db.Select_All_Vendas()
        self.ui.Tab_Caixa_Vendas.clearContents()

        self.ui.Tab_Caixa_Vendas.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.Tab_Caixa_Vendas.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.Tab_Caixa_Vendas.setItem(linha,coluna_n,QTableWidgetItem(str(dados)))

        db.close_connect()


#--------------------------------------    CALENDARIO    -------------------------------
class Data(QDialog):
    def __init__(self,*args,**argvs):
        super(Data, self).__init__(*args,**argvs)
        self.Cal = Calendario()
        self.Cal.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"/imagens/Fundo.png")
        self.setWindowIcon(appIcon)
        self.Cal.Calendario.selectionChanged.connect(self.Funcao)       
        
    def Funcao(self):
        self.dia = str(self.Cal.Calendario.selectedDate())
        diaFormat = self.dia[21:33]
        self.Cal.data.setText(diaFormat)       
        return diaFormat
        
    
    
        
              
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
import os,sys
from template.Compras import Ui_Compras
from modulos.calendario import Data
import sqlite3
from DataBase.DbCompras import Data_Base

class Comp(QDialog):
    def __init__(self,user,autenticado,*args,**argvs):
        super(Comp, self).__init__(*args,**argvs)
        self.ui = Ui_Compras()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/Fundo.png")
        self.setWindowIcon(appIcon)
        
        self.ui.L_Id.isEnabled = False
                        
        self.Tab_Compras()
        self.table_Compras()
        #self.Carrega()
        self.ui.btn_Salvar.clicked.connect(self.Cadastrar_Compras)
        self.ui.btn_Editar.clicked.connect(self.Edita_Compras)
        self.ui.btn_Limpar.clicked.connect(self.Limpar)
        self.ui.btn_Excluir.clicked.connect(self.Deletar_Compras)
        self.ui.btn_Data.clicked.connect(self.Dia)
        self.ui.Btn_Voltar.clicked.connect(self.AbrirMenu)       
        self.ui.Btn_Clientes.clicked.connect(self.Clientes)
        self.ui.Btn_Produtos.clicked.connect(self.Produto)
        self.ui.Btn_Vendas.clicked.connect(self.Vendas)
        
        self.user = user
        self.autenticado = autenticado
    
        self.ui.Tab_Transacoes.itemSelectionChanged.connect(self.PreencherCampos_Automaticamente)
        #self.dd.Cal.Calendario.selectionChanged.connect(self.dd.Funcao)


    def Carrega(self):
        #self.di = Calendario()
        self.dd = Data()
        d = str(self.dd.Cal.Calendario.selectedDate())
        self.Form = d[21:32]
        #self.dd.diaFormat = self.dd.Funcao()
        self.ui.L_Data.setText(self.Form)  #(self.diaFormat)
        

    def AbrirMenu(self):
        from modulos.menu import Start
        self.menu = Start(user=(self.user),autenticado=(self.autenticado))
        self.menu.show()
        self.close()

    def Clientes(self):
        from modulos.clientes import Clients
        self.Cli = Clients(user=(self.user),autenticado=(self.autenticado))
        self.Cli.show()
        self.close()

    def Produto(self):
        from modulos.produtos import Prod
        self.Pro = Prod(user=(self.user),autenticado=(self.autenticado))
        self.Pro.show()
        self.close()

    def Vendas(self):
        from modulos.vendas import Vendas
        self.Ven = Vendas(user=(self.user),autenticado=(self.autenticado))
        self.Ven.show()
        self.close()
        
 
    def PegaSelecaoDaTabela(self):  # pega id seleção da tabela
        valor = self.ui.Tab_Transacoes.item(self.PegaSelecaoDoBanco(), 0) 
        return valor.text() if not valor is None else valor  #deve retornar valor str não memoria

    def PegaSelecaoDoBanco(self):  # pega id seleção do banco
        return self.ui.Tab_Transacoes.currentRow() 

#--------------------------------   CARREGA CAMPOS COM DADOS DA TABELA   ----------------------------------

    def PreencherCampos_Automaticamente(self):
        IdLinhaSelecionada = self.PegaSelecaoDoBanco()

        if self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 0) != None:
            id = self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 0).text()
            self.ui.L_Id.setText(id)

        if self.ui.Tab_Transacoes.item(IdLinhaSelecionada,1) != None:
            data = self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 1).text()
            self.ui.L_Data.setText(data)

        if self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 2) != None:
            produto = self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 2).text()
            self.ui.Cbb_Produto.setCurrentText(produto)

        if self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 3) != None:
            tipo = self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 3).text()
            self.ui.Cbb_Tipo.setCurrentText(tipo)

        if self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 4) != None:
            quantidade = self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 4).text()
            self.ui.L_Quantidade.setText(quantidade)
        
        if self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 5) != None:
            custo = self.ui.Tab_Transacoes.item(IdLinhaSelecionada, 5).text()
            self.ui.L_Valor.setText(custo)
        

    def Dia(self):
        self.Dat = Data()   #(self.user,self.autenticado)
        self.Dat.show ()
        self.Carrega()


    def Tab_Compras(self):
        db = Data_Base()
        db.connect()
        db.Create_Table_Compras()
        db.close_connect()
    

    def Cadastrar_Compras(self):

        data = self.ui.L_Data.text()
        produto = self.ui.Cbb_Produto.currentText()
        tipo = self.ui.Cbb_Tipo.currentText()
        quantidade = self.ui.L_Quantidade.text()
        custo = self.ui.L_Valor.text()

        
        if data == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif produto == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif tipo == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif quantidade == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif custo == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        
        else:

            db = Data_Base()
            db.connect()

            fullDataSet =(
                
                data, produto, tipo, quantidade, custo            
            )

            resp = db.Register_Compras(fullDataSet)

    
            if resp == "OK":
                self.table_Compras()
                self.Limpar() 
                QMessageBox.information(QMessageBox(),"Cadastro de Compras","Cadastro Realizado com Sucesso!")       
                db.close_connect()
                return

            else:
                QMessageBox.information(QMessageBox(),"Cadastro de Compras","Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
                db.close_connect()
                return

        
    def Edita_Compras(self):

        id = self.ui.L_Id.text()
        data = self.ui.L_Data.text()
        produto = self.ui.Cbb_Produto.currentText()
        tipo = self.ui.Cbb_Tipo.currentText()
        quantidade = self.ui.L_Quantidade.text()
        custo = self.ui.L_Valor.text()
        
        db = Data_Base()
        db.connect()

        fullDataSet =(
            
            id, data, produto, tipo, quantidade, custo          
        )

        resp = db.Update_Compras(fullDataSet)
  
        if resp == "OK":
            self.table_Compras()
            self.Limpar()            
            QMessageBox.information(QMessageBox(),"Editar","Dados Editados com Sucesso!")
            db.close_connect()
                        
        else:
            QMessageBox.information(QMessageBox(),"Editar","Erro ao Editar, verifique se as informações foram preenchidas corretamente!")
            db.close_connect()


    def Deletar_Compras(self):
        db = Data_Base()
        db.connect()

        id = self.ui.Tab_Transacoes.selectionModel().currentIndex().siblingAtColumn(0).data()
        msg = QMessageBox()
        msg.setWindowTitle("EXCLUIR")
        msg.setText("Este registro sera Excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir id ?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            
            result = db.Delete_Compras(id)           

            self.table_Compras()
            self.Limpar()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EXCLUIR")
            msg.setText(result)
            msg.exec()

            db.close_connect()
            

    def Limpar(self):

        self.ui.L_Id.setText("")
        self.ui.L_Data.setText("")
        self.ui.Cbb_Produto.setCurrentText("")
        self.ui.Cbb_Tipo.setCurrentText("")
        self.ui.L_Quantidade.setText("")
        self.ui.L_Valor.setText("")

##################################   TABELA   ########################################################

    def table_Compras(self):

        self.ui.Tab_Transacoes.setColumnWidth(0, 50)
        self.ui.Tab_Transacoes.setColumnWidth(1, 100)
        self.ui.Tab_Transacoes.setColumnWidth(2, 300)
        self.ui.Tab_Transacoes.setColumnWidth(3, 140)
        self.ui.Tab_Transacoes.setColumnWidth(4, 125)
        self.ui.Tab_Transacoes.setColumnWidth(5, 70)

        db = Data_Base()
        db.connect()
        coletar = db.Select_All_Compras()
        self.ui.Tab_Transacoes.clearContents()        
        self.ui.Tab_Transacoes.setRowCount(len(coletar))

        for row, text in enumerate(coletar):

            for column, data in enumerate(text):
                self.ui.Tab_Transacoes.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connect()


    def Carregadados(self):
        db = Data_Base
        db.connect()

        lista = db.Select_All_Compras()
        self.ui.Tab_Transacoes.clearContents()

        self.ui.Tab_Transacoes.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.Tab_Transacoes.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.Tab_Transacoes.setItem(linha,coluna_n,QTableWidgetItem(str(dados)))

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
#         #self.ui = Ui_Comprass()   TIRAR COMENTARIO
        
        
#     def Funcao(self):
#         #ge = Compras(user=self.user,autenticado=self.autenticado)
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
    
    
        
              
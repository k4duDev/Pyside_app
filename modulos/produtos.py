from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMainWindow
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtPrintSupport import *
import os,sys
from template.Produtos import Ui_Produtos
from DataBase.DbProduto import Data_Base


class Prod(QDialog):
    def __init__(self,user,autenticado,*args,**argvs):
        super(Prod, self).__init__(*args,**argvs)
        self.ui = Ui_Produtos()
        self.ui.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"C:/Projetos de Aplicativos/Mk.Cosmeticos/imagens/Fundo.png")
        self.setWindowIcon(appIcon)
        
        self.ui.L_Id.isEnabled = False
                                        
        self.Tab_Produto()
        self.Dados()
        self.table_Produto()
        #self.Carregadados()
        

        
        self.ui.btn_Adicionar.clicked.connect(self.Cadastrar_Produto)
        self.ui.btn_Editar.clicked.connect(self.Edita_Produto)
        self.ui.btn_Limpar.clicked.connect(self.Limpar)
        self.ui.btn_Excluir.clicked.connect(self.Deletar_Produto)
        self.ui.btn_Voltar.clicked.connect(self.AbrirMenu)       
        
        self.user = user
        self.autenticado = autenticado
    
        self.ui.Tab_Produto.itemSelectionChanged.connect(self.PreencherCampos_Automaticamente)


    def AbrirMenu(self):
        from modulos.menu import Start
        self.menu = Start(user=(self.user),autenticado=(self.autenticado))
        self.menu.show()
        self.close()
        
 
    def PegaSelecaoDaTabela(self):  # pega id seleção da tabela
        valor = self.ui.Tab_Produto.item(self.PegaSelecaoDoBanco(), 0) 
        return valor.text() if not valor is None else valor  #deve retornar valor str não memoria

    def PegaSelecaoDoBanco(self):  # pega id seleção do banco
        return self.ui.Tab_Produto.currentRow() 

#--------------------------------   CARREGA CAMPOS COM DADOS DA TABELA   ----------------------------------

    def PreencherCampos_Automaticamente(self):
        IdLinhaSelecionada = self.PegaSelecaoDoBanco()

        if self.ui.Tab_Produto.item(IdLinhaSelecionada, 0) != None:
            codigo = self.ui.Tab_Produto.item(IdLinhaSelecionada, 0).text()
            self.ui.L_Codigo.setText(codigo)

        if self.ui.Tab_Produto.item(IdLinhaSelecionada, 1) != None:
            id = self.ui.Tab_Produto.item(IdLinhaSelecionada, 1).text()
            self.ui.L_Id.setText(id)
        
        if self.ui.Tab_Produto.item(IdLinhaSelecionada, 2) != None:
            produto = self.ui.Tab_Produto.item(IdLinhaSelecionada, 2).text()
            self.ui.L_Produto.setText(produto)

        if self.ui.Tab_Produto.item(IdLinhaSelecionada, 3) != None:
            tipo = self.ui.Tab_Produto.item(IdLinhaSelecionada, 3).text()
            self.ui.L_Tipo.setText(tipo)

        if self.ui.Tab_Produto.item(IdLinhaSelecionada, 4) != None:
            custo = self.ui.Tab_Produto.item(IdLinhaSelecionada, 4).text()
            self.ui.L_Custo.setText(custo)

        if self.ui.Tab_Produto.item(IdLinhaSelecionada, 5) != None:
            preco = self.ui.Tab_Produto.item(IdLinhaSelecionada, 5).text()
            self.ui.L_Preco.setText(preco)


    def Tab_Produto(self):
        db = Data_Base()
        db.connect()
        db.Create_Table_Produto()
        dados = db.Select_All_Dados()
        if not dados:
            db.Atualiza()
        db.close_connect()
        #self.Banco()
    

    def Cadastrar_Produto(self):

        """ db = Data_Base()
        db.connect()

        fullDataSet =(
            
            self.ui.L_IdCompra.text(), self.ui.L_Produto.text(), self.ui.L_Custo.text(), self.ui.L_Preco.text()            
        ) """
        id = self.ui.L_Id.text()
        produto = self.ui.L_Produto.text()
        tipo = self.ui.L_Tipo.text()
        custo = self.ui.L_Custo.text()
        preco = self.ui.L_Preco.text()

        if id == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif produto == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif tipo == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif custo == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        elif preco == "":
            QMessageBox.warning(QMessageBox(),"ERRO", "Preencha os Campos Vazios!" )
            return
        
        else:

            db = Data_Base()
            db.connect()

            fullDataSet =(
                
                id, produto, tipo, custo, preco             
            )

            resp = db.Register_Produto(fullDataSet)

    
            if resp == "OK":
                QMessageBox.information(QMessageBox(),"Cadastro de Produto","Cadastro Realizado com Sucesso!")            
                db.close_connect()
                self.table_Produto()       
                return

            else:
                QMessageBox.information(QMessageBox(),"Cadastro de Produto","Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
                db.close_connect()
                return
        
        
    def Edita_Produto(self):

        codigo= self.ui.L_Codigo.text()
        id = self.ui.L_Id.text()
        produto = self.ui.L_Produto.text()
        tipo = self.ui.L_Tipo.text()
        custo = self.ui.L_Custo.text()
        preco = self.ui.L_Preco.text()
        
        db = Data_Base()
        db.connect()

        fullDataSet =(
            
            codigo, id, produto, tipo, custo, preco           
        )

        resp = db.Update_Produto(fullDataSet)
  
        if resp == "OK":

            self.table_Produto()
            self.Limpar()
            QMessageBox.information(QMessageBox(),"Editar","Dados Editados com Sucesso!")          
            db.close_connect()

        else:
            QMessageBox.information(QMessageBox(),"Editar","Erro ao Editar, verifique se as informações foram preenchidas corretamente!")
            db.close_connect()
            
        
    def Deletar_Produto(self):
        db = Data_Base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("EXCLUIR")
        msg.setText("Este registro sera Excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            codigo = self.ui.Tab_Produto.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.Delete_Produto(codigo)           

            self.table_Produto()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EXCLUIR")
            msg.setText(result)
            msg.exec()

            db.close_connect()


    def Dados(self):
        
        db = Data_Base()
        db.connect()
               
        lista = db.Select_All_ComprasProdutos()
        dados = db.Select_All_Dados()

        for i,idi in enumerate(dados):
            pass
        for x,Idi in enumerate(lista):
            if x > i:
                novalista = []
                novalista.append(Idi)
                id = novalista[0][0]
                produto = novalista[0][1]
                tipo = novalista[0][2]
                custo = novalista[0][3]
                db.Insert_Produto(id,produto,tipo,custo)


    def Limpar(self):

        self.ui.L_Codigo.setText("") 
        self.ui.L_Id.setText("")
        self.ui.L_Produto.setText("")
        self.ui.L_Tipo.setText("")
        self.ui.L_Custo.setText("")
        self.ui.L_Preco.setText("")

##################################   TABELA   ########################################################

    def table_Produto(self):
        #from DataBase.DbCompras import Data_Base

        self.ui.Tab_Produto.setColumnWidth(0, 90)
        self.ui.Tab_Produto.setColumnWidth(1, 50)
        self.ui.Tab_Produto.setColumnWidth(2, 190)
        self.ui.Tab_Produto.setColumnWidth(3, 70)
        self.ui.Tab_Produto.setColumnWidth(4, 70)
        self.ui.Tab_Produto.setColumnWidth(5, 70)

        db = Data_Base()
        db.connect()
        coletar = db.Select_All_Produto()

        self.ui.Tab_Produto.clearContents()        
        self.ui.Tab_Produto.setRowCount(len(coletar))

        for row, text in enumerate(coletar):

            for column, data in enumerate(text):
                self.ui.Tab_Produto.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connect()


    def Carregadados(self):

        db = Data_Base
        db.connect()

        lista = db.Select_All_Produto()
        self.ui.Tab_Produto.clearContents()

        self.ui.Tab_Produto.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.Tab_Produto.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.Tab_Produto.setItem(linha,coluna_n,QTableWidgetItem(str(dados)))

        db.close_connect()


    
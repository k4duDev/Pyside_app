# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Compras.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Compras(object):
    def setupUi(self, Compras):
        if not Compras.objectName():
            Compras.setObjectName(u"Compras")
        Compras.resize(825, 598)
        Compras.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.gridLayout_7 = QGridLayout(Compras)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Btn_Voltar = QPushButton(Compras)
        self.Btn_Voltar.setObjectName(u"Btn_Voltar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Voltar.sizePolicy().hasHeightForWidth())
        self.Btn_Voltar.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Voltar.setFont(font)
        self.Btn_Voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Voltar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 127);\n"
"   border-radius: 0px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(206, 206, 206);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/image/imagens/voltar1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Voltar.setIcon(icon)
        self.Btn_Voltar.setIconSize(QSize(80, 45))

        self.gridLayout.addWidget(self.Btn_Voltar, 0, 0, 1, 1)

        self.label = QLabel(Compras)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Btn_Clientes = QPushButton(Compras)
        self.Btn_Clientes.setObjectName(u"Btn_Clientes")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Btn_Clientes.sizePolicy().hasHeightForWidth())
        self.Btn_Clientes.setSizePolicy(sizePolicy2)
        self.Btn_Clientes.setFont(font)
        self.Btn_Clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Clientes.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/image/imagens/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Clientes.setIcon(icon1)
        self.Btn_Clientes.setIconSize(QSize(45, 45))

        self.gridLayout_4.addWidget(self.Btn_Clientes, 0, 0, 1, 1)

        self.Btn_Produtos = QPushButton(Compras)
        self.Btn_Produtos.setObjectName(u"Btn_Produtos")
        sizePolicy2.setHeightForWidth(self.Btn_Produtos.sizePolicy().hasHeightForWidth())
        self.Btn_Produtos.setSizePolicy(sizePolicy2)
        self.Btn_Produtos.setFont(font)
        self.Btn_Produtos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Produtos.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/image/imagens/Produtos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Produtos.setIcon(icon2)
        self.Btn_Produtos.setIconSize(QSize(45, 45))

        self.gridLayout_4.addWidget(self.Btn_Produtos, 0, 1, 1, 1)

        self.Btn_Vendas = QPushButton(Compras)
        self.Btn_Vendas.setObjectName(u"Btn_Vendas")
        sizePolicy2.setHeightForWidth(self.Btn_Vendas.sizePolicy().hasHeightForWidth())
        self.Btn_Vendas.setSizePolicy(sizePolicy2)
        self.Btn_Vendas.setFont(font)
        self.Btn_Vendas.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Vendas.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/image/imagens/vendas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Vendas.setIcon(icon3)
        self.Btn_Vendas.setIconSize(QSize(45, 45))

        self.gridLayout_4.addWidget(self.Btn_Vendas, 0, 2, 1, 1)

        self.btn_Salvar = QPushButton(Compras)
        self.btn_Salvar.setObjectName(u"btn_Salvar")
        sizePolicy2.setHeightForWidth(self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_Salvar.setFont(font2)
        self.btn_Salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 255, 0);\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/image/imagens/guardar-dados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Salvar.setIcon(icon4)
        self.btn_Salvar.setIconSize(QSize(45, 45))

        self.gridLayout_4.addWidget(self.btn_Salvar, 0, 3, 1, 1)

        self.btn_Editar = QPushButton(Compras)
        self.btn_Editar.setObjectName(u"btn_Editar")
        sizePolicy2.setHeightForWidth(self.btn_Editar.sizePolicy().hasHeightForWidth())
        self.btn_Editar.setSizePolicy(sizePolicy2)
        self.btn_Editar.setFont(font2)
        self.btn_Editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Editar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 85, 0);\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/image/imagens/editar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Editar.setIcon(icon5)
        self.btn_Editar.setIconSize(QSize(45, 45))

        self.gridLayout_4.addWidget(self.btn_Editar, 0, 4, 1, 1)

        self.btn_Limpar = QPushButton(Compras)
        self.btn_Limpar.setObjectName(u"btn_Limpar")
        sizePolicy2.setHeightForWidth(self.btn_Limpar.sizePolicy().hasHeightForWidth())
        self.btn_Limpar.setSizePolicy(sizePolicy2)
        self.btn_Limpar.setFont(font2)
        self.btn_Limpar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Limpar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 170, 0);\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/image/imagens/limpar-limpo (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Limpar.setIcon(icon6)
        self.btn_Limpar.setIconSize(QSize(45, 45))

        self.gridLayout_4.addWidget(self.btn_Limpar, 0, 5, 1, 1)

        self.btn_Excluir = QPushButton(Compras)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        sizePolicy2.setHeightForWidth(self.btn_Excluir.sizePolicy().hasHeightForWidth())
        self.btn_Excluir.setSizePolicy(sizePolicy2)
        self.btn_Excluir.setFont(font2)
        self.btn_Excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Excluir.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/image/imagens/excluir-arquivo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Excluir.setIcon(icon7)
        self.btn_Excluir.setIconSize(QSize(45, 45))

        self.gridLayout_4.addWidget(self.btn_Excluir, 0, 6, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.label_3 = QLabel(Compras)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.L_Data = QLineEdit(Compras)
        self.L_Data.setObjectName(u"L_Data")
        sizePolicy2.setHeightForWidth(self.L_Data.sizePolicy().hasHeightForWidth())
        self.L_Data.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(14)
        self.L_Data.setFont(font4)

        self.gridLayout_2.addWidget(self.L_Data, 0, 5, 1, 1)

        self.btn_Data = QPushButton(Compras)
        self.btn_Data.setObjectName(u"btn_Data")
        sizePolicy2.setHeightForWidth(self.btn_Data.sizePolicy().hasHeightForWidth())
        self.btn_Data.setSizePolicy(sizePolicy2)
        self.btn_Data.setFont(font2)
        self.btn_Data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Data.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/image/imagens/calendario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Data.setIcon(icon8)
        self.btn_Data.setIconSize(QSize(45, 45))

        self.gridLayout_2.addWidget(self.btn_Data, 0, 4, 1, 1)

        self.label_8 = QLabel(Compras)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)

        self.L_Id = QLineEdit(Compras)
        self.L_Id.setObjectName(u"L_Id")
        self.L_Id.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.L_Id.sizePolicy().hasHeightForWidth())
        self.L_Id.setSizePolicy(sizePolicy2)
        self.L_Id.setFont(font4)

        self.gridLayout_2.addWidget(self.L_Id, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(Compras)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.Cbb_Produto = QComboBox(Compras)
        self.Cbb_Produto.setObjectName(u"Cbb_Produto")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Cbb_Produto.sizePolicy().hasHeightForWidth())
        self.Cbb_Produto.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setFamily(u"Segoe UI Black")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.Cbb_Produto.setFont(font5)
        self.Cbb_Produto.setEditable(True)

        self.gridLayout_3.addWidget(self.Cbb_Produto, 0, 1, 1, 1)

        self.label_6 = QLabel(Compras)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setFont(font)

        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)

        self.Cbb_Tipo = QComboBox(Compras)
        self.Cbb_Tipo.setObjectName(u"Cbb_Tipo")
        sizePolicy2.setHeightForWidth(self.Cbb_Tipo.sizePolicy().hasHeightForWidth())
        self.Cbb_Tipo.setSizePolicy(sizePolicy2)
        self.Cbb_Tipo.setFont(font5)
        self.Cbb_Tipo.setEditable(True)

        self.gridLayout_3.addWidget(self.Cbb_Tipo, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 4, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(Compras)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.L_Quantidade = QLineEdit(Compras)
        self.L_Quantidade.setObjectName(u"L_Quantidade")
        sizePolicy2.setHeightForWidth(self.L_Quantidade.sizePolicy().hasHeightForWidth())
        self.L_Quantidade.setSizePolicy(sizePolicy2)
        self.L_Quantidade.setFont(font4)

        self.gridLayout_5.addWidget(self.L_Quantidade, 0, 1, 1, 1)

        self.label_7 = QLabel(Compras)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font)

        self.gridLayout_5.addWidget(self.label_7, 0, 2, 1, 1)

        self.L_Valor = QLineEdit(Compras)
        self.L_Valor.setObjectName(u"L_Valor")
        sizePolicy2.setHeightForWidth(self.L_Valor.sizePolicy().hasHeightForWidth())
        self.L_Valor.setSizePolicy(sizePolicy2)
        self.L_Valor.setFont(font4)

        self.gridLayout_5.addWidget(self.L_Valor, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 5, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.Tab_Transacoes = QTableWidget(Compras)
        if (self.Tab_Transacoes.columnCount() < 6):
            self.Tab_Transacoes.setColumnCount(6)
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6);
        self.Tab_Transacoes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        self.Tab_Transacoes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.Tab_Transacoes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.Tab_Transacoes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.Tab_Transacoes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.Tab_Transacoes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.Tab_Transacoes.setObjectName(u"Tab_Transacoes")
        self.Tab_Transacoes.setFont(font4)

        self.gridLayout_7.addWidget(self.Tab_Transacoes, 1, 0, 1, 1)


        self.retranslateUi(Compras)

        QMetaObject.connectSlotsByName(Compras)
    # setupUi

    def retranslateUi(self, Compras):
        Compras.setWindowTitle(QCoreApplication.translate("Compras", u"Dialog", None))
        self.Btn_Voltar.setText("")
        self.label.setText(QCoreApplication.translate("Compras", u"Compras", None))
        self.Btn_Clientes.setText(QCoreApplication.translate("Compras", u"Clientes", None))
        self.Btn_Produtos.setText(QCoreApplication.translate("Compras", u"Produtos", None))
        self.Btn_Vendas.setText(QCoreApplication.translate("Compras", u"Vendas", None))
        self.btn_Salvar.setText(QCoreApplication.translate("Compras", u"Salvar", None))
        self.btn_Editar.setText(QCoreApplication.translate("Compras", u"Editar", None))
        self.btn_Limpar.setText(QCoreApplication.translate("Compras", u"Limpar", None))
        self.btn_Excluir.setText(QCoreApplication.translate("Compras", u"Excluir", None))
        self.label_3.setText(QCoreApplication.translate("Compras", u"Registro de Transa\u00e7\u00f5es", None))
        self.btn_Data.setText("")
        self.label_8.setText(QCoreApplication.translate("Compras", u"ID:", None))
        self.label_4.setText(QCoreApplication.translate("Compras", u"Produto:", None))
        self.label_6.setText(QCoreApplication.translate("Compras", u"Tipo:", None))
        self.label_5.setText(QCoreApplication.translate("Compras", u"Quantidades:", None))
        self.label_7.setText(QCoreApplication.translate("Compras", u"Valor:", None))
        ___qtablewidgetitem = self.Tab_Transacoes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Compras", u"Id", None));
        ___qtablewidgetitem1 = self.Tab_Transacoes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Compras", u"Data", None));
        ___qtablewidgetitem2 = self.Tab_Transacoes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Compras", u"Produtos", None));
        ___qtablewidgetitem3 = self.Tab_Transacoes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Compras", u"Tipo", None));
        ___qtablewidgetitem4 = self.Tab_Transacoes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Compras", u"Quantidade", None));
        ___qtablewidgetitem5 = self.Tab_Transacoes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Compras", u"Valor", None));
    # retranslateUi

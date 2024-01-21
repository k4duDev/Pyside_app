# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vendas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Vendas(object):
    def setupUi(self, Vendas):
        if not Vendas.objectName():
            Vendas.setObjectName(u"Vendas")
        Vendas.resize(842, 558)
        Vendas.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.gridLayout_6 = QGridLayout(Vendas)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.btn_Voltar = QPushButton(Vendas)
        self.btn_Voltar.setObjectName(u"btn_Voltar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Voltar.sizePolicy().hasHeightForWidth())
        self.btn_Voltar.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        self.btn_Voltar.setFont(font)
        self.btn_Voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Voltar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 127);\n"
"   border-radius: 0px\n"
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
        icon = QIcon()
        icon.addFile(u":/image/imagens/voltar1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Voltar.setIcon(icon)
        self.btn_Voltar.setIconSize(QSize(80, 45))

        self.gridLayout_2.addWidget(self.btn_Voltar, 0, 0, 1, 1)

        self.label_2 = QLabel(Vendas)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_Salvar = QPushButton(Vendas)
        self.btn_Salvar.setObjectName(u"btn_Salvar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy2)
        self.btn_Salvar.setFont(font)
        self.btn_Salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet(u"QPushButton{;\n"
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
        icon1.addFile(u":/image/imagens/guardar-dados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Salvar.setIcon(icon1)
        self.btn_Salvar.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.btn_Salvar, 0, 3, 1, 1)

        self.btn_Excluir = QPushButton(Vendas)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        sizePolicy2.setHeightForWidth(self.btn_Excluir.sizePolicy().hasHeightForWidth())
        self.btn_Excluir.setSizePolicy(sizePolicy2)
        self.btn_Excluir.setFont(font)
        self.btn_Excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Excluir.setStyleSheet(u"QPushButton{;\n"
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
        icon2.addFile(u":/image/imagens/excluir-arquivo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Excluir.setIcon(icon2)
        self.btn_Excluir.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.btn_Excluir, 0, 5, 1, 1)

        self.btn_Estoque_2 = QPushButton(Vendas)
        self.btn_Estoque_2.setObjectName(u"btn_Estoque_2")
        sizePolicy2.setHeightForWidth(self.btn_Estoque_2.sizePolicy().hasHeightForWidth())
        self.btn_Estoque_2.setSizePolicy(sizePolicy2)
        self.btn_Estoque_2.setFont(font)
        self.btn_Estoque_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Estoque_2.setStyleSheet(u"QPushButton{\n"
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
        icon3.addFile(u":/image/imagens/Produtos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Estoque_2.setIcon(icon3)
        self.btn_Estoque_2.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.btn_Estoque_2, 0, 2, 1, 1)

        self.btn_CadCliente = QPushButton(Vendas)
        self.btn_CadCliente.setObjectName(u"btn_CadCliente")
        sizePolicy2.setHeightForWidth(self.btn_CadCliente.sizePolicy().hasHeightForWidth())
        self.btn_CadCliente.setSizePolicy(sizePolicy2)
        self.btn_CadCliente.setFont(font)
        self.btn_CadCliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_CadCliente.setStyleSheet(u"QPushButton{\n"
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
        icon4.addFile(u":/image/imagens/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_CadCliente.setIcon(icon4)
        self.btn_CadCliente.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.btn_CadCliente, 0, 0, 1, 1)

        self.btn_Limpar = QPushButton(Vendas)
        self.btn_Limpar.setObjectName(u"btn_Limpar")
        sizePolicy2.setHeightForWidth(self.btn_Limpar.sizePolicy().hasHeightForWidth())
        self.btn_Limpar.setSizePolicy(sizePolicy2)
        self.btn_Limpar.setFont(font)
        self.btn_Limpar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Limpar.setStyleSheet(u"QPushButton{;\n"
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
        icon5.addFile(u":/image/imagens/limpar-limpo (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Limpar.setIcon(icon5)
        self.btn_Limpar.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.btn_Limpar, 0, 7, 1, 1)

        self.btn_Estoque = QPushButton(Vendas)
        self.btn_Estoque.setObjectName(u"btn_Estoque")
        sizePolicy2.setHeightForWidth(self.btn_Estoque.sizePolicy().hasHeightForWidth())
        self.btn_Estoque.setSizePolicy(sizePolicy2)
        self.btn_Estoque.setFont(font)
        self.btn_Estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Estoque.setStyleSheet(u"QPushButton{\n"
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
        icon6.addFile(u":/image/imagens/vendas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Estoque.setIcon(icon6)
        self.btn_Estoque.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.btn_Estoque, 0, 1, 1, 1)

        self.btn_Editar = QPushButton(Vendas)
        self.btn_Editar.setObjectName(u"btn_Editar")
        sizePolicy2.setHeightForWidth(self.btn_Editar.sizePolicy().hasHeightForWidth())
        self.btn_Editar.setSizePolicy(sizePolicy2)
        self.btn_Editar.setFont(font)
        self.btn_Editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Editar.setStyleSheet(u"QPushButton{;\n"
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
        icon7.addFile(u":/image/imagens/editar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Editar.setIcon(icon7)
        self.btn_Editar.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.btn_Editar, 0, 4, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.label = QLabel(Vendas)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(Vendas)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.Cbb_nome = QComboBox(Vendas)
        self.Cbb_nome.setObjectName(u"Cbb_nome")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Cbb_nome.sizePolicy().hasHeightForWidth())
        self.Cbb_nome.setSizePolicy(sizePolicy3)
        self.Cbb_nome.setFont(font2)

        self.gridLayout_3.addWidget(self.Cbb_nome, 0, 1, 1, 1)

        self.label_4 = QLabel(Vendas)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font2)

        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)

        self.Cbb_Pag = QComboBox(Vendas)
        self.Cbb_Pag.setObjectName(u"Cbb_Pag")
        sizePolicy2.setHeightForWidth(self.Cbb_Pag.sizePolicy().hasHeightForWidth())
        self.Cbb_Pag.setSizePolicy(sizePolicy2)
        self.Cbb_Pag.setFont(font2)

        self.gridLayout_3.addWidget(self.Cbb_Pag, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 3, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(Vendas)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.Cbb_Produto = QComboBox(Vendas)
        self.Cbb_Produto.setObjectName(u"Cbb_Produto")
        sizePolicy3.setHeightForWidth(self.Cbb_Produto.sizePolicy().hasHeightForWidth())
        self.Cbb_Produto.setSizePolicy(sizePolicy3)
        self.Cbb_Produto.setFont(font2)

        self.gridLayout_4.addWidget(self.Cbb_Produto, 0, 1, 1, 1)

        self.label_6 = QLabel(Vendas)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_4.addWidget(self.label_6, 0, 2, 1, 1)

        self.L_Quat = QLineEdit(Vendas)
        self.L_Quat.setObjectName(u"L_Quat")
        sizePolicy2.setHeightForWidth(self.L_Quat.sizePolicy().hasHeightForWidth())
        self.L_Quat.setSizePolicy(sizePolicy2)
        self.L_Quat.setFont(font2)
        self.L_Quat.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.L_Quat, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 4, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_Data = QPushButton(Vendas)
        self.btn_Data.setObjectName(u"btn_Data")
        sizePolicy2.setHeightForWidth(self.btn_Data.sizePolicy().hasHeightForWidth())
        self.btn_Data.setSizePolicy(sizePolicy2)
        self.btn_Data.setFont(font)
        self.btn_Data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Data.setStyleSheet(u"QPushButton{;\n"
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

        self.gridLayout_5.addWidget(self.btn_Data, 0, 4, 1, 1)

        self.L_Id = QLineEdit(Vendas)
        self.L_Id.setObjectName(u"L_Id")
        sizePolicy2.setHeightForWidth(self.L_Id.sizePolicy().hasHeightForWidth())
        self.L_Id.setSizePolicy(sizePolicy2)
        self.L_Id.setFont(font2)
        self.L_Id.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.L_Id, 0, 3, 1, 1)

        self.label_8 = QLabel(Vendas)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_5.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_7 = QLabel(Vendas)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.L_Data = QLineEdit(Vendas)
        self.L_Data.setObjectName(u"L_Data")
        sizePolicy2.setHeightForWidth(self.L_Data.sizePolicy().hasHeightForWidth())
        self.L_Data.setSizePolicy(sizePolicy2)
        self.L_Data.setFont(font2)
        self.L_Data.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.L_Data, 0, 5, 1, 1)

        self.L_Valor = QLineEdit(Vendas)
        self.L_Valor.setObjectName(u"L_Valor")
        sizePolicy2.setHeightForWidth(self.L_Valor.sizePolicy().hasHeightForWidth())
        self.L_Valor.setSizePolicy(sizePolicy2)
        self.L_Valor.setFont(font2)
        self.L_Valor.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.L_Valor, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 5, 0, 1, 1)

        self.Tab_Caixa_Vendas = QTableWidget(Vendas)
        if (self.Tab_Caixa_Vendas.columnCount() < 7):
            self.Tab_Caixa_Vendas.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.Tab_Caixa_Vendas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.Tab_Caixa_Vendas.setObjectName(u"Tab_Caixa_Vendas")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Tab_Caixa_Vendas.sizePolicy().hasHeightForWidth())
        self.Tab_Caixa_Vendas.setSizePolicy(sizePolicy5)
        self.Tab_Caixa_Vendas.setFont(font2)

        self.gridLayout_6.addWidget(self.Tab_Caixa_Vendas, 6, 0, 1, 1)


        self.retranslateUi(Vendas)

        QMetaObject.connectSlotsByName(Vendas)
    # setupUi

    def retranslateUi(self, Vendas):
        Vendas.setWindowTitle(QCoreApplication.translate("Vendas", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.btn_Voltar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Voltar.setText("")
        self.label_2.setText(QCoreApplication.translate("Vendas", u"Vendas", None))
#if QT_CONFIG(tooltip)
        self.btn_Salvar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Salvar.setText(QCoreApplication.translate("Vendas", u"Salvar", None))
#if QT_CONFIG(tooltip)
        self.btn_Excluir.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Excluir.setText(QCoreApplication.translate("Vendas", u"Excluir", None))
#if QT_CONFIG(tooltip)
        self.btn_Estoque_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Estoque_2.setText(QCoreApplication.translate("Vendas", u"Produtos", None))
        self.btn_CadCliente.setText(QCoreApplication.translate("Vendas", u"Clientes", None))
#if QT_CONFIG(tooltip)
        self.btn_Limpar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Limpar.setText(QCoreApplication.translate("Vendas", u"Limpar", None))
#if QT_CONFIG(tooltip)
        self.btn_Estoque.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Estoque.setText(QCoreApplication.translate("Vendas", u"Compras", None))
#if QT_CONFIG(tooltip)
        self.btn_Editar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Editar.setText(QCoreApplication.translate("Vendas", u"Editar", None))
        self.label.setText(QCoreApplication.translate("Vendas", u"Registro de Vendas", None))
        self.label_3.setText(QCoreApplication.translate("Vendas", u"Nome:", None))
        self.Cbb_nome.setCurrentText("")
        self.Cbb_nome.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("Vendas", u"Pagamento:", None))
        self.Cbb_Pag.setCurrentText("")
        self.Cbb_Pag.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Vendas", u"Produtos:", None))
        self.Cbb_Produto.setCurrentText("")
        self.Cbb_Produto.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("Vendas", u"Quantidades:", None))
#if QT_CONFIG(tooltip)
        self.btn_Data.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Data.setText("")
        self.label_8.setText(QCoreApplication.translate("Vendas", u"ID:", None))
        self.label_7.setText(QCoreApplication.translate("Vendas", u"Valor:", None))
        ___qtablewidgetitem = self.Tab_Caixa_Vendas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Vendas", u"Data", None));
        ___qtablewidgetitem1 = self.Tab_Caixa_Vendas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Vendas", u"Cliente", None));
        ___qtablewidgetitem2 = self.Tab_Caixa_Vendas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Vendas", u"Produtos", None));
        ___qtablewidgetitem3 = self.Tab_Caixa_Vendas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Vendas", u"Quantidades", None));
        ___qtablewidgetitem4 = self.Tab_Caixa_Vendas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Vendas", u"Valor", None));
        ___qtablewidgetitem5 = self.Tab_Caixa_Vendas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Vendas", u"SubTotal", None));
        ___qtablewidgetitem6 = self.Tab_Caixa_Vendas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Vendas", u"Pagamento", None));
    # retranslateUi


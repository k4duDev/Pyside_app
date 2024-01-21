# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(626, 581)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        Menu.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.actionSalvar = QAction(Menu)
        self.actionSalvar.setObjectName(u"actionSalvar")
        icon = QIcon()
        icon.addFile(u":/image/imagens/Save.32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSalvar.setIcon(icon)
        self.actionFechar = QAction(Menu)
        self.actionFechar.setObjectName(u"actionFechar")
        icon1 = QIcon()
        icon1.addFile(u":/image/imagens/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFechar.setIcon(icon1)
        self.actionClientes = QAction(Menu)
        self.actionClientes.setObjectName(u"actionClientes")
        icon2 = QIcon()
        icon2.addFile(u":/image/imagens/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClientes.setIcon(icon2)
        self.actionCompras = QAction(Menu)
        self.actionCompras.setObjectName(u"actionCompras")
        icon3 = QIcon()
        icon3.addFile(u":/image/imagens/S_Compras.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCompras.setIcon(icon3)
        self.actionEstoque = QAction(Menu)
        self.actionEstoque.setObjectName(u"actionEstoque")
        icon4 = QIcon()
        icon4.addFile(u":/image/imagens/editar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEstoque.setIcon(icon4)
        self.actionProdutos = QAction(Menu)
        self.actionProdutos.setObjectName(u"actionProdutos")
        icon5 = QIcon()
        icon5.addFile(u":/image/imagens/Produtos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionProdutos.setIcon(icon5)
        self.actionVendas = QAction(Menu)
        self.actionVendas.setObjectName(u"actionVendas")
        icon6 = QIcon()
        icon6.addFile(u":/image/imagens/Cash-register.32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionVendas.setIcon(icon6)
        self.actionContatos = QAction(Menu)
        self.actionContatos.setObjectName(u"actionContatos")
        icon7 = QIcon()
        icon7.addFile(u":/image/imagens/whatsapp-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionContatos.setIcon(icon7)
        self.actionSobre = QAction(Menu)
        self.actionSobre.setObjectName(u"actionSobre")
        icon8 = QIcon()
        icon8.addFile(u":/image/imagens/Info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSobre.setIcon(icon8)
        self.actionUsuarios = QAction(Menu)
        self.actionUsuarios.setObjectName(u"actionUsuarios")
        icon9 = QIcon()
        icon9.addFile(u":/image/imagens/cadastro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUsuarios.setIcon(icon9)
        self.centralwidget = QWidget(Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.BtnToggle = QPushButton(self.centralwidget)
        self.BtnToggle.setObjectName(u"BtnToggle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.BtnToggle.sizePolicy().hasHeightForWidth())
        self.BtnToggle.setSizePolicy(sizePolicy1)
        self.BtnToggle.setMaximumSize(QSize(40, 40))
        self.BtnToggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/image/imagens/menu-bar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.BtnToggle.setIcon(icon10)
        self.BtnToggle.setIconSize(QSize(45, 45))
        self.BtnToggle.setFlat(True)

        self.gridLayout_6.addWidget(self.BtnToggle, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.L_usuario = QLabel(self.centralwidget)
        self.L_usuario.setObjectName(u"L_usuario")
        sizePolicy.setHeightForWidth(self.L_usuario.sizePolicy().hasHeightForWidth())
        self.L_usuario.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.L_usuario.setFont(font)
        self.L_usuario.setStyleSheet(u"")
        self.L_usuario.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.L_usuario, 0, 8, 1, 1)

        self.Btn_Calen = QPushButton(self.centralwidget)
        self.Btn_Calen.setObjectName(u"Btn_Calen")
        icon11 = QIcon()
        icon11.addFile(u":/image/imagens/calendario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Calen.setIcon(icon11)

        self.gridLayout_3.addWidget(self.Btn_Calen, 0, 6, 1, 1)

        self.L_Logado = QLabel(self.centralwidget)
        self.L_Logado.setObjectName(u"L_Logado")
        sizePolicy.setHeightForWidth(self.L_Logado.sizePolicy().hasHeightForWidth())
        self.L_Logado.setSizePolicy(sizePolicy)
        self.L_Logado.setFont(font)
        self.L_Logado.setStyleSheet(u"color: rgb(0, 255, 165);\n"
"")
        self.L_Logado.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.L_Logado, 0, 7, 1, 1)

        self.L_Data = QLabel(self.centralwidget)
        self.L_Data.setObjectName(u"L_Data")
        sizePolicy.setHeightForWidth(self.L_Data.sizePolicy().hasHeightForWidth())
        self.L_Data.setSizePolicy(sizePolicy)
        self.L_Data.setFont(font)
        self.L_Data.setStyleSheet(u"")
        self.L_Data.setFrameShape(QFrame.NoFrame)
        self.L_Data.setFrameShadow(QFrame.Plain)
        self.L_Data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.L_Data, 0, 5, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.LeftMenu = QFrame(self.centralwidget)
        self.LeftMenu.setObjectName(u"LeftMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LeftMenu.sizePolicy().hasHeightForWidth())
        self.LeftMenu.setSizePolicy(sizePolicy2)
        self.LeftMenu.setMaximumSize(QSize(0, 450))
        self.LeftMenu.setFrameShape(QFrame.StyledPanel)
        self.LeftMenu.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.LeftMenu)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Toggle = QToolBox(self.LeftMenu)
        self.Toggle.setObjectName(u"Toggle")
        sizePolicy.setHeightForWidth(self.Toggle.sizePolicy().hasHeightForWidth())
        self.Toggle.setSizePolicy(sizePolicy)
        self.Toggle.setMaximumSize(QSize(230, 450))
        self.Toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.Toggle.setLayoutDirection(Qt.LeftToRight)
        self.Toggle.setFrameShape(QFrame.Panel)
        self.Toggle.setFrameShadow(QFrame.Plain)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(0, 0, 16, 384))
        self.layoutWidget = QWidget(self.Home)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 202, 332))
        self.gridLayout_4 = QGridLayout(self.layoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_Clientes = QPushButton(self.layoutWidget)
        self.Btn_Clientes.setObjectName(u"Btn_Clientes")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Btn_Clientes.sizePolicy().hasHeightForWidth())
        self.Btn_Clientes.setSizePolicy(sizePolicy3)
        self.Btn_Clientes.setMinimumSize(QSize(200, 50))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.Btn_Clientes.setFont(font1)
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
        self.Btn_Clientes.setIcon(icon2)
        self.Btn_Clientes.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.Btn_Clientes, 0, 0, 1, 1)

        self.Btn_Compras = QPushButton(self.layoutWidget)
        self.Btn_Compras.setObjectName(u"Btn_Compras")
        sizePolicy3.setHeightForWidth(self.Btn_Compras.sizePolicy().hasHeightForWidth())
        self.Btn_Compras.setSizePolicy(sizePolicy3)
        self.Btn_Compras.setMinimumSize(QSize(200, 50))
        self.Btn_Compras.setFont(font1)
        self.Btn_Compras.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Compras.setStyleSheet(u"QPushButton{\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/image/imagens/vendas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Compras.setIcon(icon12)
        self.Btn_Compras.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.Btn_Compras, 1, 0, 1, 1)

        self.Btn_Estoque = QPushButton(self.layoutWidget)
        self.Btn_Estoque.setObjectName(u"Btn_Estoque")
        sizePolicy3.setHeightForWidth(self.Btn_Estoque.sizePolicy().hasHeightForWidth())
        self.Btn_Estoque.setSizePolicy(sizePolicy3)
        self.Btn_Estoque.setMinimumSize(QSize(200, 50))
        self.Btn_Estoque.setFont(font1)
        self.Btn_Estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Estoque.setStyleSheet(u"QPushButton{\n"
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
        self.Btn_Estoque.setIcon(icon4)
        self.Btn_Estoque.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.Btn_Estoque, 2, 0, 1, 1)

        self.Btn_Produtos = QPushButton(self.layoutWidget)
        self.Btn_Produtos.setObjectName(u"Btn_Produtos")
        sizePolicy3.setHeightForWidth(self.Btn_Produtos.sizePolicy().hasHeightForWidth())
        self.Btn_Produtos.setSizePolicy(sizePolicy3)
        self.Btn_Produtos.setMinimumSize(QSize(200, 50))
        self.Btn_Produtos.setFont(font1)
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
        self.Btn_Produtos.setIcon(icon5)
        self.Btn_Produtos.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.Btn_Produtos, 3, 0, 1, 1)

        self.Btn_Vendas = QPushButton(self.layoutWidget)
        self.Btn_Vendas.setObjectName(u"Btn_Vendas")
        sizePolicy3.setHeightForWidth(self.Btn_Vendas.sizePolicy().hasHeightForWidth())
        self.Btn_Vendas.setSizePolicy(sizePolicy3)
        self.Btn_Vendas.setMinimumSize(QSize(200, 50))
        self.Btn_Vendas.setFont(font1)
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
        self.Btn_Vendas.setIcon(icon6)
        self.Btn_Vendas.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.Btn_Vendas, 4, 0, 1, 1)

        self.Btn_Usuarios = QPushButton(self.layoutWidget)
        self.Btn_Usuarios.setObjectName(u"Btn_Usuarios")
        sizePolicy3.setHeightForWidth(self.Btn_Usuarios.sizePolicy().hasHeightForWidth())
        self.Btn_Usuarios.setSizePolicy(sizePolicy3)
        self.Btn_Usuarios.setMinimumSize(QSize(200, 50))
        self.Btn_Usuarios.setFont(font1)
        self.Btn_Usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Usuarios.setStyleSheet(u"QPushButton{\n"
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
        icon13 = QIcon()
        icon13.addFile(u":/image/imagens/cade.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Usuarios.setIcon(icon13)
        self.Btn_Usuarios.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.Btn_Usuarios, 5, 0, 1, 1)

        self.Toggle.addItem(self.Home, u"Home")
        self.Ajuda = QWidget()
        self.Ajuda.setObjectName(u"Ajuda")
        self.Ajuda.setGeometry(QRect(0, 0, 16, 384))
        self.layoutWidget1 = QWidget(self.Ajuda)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(9, 9, 202, 88))
        self.gridLayout_5 = QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Btn_Contatos = QPushButton(self.layoutWidget1)
        self.Btn_Contatos.setObjectName(u"Btn_Contatos")
        sizePolicy3.setHeightForWidth(self.Btn_Contatos.sizePolicy().hasHeightForWidth())
        self.Btn_Contatos.setSizePolicy(sizePolicy3)
        self.Btn_Contatos.setMinimumSize(QSize(200, 40))
        self.Btn_Contatos.setFont(font1)
        self.Btn_Contatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Contatos.setStyleSheet(u"QPushButton{\n"
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
        self.Btn_Contatos.setIcon(icon7)
        self.Btn_Contatos.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.Btn_Contatos, 0, 0, 1, 1)

        self.Btn_Sobre = QPushButton(self.layoutWidget1)
        self.Btn_Sobre.setObjectName(u"Btn_Sobre")
        sizePolicy3.setHeightForWidth(self.Btn_Sobre.sizePolicy().hasHeightForWidth())
        self.Btn_Sobre.setSizePolicy(sizePolicy3)
        self.Btn_Sobre.setMinimumSize(QSize(200, 40))
        self.Btn_Sobre.setFont(font1)
        self.Btn_Sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Sobre.setStyleSheet(u"QPushButton{\n"
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
        self.Btn_Sobre.setIcon(icon8)
        self.Btn_Sobre.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.Btn_Sobre, 1, 0, 1, 1)

        self.Toggle.addItem(self.Ajuda, u"Ajuda")

        self.gridLayout_2.addWidget(self.Toggle, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.LeftMenu, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 43))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setFont(font1)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 2, 1, 1, 1)

        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Menu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 626, 21))
        self.menuArquivos = QMenu(self.menubar)
        self.menuArquivos.setObjectName(u"menuArquivos")
        self.menuAbrir = QMenu(self.menuArquivos)
        self.menuAbrir.setObjectName(u"menuAbrir")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        Menu.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArquivos.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menuArquivos.addAction(self.menuAbrir.menuAction())
        self.menuArquivos.addAction(self.actionSalvar)
        self.menuArquivos.addAction(self.actionFechar)
        self.menuAbrir.addAction(self.actionClientes)
        self.menuAbrir.addAction(self.actionCompras)
        self.menuAbrir.addAction(self.actionEstoque)
        self.menuAbrir.addAction(self.actionProdutos)
        self.menuAbrir.addAction(self.actionVendas)
        self.menuAbrir.addAction(self.actionUsuarios)
        self.menuAjuda.addAction(self.actionContatos)
        self.menuAjuda.addAction(self.actionSobre)

        self.retranslateUi(Menu)

        self.Toggle.setCurrentIndex(0)
        self.Toggle.layout().setSpacing(0)


        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"MainWindow", None))
        self.actionSalvar.setText(QCoreApplication.translate("Menu", u"Salvar", None))
        self.actionFechar.setText(QCoreApplication.translate("Menu", u"Fechar", None))
        self.actionClientes.setText(QCoreApplication.translate("Menu", u"Clientes", None))
#if QT_CONFIG(tooltip)
        self.actionClientes.setToolTip(QCoreApplication.translate("Menu", u"Cadastro de Clientes", None))
#endif // QT_CONFIG(tooltip)
        self.actionCompras.setText(QCoreApplication.translate("Menu", u"Compras", None))
#if QT_CONFIG(tooltip)
        self.actionCompras.setToolTip(QCoreApplication.translate("Menu", u"Ca dastro de Compras", None))
#endif // QT_CONFIG(tooltip)
        self.actionEstoque.setText(QCoreApplication.translate("Menu", u"Estoque", None))
#if QT_CONFIG(tooltip)
        self.actionEstoque.setToolTip(QCoreApplication.translate("Menu", u"Controle de Estoque", None))
#endif // QT_CONFIG(tooltip)
        self.actionProdutos.setText(QCoreApplication.translate("Menu", u"Produtos", None))
#if QT_CONFIG(tooltip)
        self.actionProdutos.setToolTip(QCoreApplication.translate("Menu", u"Tela de Produtos", None))
#endif // QT_CONFIG(tooltip)
        self.actionVendas.setText(QCoreApplication.translate("Menu", u"Vendas", None))
#if QT_CONFIG(tooltip)
        self.actionVendas.setToolTip(QCoreApplication.translate("Menu", u"Cadastro de Vendas", None))
#endif // QT_CONFIG(tooltip)
        self.actionContatos.setText(QCoreApplication.translate("Menu", u"Contatos", None))
        self.actionSobre.setText(QCoreApplication.translate("Menu", u"Sobre", None))
        self.actionUsuarios.setText(QCoreApplication.translate("Menu", u"Usuarios", None))
        self.L_usuario.setText("")
        self.Btn_Calen.setText("")
        self.L_Logado.setText(QCoreApplication.translate("Menu", u"<html><head/><body><p align=\"center\">Logado </p></body></html>", None))
        self.L_Data.setText("")
        self.Btn_Clientes.setText(QCoreApplication.translate("Menu", u"Clientes", None))
        self.Btn_Compras.setText(QCoreApplication.translate("Menu", u"Compras", None))
        self.Btn_Estoque.setText(QCoreApplication.translate("Menu", u"Estoque", None))
        self.Btn_Produtos.setText(QCoreApplication.translate("Menu", u"Produtos", None))
        self.Btn_Vendas.setText(QCoreApplication.translate("Menu", u"Vendas", None))
        self.Btn_Usuarios.setText(QCoreApplication.translate("Menu", u"Usuarios", None))
        self.Toggle.setItemText(self.Toggle.indexOf(self.Home), QCoreApplication.translate("Menu", u"Home", None))
        self.Btn_Contatos.setText(QCoreApplication.translate("Menu", u"Contatos", None))
        self.Btn_Sobre.setText(QCoreApplication.translate("Menu", u"Sobre", None))
        self.Toggle.setItemText(self.Toggle.indexOf(self.Ajuda), QCoreApplication.translate("Menu", u"Ajuda", None))
        self.label.setText(QCoreApplication.translate("Menu", u"<html><head/><body><p align=\"center\">Kdu 2023 <img src=\":/image/imagens/d.png\"/></p></body></html>", None))
        self.menuArquivos.setTitle(QCoreApplication.translate("Menu", u"Arquivos", None))
        self.menuAbrir.setTitle(QCoreApplication.translate("Menu", u"Abrir", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("Menu", u"Ajuda", None))
    # retranslateUi


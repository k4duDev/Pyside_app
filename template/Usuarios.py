# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Usuarios.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Usuarios(object):
    def setupUi(self, Usuarios):
        if not Usuarios.objectName():
            Usuarios.setObjectName(u"Usuarios")
        Usuarios.resize(960, 628)
        Usuarios.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.gridLayout_6 = QGridLayout(Usuarios)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_Voltar = QPushButton(Usuarios)
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
        font.setWeight(75)
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
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/image/imagens/voltar1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Voltar.setIcon(icon)
        self.btn_Voltar.setIconSize(QSize(80, 45))

        self.gridLayout_3.addWidget(self.btn_Voltar, 0, 0, 1, 1)

        self.label = QLabel(Usuarios)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_Excluir = QPushButton(Usuarios)
        self.btn_Excluir.setObjectName(u"btn_Excluir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_Excluir.sizePolicy().hasHeightForWidth())
        self.btn_Excluir.setSizePolicy(sizePolicy1)
        self.btn_Excluir.setFont(font)
        self.btn_Excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Excluir.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/image/imagens/excluir-arquivo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Excluir.setIcon(icon1)
        self.btn_Excluir.setIconSize(QSize(45, 45))

        self.gridLayout_5.addWidget(self.btn_Excluir, 0, 7, 1, 1)

        self.btn_Salvar = QPushButton(Usuarios)
        self.btn_Salvar.setObjectName(u"btn_Salvar")
        sizePolicy1.setHeightForWidth(self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy1)
        self.btn_Salvar.setFont(font)
        self.btn_Salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/image/imagens/guardar-dados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Salvar.setIcon(icon2)
        self.btn_Salvar.setIconSize(QSize(45, 45))

        self.gridLayout_5.addWidget(self.btn_Salvar, 0, 4, 1, 1)

        self.L_Data = QLineEdit(Usuarios)
        self.L_Data.setObjectName(u"L_Data")
        sizePolicy1.setHeightForWidth(self.L_Data.sizePolicy().hasHeightForWidth())
        self.L_Data.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.L_Data.setFont(font2)

        self.gridLayout_5.addWidget(self.L_Data, 0, 2, 1, 1)

        self.btn_Limpar = QPushButton(Usuarios)
        self.btn_Limpar.setObjectName(u"btn_Limpar")
        sizePolicy1.setHeightForWidth(self.btn_Limpar.sizePolicy().hasHeightForWidth())
        self.btn_Limpar.setSizePolicy(sizePolicy1)
        self.btn_Limpar.setFont(font)
        self.btn_Limpar.setStyleSheet(u"QPushButton{\n"
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
        icon3.addFile(u":/image/imagens/limpar-limpo (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Limpar.setIcon(icon3)
        self.btn_Limpar.setIconSize(QSize(45, 45))

        self.gridLayout_5.addWidget(self.btn_Limpar, 0, 6, 1, 1)

        self.label_3 = QLabel(Usuarios)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font2)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.L_Id = QLineEdit(Usuarios)
        self.L_Id.setObjectName(u"L_Id")
        self.L_Id.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.L_Id.sizePolicy().hasHeightForWidth())
        self.L_Id.setSizePolicy(sizePolicy1)
        self.L_Id.setFont(font2)

        self.gridLayout_5.addWidget(self.L_Id, 0, 1, 1, 1)

        self.btn_Editar = QPushButton(Usuarios)
        self.btn_Editar.setObjectName(u"btn_Editar")
        sizePolicy1.setHeightForWidth(self.btn_Editar.sizePolicy().hasHeightForWidth())
        self.btn_Editar.setSizePolicy(sizePolicy1)
        self.btn_Editar.setFont(font)
        self.btn_Editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Editar.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/image/imagens/editar (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Editar.setIcon(icon4)
        self.btn_Editar.setIconSize(QSize(45, 45))

        self.gridLayout_5.addWidget(self.btn_Editar, 0, 5, 1, 1)

        self.btn_Data = QPushButton(Usuarios)
        self.btn_Data.setObjectName(u"btn_Data")
        sizePolicy1.setHeightForWidth(self.btn_Data.sizePolicy().hasHeightForWidth())
        self.btn_Data.setSizePolicy(sizePolicy1)
        self.btn_Data.setFont(font)
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
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/image/imagens/calendario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Data.setIcon(icon5)
        self.btn_Data.setIconSize(QSize(45, 45))

        self.gridLayout_5.addWidget(self.btn_Data, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Usuarios)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font2)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.L_Nome = QLineEdit(Usuarios)
        self.L_Nome.setObjectName(u"L_Nome")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.L_Nome.sizePolicy().hasHeightForWidth())
        self.L_Nome.setSizePolicy(sizePolicy2)
        self.L_Nome.setFont(font2)
        self.L_Nome.setMaxLength(50)

        self.gridLayout.addWidget(self.L_Nome, 0, 1, 1, 1)

        self.label_5 = QLabel(Usuarios)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font2)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.L_Telefone = QLineEdit(Usuarios)
        self.L_Telefone.setObjectName(u"L_Telefone")
        sizePolicy1.setHeightForWidth(self.L_Telefone.sizePolicy().hasHeightForWidth())
        self.L_Telefone.setSizePolicy(sizePolicy1)
        self.L_Telefone.setFont(font2)

        self.gridLayout.addWidget(self.L_Telefone, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(Usuarios)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.L_Endereco = QLineEdit(Usuarios)
        self.L_Endereco.setObjectName(u"L_Endereco")
        self.L_Endereco.setFont(font2)
        self.L_Endereco.setMaxLength(80)

        self.gridLayout_2.addWidget(self.L_Endereco, 0, 1, 1, 1)

        self.label_9 = QLabel(Usuarios)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)

        self.Cbb_Permicao = QComboBox(Usuarios)
        self.Cbb_Permicao.addItem("")
        self.Cbb_Permicao.addItem("")
        self.Cbb_Permicao.addItem("")
        self.Cbb_Permicao.setObjectName(u"Cbb_Permicao")
        self.Cbb_Permicao.setFont(font2)

        self.gridLayout_2.addWidget(self.Cbb_Permicao, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(Usuarios)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.L_Usuario = QLineEdit(Usuarios)
        self.L_Usuario.setObjectName(u"L_Usuario")
        self.L_Usuario.setFont(font2)
        self.L_Usuario.setMaxLength(50)

        self.gridLayout_4.addWidget(self.L_Usuario, 0, 1, 1, 1)

        self.label_8 = QLabel(Usuarios)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 0, 2, 1, 1)

        self.L_Senha = QLineEdit(Usuarios)
        self.L_Senha.setObjectName(u"L_Senha")
        self.L_Senha.setFont(font2)
        self.L_Senha.setMaxLength(50)

        self.gridLayout_4.addWidget(self.L_Senha, 0, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_4, 4, 0, 1, 1)

        self.Tab_Usuarios = QTableWidget(Usuarios)
        if (self.Tab_Usuarios.columnCount() < 8):
            self.Tab_Usuarios.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.Tab_Usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.Tab_Usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.Tab_Usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.Tab_Usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.Tab_Usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.Tab_Usuarios.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.Tab_Usuarios.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.Tab_Usuarios.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.Tab_Usuarios.setObjectName(u"Tab_Usuarios")

        self.gridLayout_6.addWidget(self.Tab_Usuarios, 5, 0, 1, 1)

        QWidget.setTabOrder(self.L_Id, self.L_Data)
        QWidget.setTabOrder(self.L_Data, self.L_Nome)
        QWidget.setTabOrder(self.L_Nome, self.L_Telefone)
        QWidget.setTabOrder(self.L_Telefone, self.L_Endereco)
        QWidget.setTabOrder(self.L_Endereco, self.L_Usuario)
        QWidget.setTabOrder(self.L_Usuario, self.L_Senha)
        QWidget.setTabOrder(self.L_Senha, self.Cbb_Permicao)
        QWidget.setTabOrder(self.Cbb_Permicao, self.btn_Salvar)
        QWidget.setTabOrder(self.btn_Salvar, self.btn_Limpar)
        QWidget.setTabOrder(self.btn_Limpar, self.btn_Excluir)
        QWidget.setTabOrder(self.btn_Excluir, self.Tab_Usuarios)

        self.retranslateUi(Usuarios)

        QMetaObject.connectSlotsByName(Usuarios)
    # setupUi

    def retranslateUi(self, Usuarios):
        Usuarios.setWindowTitle(QCoreApplication.translate("Usuarios", u"Dialog", None))
        self.btn_Voltar.setText("")
        self.label.setText(QCoreApplication.translate("Usuarios", u"Usuarios", None))
        self.btn_Excluir.setText(QCoreApplication.translate("Usuarios", u"Excluir", None))
        self.btn_Salvar.setText(QCoreApplication.translate("Usuarios", u"Salvar", None))
        self.L_Data.setInputMask("")
        self.btn_Limpar.setText(QCoreApplication.translate("Usuarios", u"Limpar", None))
        self.label_3.setText(QCoreApplication.translate("Usuarios", u"ID:", None))
        self.btn_Editar.setText(QCoreApplication.translate("Usuarios", u"Editar", None))
        self.btn_Data.setText("")
        self.label_4.setText(QCoreApplication.translate("Usuarios", u"Nome:", None))
        self.label_5.setText(QCoreApplication.translate("Usuarios", u"Telefone:", None))
        self.L_Telefone.setInputMask(QCoreApplication.translate("Usuarios", u"(00)00000-0000", None))
        self.label_6.setText(QCoreApplication.translate("Usuarios", u"Endere\u00e7o:", None))
        self.label_9.setText(QCoreApplication.translate("Usuarios", u"Permi\u00e7\u00e3o", None))
        self.Cbb_Permicao.setItemText(0, "")
        self.Cbb_Permicao.setItemText(1, QCoreApplication.translate("Usuarios", u"Administrador", None))
        self.Cbb_Permicao.setItemText(2, QCoreApplication.translate("Usuarios", u"Usu\u00e1rio", None))

        self.label_7.setText(QCoreApplication.translate("Usuarios", u"Usuario", None))
        self.label_8.setText(QCoreApplication.translate("Usuarios", u"Senha", None))
        ___qtablewidgetitem = self.Tab_Usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Usuarios", u"ID", None));
        ___qtablewidgetitem1 = self.Tab_Usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Usuarios", u"Data", None));
        ___qtablewidgetitem2 = self.Tab_Usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Usuarios", u"Nome", None));
        ___qtablewidgetitem3 = self.Tab_Usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Usuarios", u"Telefone", None));
        ___qtablewidgetitem4 = self.Tab_Usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Usuarios", u"Endere\u00e7o", None));
        ___qtablewidgetitem5 = self.Tab_Usuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Usuarios", u"Usuario", None));
        ___qtablewidgetitem6 = self.Tab_Usuarios.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Usuarios", u"Senha", None));
        ___qtablewidgetitem7 = self.Tab_Usuarios.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Usuarios", u"Permi\u00e7\u00e3o", None));
    # retranslateUi


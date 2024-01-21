# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calendario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Calendario(object):
    def setupUi(self, Calendario):
        if not Calendario.objectName():
            Calendario.setObjectName(u"Calendario")
        Calendario.resize(339, 264)
        self.gridLayout = QGridLayout(Calendario)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Calendario = QCalendarWidget(Calendario)
        self.Calendario.setObjectName(u"Calendario")

        self.gridLayout.addWidget(self.Calendario, 0, 0, 1, 1)

        self.data = QLabel(Calendario)
        self.data.setObjectName(u"data")
        self.data.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.data, 1, 0, 1, 1)


        self.retranslateUi(Calendario)
        self.Calendario.selectionChanged.connect(self.Calendario.showSelectedDate)

        QMetaObject.connectSlotsByName(Calendario)
    # setupUi

    def retranslateUi(self, Calendario):
        Calendario.setWindowTitle(QCoreApplication.translate("Calendario", u"Calendario", None))
    # retranslateUi


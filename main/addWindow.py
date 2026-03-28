# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class AddDialog(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(519, 227)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameEntry = QLineEdit(self.centralwidget)
        self.nameEntry.setObjectName(u"nameEntry")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameEntry)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.phoneEntry = QLineEdit(self.centralwidget)
        self.phoneEntry.setObjectName(u"phoneEntry")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.phoneEntry)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.mailEntry = QLineEdit(self.centralwidget)
        self.mailEntry.setObjectName(u"mailEntry")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.mailEntry)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)


        self.verticalLayout.addLayout(self.formLayout)

        self.addConfirm = QPushButton(self.centralwidget)
        self.addConfirm.setObjectName(u"addConfirm")

        self.verticalLayout.addWidget(self.addConfirm)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 519, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Window", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Phone:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"E-Mail:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.addConfirm.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi


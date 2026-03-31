# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUI.ui'
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

class Ui_loginUI(object):
    def setupUi(self, loginUI):
        if not loginUI.objectName():
            loginUI.setObjectName(u"loginUI")
        loginUI.resize(447, 196)
        self.centralwidget = QWidget(loginUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.username)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.password)


        self.verticalLayout.addLayout(self.formLayout)

        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")

        self.verticalLayout.addWidget(self.loginButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        loginUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(loginUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 447, 30))
        loginUI.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(loginUI)
        self.statusbar.setObjectName(u"statusbar")
        loginUI.setStatusBar(self.statusbar)

        self.retranslateUi(loginUI)

        QMetaObject.connectSlotsByName(loginUI)
    # setupUi

    def retranslateUi(self, loginUI):
        loginUI.setWindowTitle(QCoreApplication.translate("loginUI", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("loginUI", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("loginUI", u"Password:", None))
        self.loginButton.setText(QCoreApplication.translate("loginUI", u"Login", None))
    # retranslateUi


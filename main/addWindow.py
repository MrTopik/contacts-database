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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameEntry = QLineEdit(Dialog)
        self.nameEntry.setObjectName(u"nameEntry")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameEntry)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.phoneEntry = QLineEdit(Dialog)
        self.phoneEntry.setObjectName(u"phoneEntry")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.phoneEntry)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.mailEntry = QLineEdit(Dialog)
        self.mailEntry.setObjectName(u"mailEntry")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.mailEntry)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)


        self.verticalLayout.addLayout(self.formLayout)

        self.addConfirm = QPushButton(Dialog)
        self.addConfirm.setObjectName(u"addConfirm")

        self.verticalLayout.addWidget(self.addConfirm)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Phone:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"E-Mail:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.addConfirm.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi


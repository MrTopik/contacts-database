import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QDialog
from basicUI import Ui_MainWindow
from addWindow import Ui_Dialog
from loginUI import Ui_loginUI
from database import add_contact, get_all_contacts, delete_contact, update_contact, setup

setup() #Database setup

class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.addConfirm.clicked.connect(self.accept)

    def get_data(self):
        return (self.ui.nameEntry.text(),self.ui.phoneEntry.text(),self.ui.mailEntry.text())
    def set_data(self, name, phone, mail):
        self.ui.nameEntry.setText(name)
        self.ui.phoneEntry.setText(phone)
        self.ui.mailEntry.setText(mail)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.logui = Ui_loginUI()
        self.logui.setupUi(self)
        self.logui.loginButton.clicked.connect(self.login)

    def login(self):
        if self.logui.username.text() == "Topik" and self.logui.password.text() == "topik":
            self.UIsetup()
    
    #Main Window
    def UIsetup(self):
        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Name", "Phone", "E-Mail"])

        self.ui.addButton.clicked.connect(self.add_entry)
        self.ui.removeButton.clicked.connect(self.remove_entry)
        self.ui.updateButton.clicked.connect(self.update)
        for i in get_all_contacts():
            self.ui.tableWidget.insertRow(i[0]-1)
            self.ui.tableWidget.setItem(i[0]-1, 0, QTableWidgetItem(i[1]))
            self.ui.tableWidget.setItem(i[0]-1, 1, QTableWidgetItem(i[2]))
            self.ui.tableWidget.setItem(i[0]-1, 2, QTableWidgetItem(i[3]))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            
    #Database functions
    def add_entry(self):
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            name, phone, mail = dialog.get_data()
            add_contact(name,phone,mail)
            self.UIsetup()

    def update(self):
        selected = self.ui.tableWidget.selectedItems()
        if not selected:
            return
        row = self.ui.tableWidget.row(selected[0])

        name  = self.ui.tableWidget.item(row, 0).text()
        phone = self.ui.tableWidget.item(row, 1).text()
        mail  = self.ui.tableWidget.item(row, 2).text()

        dialog = AddDialog(self)          # Reuse the same dialog for updates
        dialog.set_data(name, phone, mail)
        dialog.ui.addConfirm.setText("Update")

        if dialog.exec() == QDialog.Accepted:
            new_name, new_phone, new_mail = dialog.get_data()
            update_contact(row + 1, new_name, new_phone, new_mail)
            self.UIsetup()

    def remove_entry(self):
        selected = self.ui.tableWidget.selectedItems()
        if selected:
            row = self.ui.tableWidget.row(selected[0])
            self.ui.tableWidget.removeRow(row)
            delete_contact(row+1)
        else:
            row = self.ui.tableWidget.rowCount()
            if row > 0:
                self.ui.tableWidget.removeRow(row - 1)
                delete_contact(row+1)

#App setup
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
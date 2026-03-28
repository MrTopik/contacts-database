import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from basicUI import Ui_MainWindow
from addWindow import AddDialog
from database import add_contact, get_all_contacts, delete_contact, update_contact, setup

setup() #Database setup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.add = AddDialog()

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
        self.add.setupUi(self)
        self.add.addConfirm.clicked.connect(self.contactAddConfirm)
        
    def contactAddConfirm(self):
        add_contact(self.add.nameEntry.text(),self.add.phoneEntry.text(),self.add.mailEntry.text())
        self.UIsetup()

    def update(self):
        selected = self.ui.tableWidget.selectedItems()
        self.rowUp = self.ui.tableWidget.row(selected[0])
        self.add.setupUi(self)
        self.add.addConfirm.setText("Update")
        self.add.addConfirm.clicked.connect(self.updateConfirm)
    
    def updateConfirm(self):
        update_contact(self.rowUp+1,self.add.nameEntry.text(),self.add.phoneEntry.text(),self.add.mailEntry.text())
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
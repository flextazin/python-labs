import sys
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView
from PyQt5 import QtSql
from PyQt5 import QtCore

class form(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('orders.db')        
        self.db.open()
        self.setupDatabase()
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('orders')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal,"id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal,"Название")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "ЕИ")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Кол-во")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal,"Цена")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal,"Сумма")
        self.ui.tableWidget.setModel(self.model)
        self.ui.pushButton.clicked.connect(self.addToDb)
        self.show()
        self.ui.pushButton_2.clicked.connect(self.updaterow)
        self.ui.pushButton_3.clicked.connect(self.delrow)
        self.i = self.model.rowCount()
        self.ui.lcdNumber.display(self.i)
        print(self.ui.tableWidget.currentIndex().row())

        
    def setupDatabase(self):
        query = QtSql.QSqlQuery(self.db)
        query.exec(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                title VARCHAR(40) NOT NULL,
                unts VARCHAR(40) NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                sum REAL NOT NULL
            )
            """
        )

    def addToDb(self):
        print(self.i)
        
        q = int(self.ui.lineEdit_3.text())
        p = float(self.ui.lineEdit_4.text())

        self.model.insertRows(self.i,1)
        self.model.setData(self.model.index(self.i, 1),self.ui.lineEdit.text())
        self.model.setData(self.model.index(self.i, 2), self.ui.lineEdit_2.text())
        self.model.setData(self.model.index(self.i, 3), q)
        self.model.setData(self.model.index(self.i, 4), p)
        self.model.setData(self.model.index(self.i, 5), q * p)
        self.model.submitAll()
        self.i = self.model.rowCount()
        self.ui.lcdNumber.display(self.i)

    def delrow(self):
        if self.ui.tableWidget.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableWidget.currentIndex().row())
            self.model.select()
            
            self.i = self.model.rowCount()
            self.ui.lcdNumber.display(self.i)
        else:
            QMessageBox.question(self,'Message', "Выберите строку к удаленю", QMessageBox.Ok)
            self.show()

    def updaterow(self):
        if self.ui.tableWidget.currentIndex().row() > -1:
            q = int(self.ui.lineEdit_3.text())
            p = float(self.ui.lineEdit_4.text())
            currentIndex = self.ui.tableWidget.currentIndex()
            print(currentIndex.row())
            
            self.model.setData(self.model.index(currentIndex.row(), 1),self.ui.lineEdit.text())
            self.model.setData(self.model.index(currentIndex.row(), 2), self.ui.lineEdit_2.text())
            self.model.setData(self.model.index(currentIndex.row(), 3), q)
            self.model.setData(self.model.index(currentIndex.row(), 4), p)
            self.model.setData(self.model.index(currentIndex.row(), 5), q * p)
            self.model.submitAll()
        else:
            QMessageBox.question(self,'Message', "Выберите строку для сохранения", QMessageBox.Ok)
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = form()
    sys.exit(app.exec_())

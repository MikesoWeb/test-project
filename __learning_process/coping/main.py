import sys
from coping import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Вешаем на кнопку функцию
        self.ui.pushButton.clicked.connect(self.my_click)
        self.ui.pushButton_2.clicked.connect(self.my_clear)

    def my_clear(self):
        self.ui.textEdit_2.setText('')
        self.ui.textEdit.setText('')

    def my_click(self):
        result = self.ui.textEdit.toPlainText()
        self.ui.textEdit_2.setText(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

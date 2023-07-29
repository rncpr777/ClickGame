import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        font1 = QFont('helvetica', 45)
        font2 = QFont('helvetica', 60)
        font3 = QFont('helvetica', 25, italic=True)
        font4 = QFont('helvetica', 20)
        font5 = QFont('helvetica', 15)
        self.setWindowTitle('SClicker')
        self.setGeometry(500, 300, 800, 600)
        self.setStyleSheet("background-color: lightblue;")
        namelabel = QLabel(' SClicker', self, font=font1)
        namelabel.setGeometry(275, 5, 300, 100)
        plusbutton = QPushButton('+', self, font=font2)
        plusbutton.setGeometry(25, 300, 150, 100)
        plusbutton.setStyleSheet("background-color: lightcoral;")
        plusbutton.clicked.connect(self.plus)
        minusbutton = QPushButton('-', self, font=font2)
        minusbutton.setGeometry(225, 300, 150, 100)
        minusbutton.setStyleSheet("background-color: lightcoral;")
        minusbutton.clicked.connect(self.minus)
        multbutton = QPushButton('x', self, font=font2)
        multbutton.setGeometry(425, 300, 150, 100)
        multbutton.setStyleSheet("background-color: lightcoral;")
        multbutton.clicked.connect(self.multify)
        divbutton = QPushButton('/', self, font=font2)
        divbutton.setGeometry(625, 300, 150, 100)
        divbutton.setStyleSheet("background-color: lightcoral;")
        divbutton.clicked.connect(self.division)
        delbutton = QPushButton('Delete', self, font=font5)
        delbutton.setGeometry(250, 540, 300, 50)
        delbutton.setStyleSheet("background-color: red;")
        delbutton.clicked.connect(self.delete)
        self.entry = QLineEdit('ENTER DELTA VALUE', self, font=font4)
        self.entry.setGeometry(260, 440, 280, 65)
        self.entry.setStyleSheet("background-color: lightgreen;")
        self.outry = QLineEdit('', self, font=font3)
        self.outry.setGeometry(250, 130, 300, 100)
        self.outry.setText('0')
        self.outry.setReadOnly(True)
        self.outry.setStyleSheet("background-color: white;")

    def plus(self):
        a = float(self.outry.text())
        b = float(self.entry.text())
        n = a + b
        self.outry.setText(str(round(n, 2)))

    def minus(self):
        a = float(self.outry.text())
        b = float(self.entry.text())
        n = a - b
        self.outry.setText(str(round(n, 2)))

    def multify(self):
        a = float(self.outry.text())
        b = float(self.entry.text())
        n = a * b
        self.outry.setText(str(round(n, 2)))

    def division(self):
        a = float(self.outry.text())
        b = float(self.entry.text())
        n = a / b
        self.outry.setText(str(round(n, 2)))

    def delete(self):
        self.outry.setText('0')
        self.entry.setText('ENTER DELTA VALUE')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

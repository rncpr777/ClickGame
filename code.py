import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        font1 = QFont('helvetica', 45)
        font2 = QFont('helvetica', 60)
        font3 = QFont('helvetica', 25, italic=True)
        font4 = QFont('helvetica', 20)
        self.setWindowTitle('SClicker')
        self.setGeometry(500, 300, 800, 600)
        '''p = QPalette()
        p.setColor(self,QPalette.base, QColor.black)
        self.setAutoFillBackground(True)
        self.setPalette(p)'''
        namelabel = QLabel(' SClicker', self, font=font1)
        namelabel.setGeometry(275, 5, 300, 100)
        minusbutton = QPushButton('-', self, font=font2)
        minusbutton.setGeometry(120, 300, 150, 100)
        minusbutton.clicked.connect(self.minus)
        plusbutton = QPushButton('+', self, font=font2)
        plusbutton.setGeometry(320, 300, 150, 100)
        plusbutton.clicked.connect(self.plus)
        multbutton = QPushButton('x', self, font=font2)
        multbutton.setGeometry(520, 300, 150, 100)
        multbutton.clicked.connect(self.multify)
        self.entry = QLineEdit('ENTER DELTA VALUE', self, font=font4)
        self.entry.setGeometry(260, 470, 280, 65)
        self.outry = QLineEdit('', self, font=font3)
        self.outry.setGeometry(250, 130, 300, 100)
        self.outry.setText('0')

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


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
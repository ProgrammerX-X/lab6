import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QRadioButton, \
    QPushButton, QButtonGroup, QTextEdit
from PyQt6.QtGui import QFont
import numpy as np
import sympy as sp

from method_eyler import eyler
from runge import runge

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculating methods")
        self.resize(600, 400)
        self.move(350, 160)

        fontIter = QFont("Arial", 10)

        self.label = QLabel("Чисельні методи", self)
        self.label.move(225, 10)
        self.label.setFixedSize(600, 50)

        font = QFont("Arial", 15)
        font.setBold(True)
        self.label.setFont(font)

        self.method = QLabel("Виберіть метод для обробки", self)
        self.method.move(30, 60)
        self.method.setFixedSize(175, 40)

        self.eylers = QRadioButton("Метод Ейлера", self)
        self.eylers.move(30, 90)
        self.eylers.setFixedSize(175, 40)
        self.eylers.setChecked(True)
        
        self.runge_kutta = QRadioButton("Метод Рунге-Кутти", self)
        self.runge_kutta.move(30, 120)
        self.runge_kutta.setFixedSize(175, 40)

        self.methodGroup = QButtonGroup(self)
        self.methodGroup.addButton(self.eylers)
        self.methodGroup.addButton(self.runge_kutta)

        self.equation = QLabel("Виберіть рівняння", self)
        self.equation.move(410, 60)
        self.equation.setFixedSize(130, 40)
        self.equation.setFont(fontIter)

        self.firstEq = QRadioButton("sec(x) - y * tan(x)", self)
        self.firstEq.move(410, 90)
        self.firstEq.setFixedSize(130, 40)
        self.firstEq.setChecked(True)

        self.eqGroup = QButtonGroup(self)
        self.eqGroup.addButton(self.firstEq)

        self.calculating = QPushButton("Розрахувати", self)
        self.calculating.move(240, 300)
        self.calculating.setFixedSize(130, 40)
        self.calculating.setFont(fontIter)
        self.calculating.clicked.connect(self.isCheckFunction)

        self.method.setFont(fontIter)
        
        self.title = QLabel("Виберіть межі та похибку", self)
        self.title.move(230, 200)
        self.title.setFixedSize(170, 40)
        self.title.setFont(fontIter)

        self.limitA = QTextEdit(self)
        self.limitA.move(130, 250)
        self.limitA.setFixedSize(100, 40)
        self.limitA.setPlaceholderText("Межа А: 1")
        self.limitA.setPlainText(str(1))

        self.limitB = QTextEdit(self)
        self.limitB.move(250, 250)
        self.limitB.setFixedSize(100, 40)
        self.limitB.setPlaceholderText("Межа В: 2")
        self.limitB.setPlainText(str(2))

        self.h_step = QTextEdit(self)
        self.h_step.move(370, 250)
        self.h_step.setFixedSize(100, 40)
        self.h_step.setPlaceholderText("Крок h: 0.01")
        self.h_step.setPlainText(str(0.01))

    def fx1(self, x, y):
        sec_x = 1/np.cos(x)
        return sec_x - y * np.tan(x)

    def isCheckFunction(self):
        try:
            a = float(self.limitA.toPlainText())
            b = float(self.limitB.toPlainText())
            h = float(self.h_step.toPlainText())
        except ValueError:
            print("Invalid input values. Please enter numeric values for limits and epsilon.")
            return

        
        if self.runge_kutta.isChecked() and self.firstEq.isChecked():
            runge(a, b, h, self.fx1)
        else:
            eyler(a, b, h, self.fx1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
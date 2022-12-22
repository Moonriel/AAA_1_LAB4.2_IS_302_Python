import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.btn_v.clicked.connect(self.solve)
        self.btn_c.clicked.connect(self.clear)

    def flatten(self, l):
        return [item for sublist in l for item in sublist]

    def split(self, s, size):
        return [s[i:i + size] for i in range(0, len(s), size)]

    def solve(self):
        self.textEdit_dst.clear()
        text = self.textEdit_src.toPlainText()  
        AB = text.split("$")
        ch = [self.split(p, 60) for p in AB]
        for s in self.flatten(ch):
            self.textEdit_dst.insertPlainText(s+"\n")

    def clear(self):
        self.textEdit_src.clear()
        self.textEdit_dst.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
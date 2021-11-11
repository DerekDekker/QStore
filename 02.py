from PySide6 import QtWidgets,QtGui,QtCore
import sys

def __init__(self):
    for i in range(0,10):
        self._numberButtons += [QtWidgets.QPushButton(str(i), self)]
        self.connect(self._numberButtons[i], SIGNAL('clicked()'), lambda : self._number(i))

def _number(self, x):
    print(x)
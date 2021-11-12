import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
import random
from PyQt5.QtGui import QFont
from .ui import AppUi


class AppWidget(QWidget, AppUi):
    def __init__(self, name, describe, img):
        super(AppWidget, self).__init__()
        self.name = name
        self.describe = describe
        self.img = img

        self.ui(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = AppWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

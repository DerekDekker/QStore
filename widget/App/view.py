import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
import random
from PyQt5.QtGui import QFont
from .ui import AppUi
from PySide6.QtCore import Signal


class AppWidget(QWidget, AppUi):

    def __init__(self, app_clicked_signal, **kwargs):
        super(AppWidget, self).__init__()
        self.id = kwargs['id']  # ID
        self.name = kwargs['name']  # 名称
        self.describe = kwargs['describe']  # 介绍
        self.img = kwargs['img']  # 图片
        self.website = kwargs['website']  # 官网

        self.app_clicked_signal = app_clicked_signal  # 信号

        self.ui(self)

    def mousePressEvent(self, e):
        self.app_clicked_signal.emit(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = AppWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

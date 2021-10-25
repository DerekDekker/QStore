import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QGridLayout
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
import random
from PyQt5.QtGui import QFont
from widget.App.view import AppWidget


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setStyleSheet("background-color: #292929;")

        self.q_layout = QGridLayout(self)

        self.pagination = 4

        self.app_widget_list = []
        for app_widget in range(16):
            self.app_widget_list.append(AppWidget())
            self.q_layout.addWidget(self.app_widget_list[-1], int(app_widget/self.pagination), app_widget-(int(app_widget/self.pagination)*self.pagination))
            print(self.app_widget_list[-1].size())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = MainWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环


import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QGridLayout
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
import random
from PyQt5.QtGui import QFont
from widget.App.view import AppWidget
from Nav.view import NavWidget
from utils.FileQss import FileQss


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setObjectName('MainWidget')
        self.setWindowIcon(QtGui.QIcon('../../media/image/tor-browser-zh_icon.svg'))
        qssStyle = FileQss.readQSS('../../static/qss/main.qss')
        self.setStyleSheet(qssStyle)

        q_widget = QWidget()
        self.setCentralWidget(q_widget)


        # 布局 水平
        self.h_layout = QHBoxLayout(q_widget)
        self.h_layout.setContentsMargins(0, 0, 0, 0)

        # 布局 网格
        self.q_layout = QGridLayout()

        # 菜单
        nav_widget = NavWidget()

        self.pagination = 4

        self.app_widget_list = []
        for app_widget in range(16):
            self.app_widget_list.append(AppWidget())
            self.q_layout.addWidget(self.app_widget_list[-1], int(app_widget/self.pagination), app_widget-(int(app_widget/self.pagination)*self.pagination))

        # 水平布局 添加 网格布局
        self.h_layout.addWidget(nav_widget)
        self.h_layout.addLayout(self.q_layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = MainWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环


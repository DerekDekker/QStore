import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QGridLayout, QPushButton
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
import random
from PySide6.QtGui import QIcon
from PySide6 import QtCore
from widget.Menu.view import MenuWidget
from utils.CommonHelper import CommonHelper
from utils.FileQss import FileQss
import sqlite3


class NavWidget(QMainWindow):
    def __init__(self):
        super(NavWidget, self).__init__()
        qssStyle = FileQss.readQSS('../../static/qss/nav.qss')
        self.setStyleSheet(qssStyle)

        q_widget = QWidget()
        self.setCentralWidget(q_widget)

        self.setFixedWidth(150)

        # 布局 垂直
        self.V_layout = QVBoxLayout(q_widget)
        self.V_layout.setContentsMargins(0, 0, 0, 0)
        self.V_layout.setSpacing(0)
        self.setContentsMargins(6, 3, 6, 0)


        c = sqlite3.connect('../../QStore.db')
        cursor = c.execute('SELECT * FROM column')

        # 数据库
        self.menu_widget_list = {}
        for cursor_obj in cursor:
            # 菜单
            self.menu_widget_list[cursor_obj[0]] = MenuWidget()
            self.menu_widget_list[cursor_obj[0]].setText(cursor_obj[1])
            self.menu_widget_list[cursor_obj[0]].svg.load(f'../../media/image/{cursor_obj[3]}')
            # 布局 添加 标签
            self.V_layout.addWidget(self.menu_widget_list[cursor_obj[0]])

        self.V_layout.addStretch(1)

        # 菜单
        # self.menu_widget = MenuWidget()
        # self.menu_widget.nav_menu.setText('网络应用')
        # self.menu_widget.svg.load('../../media/image/etcher_icon_32d6b781.svg')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = NavWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

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


class NavWidget(QWidget):
    def __init__(self):
        super(NavWidget, self).__init__()
        qssStyle = FileQss.readQSS('../../static/qss/nav.qss')
        self.setStyleSheet(qssStyle)


        self.setMinimumWidth(150)
        self.setObjectName('x')

        # q_widget = QWidget()
        # q_widget.setStyleSheet("border-right: 1px solid #ddd;")

        # 布局 垂直
        self.V_layout = QVBoxLayout(self)
        self.V_layout.setContentsMargins(0, 0, 0, 0)
        self.V_layout.setSpacing(0)

        # 菜单
        menu_widget = MenuWidget()
        menu_widget.nav_menu.setText('网络应用')
        menu_widget2 = MenuWidget()
        menu_widget2.nav_menu.setText('社交共通')
        menu_widget3 = MenuWidget()
        menu_widget3.nav_menu.setText('音乐欣赏')

        # self.setCentralWidget(q_widget)

        # 布局 添加 标签
        self.V_layout.addWidget(menu_widget)
        self.V_layout.addWidget(menu_widget2)
        self.V_layout.addWidget(menu_widget3)
        self.V_layout.addStretch(1)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = NavWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

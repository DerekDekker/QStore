import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
import random
from PyQt5.QtGui import QFont
from PySide6.QtGui import QIcon
from PySide6 import QtCore


class MenuWidget(QWidget):
    def __init__(self):
        super(MenuWidget, self).__init__()
        self.setMinimumWidth(40)
        self.setMinimumWidth(140)

        # 布局 水平
        self.h_layout = QHBoxLayout(self)
        self.h_layout.setContentsMargins(20, 0, 0, 0)

        # 图标
        svg = QtSvgWidgets.QSvgWidget('../../media/image/anaconda2-install_icon.svg')
        svg.setFixedSize(20, 20)

        # 标签
        self.nav_menu = QLabel('网络应用')
        self.nav_menu.setFixedHeight(35)
        self.nav_menu.setStyleSheet('color:#cecece;font-size:14px;font-family: "Liberation Serif";')

        # 布局 添加 标签
        self.h_layout.addWidget(svg)
        self.h_layout.addWidget(self.nav_menu)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = MenuWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

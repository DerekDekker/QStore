import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QGridLayout, QScrollArea, QGraphicsBlurEffect, QSplitter
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
import random
from PySide6.QtGui import QIcon
from PySide6 import QtCore
from widget.Menu.view import MenuWidget
from utils.CommonHelper import CommonHelper
from utils.FileQss import FileQss
from widget.App.view import AppWidget


class DetailWidget(QWidget):
    def __init__(self, app_obj):
        super(DetailWidget, self).__init__()

        # 布局 垂直
        self.q_layout = QVBoxLayout(self)

        # 图片
        self.svg = QtSvgWidgets.QSvgWidget(f'../../media/image/{app_obj.img}')
        self.svg.setFixedSize(240, 240)
        self.q_layout.addWidget(self.svg, 0, Qt.AlignCenter | Qt.AlignBottom)

        # 标题
        title_label = QLabel(app_obj.name)
        title_label.setStyleSheet('color:#cecece;font-size:48px;font-family: "Liberation Serif";')
        self.q_layout.addWidget(title_label, 0, Qt.AlignCenter | Qt.AlignTop)

        # 官网
        website = QLabel(f'官网: {app_obj.website}')
        website.setStyleSheet('color:#969696;font-size:18px;font-family: "Liberation Serif";')
        self.q_layout.addWidget(website, 1, Qt.AlignCenter | Qt.AlignTop)

        # 介绍
        describe = QLabel(app_obj.describe)
        describe.setWordWrap(True)
        describe.setStyleSheet('color:#969696;font-size:18px;font-family: "Liberation Serif";padding: 0px;margin: 0px;')
        self.q_layout.addWidget(describe, 3,  Qt.AlignCenter | Qt.AlignTop)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = DetailWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

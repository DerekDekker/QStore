import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QGridLayout, QScrollArea, QGraphicsBlurEffect
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
import random
from PySide6.QtGui import QIcon
from PySide6 import QtCore
from widget.Menu.view import MenuWidget
from utils.CommonHelper import CommonHelper
from utils.FileQss import FileQss
from widget.App.view import AppWidget


class BodyWidget(QWidget):
    def __init__(self, pagination=1):
        super(BodyWidget, self).__init__()

        # 布局 网格
        self.q_layout = QGridLayout(self)

        self.pagination = pagination
        # self.pagination = 4

        for app_widget in range(30):
            self.q_layout.addWidget(AppWidget(), int(app_widget/self.pagination), app_widget-(int(app_widget/self.pagination)*self.pagination))






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = BodyWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环
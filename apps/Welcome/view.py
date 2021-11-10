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


class WelcomeWidget(QWidget):
    def __init__(self):
        super(WelcomeWidget, self).__init__()


        # 布局 垂直
        self.q_layout = QVBoxLayout(self)

        title_label = QLabel('欢迎使用QStore')
        title_label.setStyleSheet('color:#cecece;font-size:48px;font-family: "Liberation Serif";')

        self.q_layout.addWidget(title_label, 0, Qt.AlignCenter)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = WelcomeWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

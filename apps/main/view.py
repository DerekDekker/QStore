import sys
from PySide6 import QtWidgets, QtGui, Qt, QtSvgWidgets
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QMainWindow, QGridLayout, QScrollArea, QStackedWidget
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtCore import Qt
from widget.App.view import AppWidget
from Nav.view import NavWidget
from utils.FileQss import FileQss
from BlurWindow.blurWindow import GlobalBlur
from utils.FlowLayout import FlowLayout
from Body.view import BodyWidget
from PySide6.QtCore import Slot
from Welcome.view import WelcomeWidget
from functools import partial


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setObjectName('MainWidget')
        self.setWindowIcon(QtGui.QIcon('../../media/image/tor-browser-zh_icon.svg'))
        self.setWindowTitle('应用商店')
        qssStyle = FileQss.readQSS('../../static/qss/main.qss')
        self.setStyleSheet(qssStyle)
        self.setObjectName('MainWidget')
        self.resize(1100, 600)

        # 毛玻璃
        self.setAttribute(Qt.WA_TranslucentBackground)
        GlobalBlur(self.winId(), Dark=True)

        q_widget = QWidget()
        self.setCentralWidget(q_widget)

        # 布局 水平
        self.h_layout = QHBoxLayout(q_widget)
        self.h_layout.setContentsMargins(0, 0, 0, 0)

        # 菜单
        nav_widget = NavWidget()

        # 滚动区域
        self.scroll = QScrollArea()  # 滚动条 控件
        self.scroll.setWidgetResizable(True)  # 适应高度
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏横向滚动条
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏纵向滚动条
        self.scroll.lineWidth()

        # 水平布局 添加 网格布局
        self.h_layout.addWidget(nav_widget)
        self.h_layout.addWidget(self.scroll)

        # 堆栈窗口
        self.stacked_widget = QStackedWidget()

        self.scroll.setWidget(self.stacked_widget)  # 滚动区域 添加 堆栈窗口

        # 欢迎界面
        welcome_widget = WelcomeWidget()
        self.stacked_widget.addWidget(welcome_widget)  # 堆栈窗口 添加 主窗体

        # 信号
        for menu_widget_list_obj in nav_widget.menu_widget_list:
            nav_widget.menu_widget_list[menu_widget_list_obj].clicked.connect(partial(self.menu_slot, menu_widget_list_obj))

    @Slot()
    def menu_slot(self, column_id):
        # 主窗体
        body_widget3 = BodyWidget(column_id)
        self.stacked_widget.addWidget(body_widget3)  # 堆栈窗口 添加 主窗体
        self.stacked_widget.setCurrentWidget(body_widget3)  # 堆栈窗口 显示 主窗体


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = MainWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环


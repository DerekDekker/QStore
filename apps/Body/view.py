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
import sqlite3
from PySide6.QtCore import Signal
from PySide6.QtCore import Slot


class BodyWidget(QWidget):
    app_clicked_signal = Signal(object)

    def __init__(self, column_id):
        super(BodyWidget, self).__init__()

        # 布局 网格
        self.q_layout = QGridLayout(self)

        self.pagination = 3

        c = sqlite3.connect('../../QStore.db')
        cursor = c.execute(f'SELECT id, name, describe, img, website FROM app WHERE column_id={column_id}')

        app_widget_dict = {}
        count = 0
        for cursor_obj in cursor:
            app_widget_dict[cursor_obj[0]] = AppWidget(app_clicked_signal=self.app_clicked_signal, id=cursor_obj[0], name=cursor_obj[1], describe=cursor_obj[2], img=cursor_obj[3], website=cursor_obj[4])
            self.q_layout.addWidget(app_widget_dict[cursor_obj[0]], int(count/self.pagination), count-(int(count/self.pagination)*self.pagination), 1, 1, Qt.AlignTop)
            # app_widget_dict[cursor_obj[0]].clicked.connect(lambda: app_clicked())

            count += 1

        c.close()

        # 伸展器
        self.main_splitter = QSplitter(Qt.Vertical)
        self.q_layout.addWidget(self.main_splitter, )



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = BodyWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

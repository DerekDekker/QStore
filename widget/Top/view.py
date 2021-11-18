import sys
from PySide6 import QtWidgets, Qt, QtSvgWidgets
from PySide6.QtWidgets import QLabel, QHBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt
from utils.FileQss import FileQss


class TopWidget(QWidget):
    def __init__(self):
        super(TopWidget, self).__init__()
        self.setMinimumWidth(40)
        self.setMinimumWidth(140)
        qssStyle = FileQss.readQSS('../../static/qss/nav.qss')
        self.setStyleSheet(qssStyle)

        # 布局 水平
        self.h_layout = QHBoxLayout(self)

        # 最小化
        self.minimize = QtSvgWidgets.QSvgWidget(f'../../static/image/minimize.svg')
        self.h_layout.addWidget(self.minimize)
        # 最大化
        self.maximize = QtSvgWidgets.QSvgWidget(f'../../static/image/maximize.svg')
        self.h_layout.addWidget(self.maximize)
        # 关闭
        self.closure = QtSvgWidgets.QSvgWidget(f'../../static/image/closure.svg')
        self.h_layout.addWidget(self.closure)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = TopWidget()  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环

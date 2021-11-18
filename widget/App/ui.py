from PySide6 import Qt, QtSvgWidgets
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt


class AppUi(object):
    def ui(self, AppWidget):
        AppWidget.setGeometry(300, 200, 650, 350)
        # AppWidget.setStyleSheet("background-color: #292929;")

        # 布局
        b_layout = QHBoxLayout(AppWidget)

        # 应用Logo
        self.svg = QtSvgWidgets.QSvgWidget(f'../../media/image/{AppWidget.img}')
        self.svg.setMinimumWidth(120)
        self.svg.setMinimumHeight(120)
        self.svg.setMaximumWidth(120)
        self.svg.setMaximumHeight(120)

        # 标题
        self.title = QLabel(f'{AppWidget.name}')
        self.title.setStyleSheet('color:#cecece;letter-spacing:2px;font-size:24px;font-family: "Liberation Serif";')

        # 内容
        self.content = QLabel(AppWidget.describe[:90])
        self.content.setStyleSheet('color:#c7c7c7;font-weight: 400;font-family: "Noto Serif CJK JP";')
        self.content.setWordWrap(True)

        b_layout.addWidget(self.svg, 1, Qt.AlignTop)
        v_loxLayout = QVBoxLayout()
        b_layout.addLayout(v_loxLayout)
        v_loxLayout.addWidget(self.title, 1, Qt.AlignTop)
        v_loxLayout.addWidget(self.content, 2, Qt.AlignTop)



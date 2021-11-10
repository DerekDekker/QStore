from PySide6 import QtCore, QtWidgets


class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent=None)

        # if parent is not None:
        #     self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True


    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        width = self.geometry().width() - 2 * self.contentsMargins().top()
        minWidth, minHeight = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        # print('minimumSize', width, minWidth, minHeight)

        size = QtCore.QSize(minWidth, minHeight)
        margin, _, _, _ = self.getContentsMargins()

        size += QtCore.QSize(2 * margin, 2 * margin)
        print(size)
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0
        maxLineWidth = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(
                QtWidgets.QSizePolicy.PushButton,
                QtWidgets.QSizePolicy.PushButton,
                QtCore.Qt.Horizontal
            )
            spaceY = self.spacing() + wid.style().layoutSpacing(
                QtWidgets.QSizePolicy.PushButton,
                QtWidgets.QSizePolicy.PushButton,
                QtCore.Qt.Vertical
            )
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                maxLineWidth = max(x - rect.x(),
                                   maxLineWidth,
                                   item.sizeHint().width())
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(
                    QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint())
                )

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return maxLineWidth, y + lineHeight - rect.y()

class TestWindow(QtWidgets.QMainWindow):
    ''' Minimal working example of the FlowLayout. '''
    qtObjectName = "FlowLayout_Test_Window"

    def __init__(self, parent):
        super(TestWindow, self).__init__(parent)
        self.setObjectName(self.qtObjectName)
        self.setWindowTitle('FlowLayout Test')
        self.setCentralWidget(QtWidgets.QWidget(self))
        flowLayout = FlowLayout()
        for text in ("Lorem ipsum dolor sit amet, consectetur adipiscing "
                     "elit. Ut eu metus ultricies, laoreet erat ut, 1111111111111111111111pharetra "
                     "nunc. Suspendisse ultrices sem et sapien congue mattis."
                     ).split():
            flowLayout.addWidget(QtWidgets.QPushButton(text))
        self.centralWidget().setLayout(flowLayout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  # 创建类实例
    window = TestWindow(None)  # 创建窗口
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 进入主循环
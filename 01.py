from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap

app = QApplication([])
Label = QLabel()

PixMap = QPixmap("media/image/librecad_icon.svg")            #注意不要把这行放到实例化app对象的上面，会无效
Label.setPixmap(PixMap)

Label.show()
app.exec_()
# 5
import random
import sys

from classifier import is_bad_posture
from PySide6 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hack posture app"]

        self.button = QtWidgets.QPushButton("Check my posture!")
        self.button.setCheckable(True)
        self.button.toggle()
        self.button.clicked.connect(self.check_button_state)

        self.text = QtWidgets.QLabel(
            "Hack posture app", alignment=QtCore.Qt.AlignCenter
        )

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

    def check_button_state(self):
        if self.button.isChecked():
            print("Button is pressed!")
        else:
            print("None")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

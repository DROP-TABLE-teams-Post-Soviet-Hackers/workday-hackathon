import random
import sys
from threading import Thread
from test2 import posture_checker
from classifier import is_bad_posture
from PySide6 import QtCore, QtGui, QtWidgets
from starter_ai import start, stop
from loader import event


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.setCheckable(True)
        self.start_button.toggle()
        self.start_button.clicked.connect(self.check_start_button)

        self.stop_button = QtWidgets.QPushButton("Stop")
        self.stop_button.setCheckable(True)
        self.stop_button.toggle()
        self.stop_button.clicked.connect(self.check_stop_button)

        self.text = QtWidgets.QLabel(
            "Check my posture!", alignment=QtCore.Qt.AlignCenter
        )

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

    def check_start_button(self) -> None:
        if self.start_button.isChecked():
            start()

    def check_stop_button(self)-> None:
        if self.stop_button.isChecked():
            event.set()
            stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

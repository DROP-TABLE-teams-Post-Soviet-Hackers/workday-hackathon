import random
import sys

from classifier import is_bad_posture
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from starter_ai import start, stop


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Add an image
        self.image_label = QLabel(self)
        pixmap = QPixmap(
            "/Users/ianmiller/workday-hackathon-2024/model/hack-posture-logo.jpg"
        )
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.setCheckable(True)
        self.start_button.toggle()
        self.start_button.clicked.connect(self.check_start_button)

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.setCheckable(True)
        self.start_button.toggle()
        self.start_button.clicked.connect(self.check_start_button)

        self.stop_button = QtWidgets.QPushButton("Stop")
        self.stop_button.setCheckable(True)
        self.stop_button.toggle()
        self.stop_button.clicked.connect(self.check_stop_button)

        self.text = QtWidgets.QLabel("H4ck P0stur3", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

    def check_start_button(self) -> None:
        if self.start_button.isChecked():
            start()

    def check_stop_button(self) -> None:
        if self.stop_button.isChecked():
            stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


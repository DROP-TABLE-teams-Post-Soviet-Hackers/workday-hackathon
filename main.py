from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json

import ui.settingsWindow

import sys


class MainDialog(QMainWindow, ui.settingsWindow.Ui_SettingsWindow):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        with open("config.json", "r") as f:
            data = json.load(f)

        self.distanceSelector.setValue(data["distance"])
        self.distanceLabel.setText(str(data["distance"]) + " cm")
        self.windowOption.setChecked(not bool(data["type"]))
        self.builtinOption.setChecked(bool(data["type"]))

        self.distanceSelector.valueChanged.connect(self.updateDistance)

        self.saveBtn.clicked.connect(self.save)
        self.cancelBtn.clicked.connect(self.close)

    def updateDistance(self):
        self.distanceLabel.setText(str(self.distanceSelector.value()) + " cm")

    def save(self):
        configData = {
            "distance": self.distanceSelector.value(),
            "type": 0 if self.windowOption.isChecked() else 1
        }

        with open('config.json', 'w') as f:
            json.dump(configData, f)

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()

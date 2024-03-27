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

        self.frequencySelector.setValue(data["frequency"])
        self.frequencyLabel.setText(str(data["frequency"]) + " ms")
        self.windowOption.setChecked(not bool(data["type"]))
        self.builtinOption.setChecked(bool(data["type"]))

        self.frequencySelector.valueChanged.connect(self.updateFrequency)

        self.saveBtn.clicked.connect(self.save)
        self.cancelBtn.clicked.connect(self.close)

    def updateFrequency(self):
        self.frequencyLabel.setText(str(self.frequencySelector.value()) + " ms")

    def save(self):
        configData = {
            "frequency": self.frequencySelector.value(),
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

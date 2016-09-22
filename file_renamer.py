#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Renamer
#
# Author: Simon Lachaîne


import sys
from PyQt4 import QtCore, QtGui

import ui_file_renamer as main_frame


MA_RESOLUTIONS = [
    "1920x1080",
    "1280x720",
]


MEZZ_RESOLUTIONS = [
    "1280x720",
    "720x480",
]


CUSTOM_RESOLUTIONS = [
    "1920x1080",
    "1280x720",
    "720x480",
]


class FileRenamerApp(QtGui.QMainWindow, main_frame.Ui_FileRenamerWindow):
    def __init__(self, parent=None):
        super(FileRenamerApp, self).__init__(parent)

        self.setupUi(self)

        self.title_line.textChanged.connect(self.set_title)
        self.reel_line.textChanged.connect(self.set_reel)

        self.default_ma.toggled.connect(self.set_default_ma)
        self.default_mezz.toggled.connect(self.set_default_mezz)
        self.default_custom.toggled.connect(self.set_default_custom)

        self.resolution_combo.currentIndexChanged.connect(self.set_resolution)
        self.resolution_combo.currentIndexChanged.connect(self.set_resolution)
        self.resolution_combo.currentIndexChanged.connect(self.set_resolution)

        self.default_ma.toggle()

        self.show()

    def set_title(self):
        self.results_line.insert(self.title_line.text())

    def set_reel(self):
        self.results_line.insert(self.title_line.text())

    def set_default_ma(self):
        self.resolution_combo.clear()
        self.resolution_combo.addItems(MA_RESOLUTIONS)

    def set_default_mezz(self):
        self.resolution_combo.clear()
        self.resolution_combo.addItems(MEZZ_RESOLUTIONS)

    def set_default_custom(self):
        self.resolution_combo.clear()
        self.resolution_combo.addItems(CUSTOM_RESOLUTIONS)

    def set_resolution(self):
        pass


def main():
    app = QtGui.QApplication(sys.argv)
    gui = FileRenamerApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

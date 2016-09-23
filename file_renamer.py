#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Renamer
#
# Author: Simon Lachaîne


import sys
from collections import OrderedDict
from PyQt4 import QtCore, QtGui

import ui_file_renamer as main_frame
import app_lists


filename = OrderedDict([
    ("title", ""),
    ("reel", ""),
    ("resolution", ""),
    ("extension", ""),
])


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
        self.extension_combo.currentIndexChanged.connect(self.set_extension)

        self.default_ma.toggle()

        self.show()

    def set_title(self):
        filename["title"] = self.title_line.text()
        self.set_results()

    def set_reel(self):
        filename["reel"] = self.reel_line.text()
        self.set_results()

    def set_default_ma(self):
        self.resolution_combo.clear()
        self.resolution_combo.addItems(app_lists.MA_RESOLUTIONS)
        self.extension_combo.clear()
        self.extension_combo.addItems(app_lists.CUSTOM_EXTENSIONS)

    def set_default_mezz(self):
        self.resolution_combo.clear()
        self.resolution_combo.addItems(app_lists.MEZZ_RESOLUTIONS)
        self.extension_combo.clear()
        self.extension_combo.addItems(app_lists.CUSTOM_EXTENSIONS)

    def set_default_custom(self):
        self.resolution_combo.clear()
        self.resolution_combo.addItems([(tup[0]) for tup in app_lists.CUSTOM_RESOLUTIONS])
        self.extension_combo.clear()
        self.extension_combo.addItems(app_lists.CUSTOM_EXTENSIONS)

    def set_resolution(self):
        try:
            filename["resolution"] = \
            [y for x, y, z in app_lists.CUSTOM_RESOLUTIONS if x == self.resolution_combo.currentText()][0]
            self.set_results()

        except IndexError:
            return

    def set_extension(self):
        filename["extension"] = self.extension_combo.currentText()
        self.set_results()

    def set_results(self):
        self.results_line.clear()
        for key in filename.keys():
            self.results_line.insert(filename[key])


def main():
    app = QtGui.QApplication(sys.argv)
    gui = FileRenamerApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

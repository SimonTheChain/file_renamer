#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Renamer
#
# Author: Simon Lachaîne



import sys
from PyQt4 import QtCore, QtGui

import ui_file_renamer as main_frame


class FileRenamerApp(QtGui.QMainWindow, main_frame.Ui_MainWindow):
    def __init__(self, parent=None):
        super(FileRenamerApp, self).__init__(parent)

        self.setupUi(self)

        self.title_line.textChanged.connect(self.set_title)
        self.reel_line.textChanged.connect(self.set_reel)

        self.default_ma.toggled.connect(self.set_default_ma)
        self.default_mezz.toggled.connect(self.set_default_mezz)
        self.default_custom.toggled.connect(self.set_default_custom)

        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    gui = FileRenamerApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

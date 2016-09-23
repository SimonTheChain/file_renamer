#!/usr/bin/python
# -*- coding: utf-8 -*-

# Filename Creator
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

        self.copy_btn.clicked.connect(self.copy_filename)

        self.default_ma.toggle()

        self.show()

    def set_default_ma(self):
        temp_resolution = self.resolution_combo.currentText()
        self.resolution_combo.clear()
        self.resolution_combo.addItems(app_lists.MA_RESOLUTIONS)

        if temp_resolution in [self.resolution_combo.itemText(i) for i in range(self.resolution_combo.count())]:
            index_resolution = self.resolution_combo.findText(temp_resolution)
            self.resolution_combo.setCurrentIndex(index_resolution)

        temp_extension = self.extension_combo.currentText()
        self.extension_combo.clear()
        self.extension_combo.addItems(app_lists.CUSTOM_EXTENSIONS)

        if temp_extension in [self.extension_combo.itemText(i) for i in range(self.extension_combo.count())]:
            index_extension = self.extension_combo.findText(temp_extension)
            self.extension_combo.setCurrentIndex(index_extension)

        self.set_title()
        self.set_reel()

    def set_default_mezz(self):
        temp_resolution = self.resolution_combo.currentText()
        self.resolution_combo.clear()
        self.resolution_combo.addItems(app_lists.MEZZ_RESOLUTIONS)

        if temp_resolution in [self.resolution_combo.itemText(i) for i in range(self.resolution_combo.count())]:
            index_resolution = self.resolution_combo.findText(temp_resolution)
            self.resolution_combo.setCurrentIndex(index_resolution)

        temp_extension = self.extension_combo.currentText()
        self.extension_combo.clear()
        self.extension_combo.addItems(app_lists.CUSTOM_EXTENSIONS)
        
        if temp_extension in [self.extension_combo.itemText(i) for i in range(self.extension_combo.count())]:
            index_extension = self.extension_combo.findText(temp_extension)
            self.extension_combo.setCurrentIndex(index_extension)

        self.set_title()
        self.set_reel()

    def set_default_custom(self):
        temp_resolution = self.resolution_combo.currentText()
        self.resolution_combo.clear()
        self.resolution_combo.addItems([(tup[0]) for tup in app_lists.CUSTOM_RESOLUTIONS])

        if temp_resolution in [self.resolution_combo.itemText(i) for i in range(self.resolution_combo.count())]:
            index_resolution = self.resolution_combo.findText(temp_resolution)
            self.resolution_combo.setCurrentIndex(index_resolution)

        temp_extension = self.extension_combo.currentText()
        self.extension_combo.clear()
        self.extension_combo.addItems(app_lists.CUSTOM_EXTENSIONS)

        if temp_extension in [self.extension_combo.itemText(i) for i in range(self.extension_combo.count())]:
            index_extension = self.extension_combo.findText(temp_extension)
            self.extension_combo.setCurrentIndex(index_extension)

        self.set_title()
        self.set_reel()

    def set_title(self):
        if self.default_ma.isChecked():
            filename["title"] = str(self.title_line.text()).upper().replace(" ", "") + "_"

        elif self.default_mezz.isChecked():
            filename["title"] = str(self.title_line.text()).lower().replace(" ", "")

        elif self.default_custom.isChecked():
            filename["title"] = self.title_line.text()

        return self.set_results()

    def set_reel(self):
        if self.default_ma.isChecked():
            filename["reel"] = str(self.reel_line.text()).replace(" ", "") + "_"

        elif self.default_mezz.isChecked():
            filename["reel"] = str(self.reel_line.text()).replace(" ", "")

        elif self.default_custom.isChecked():
            filename["reel"] = self.reel_line.text()

        return self.set_results()

    def set_resolution(self):
        if self.default_ma.isChecked():
            try:
                filename["resolution"] = \
                    [y for x, y, z in app_lists.CUSTOM_RESOLUTIONS if x == self.resolution_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return

        elif self.default_mezz.isChecked():
            try:
                filename["resolution"] = \
                    [z for x, y, z in app_lists.CUSTOM_RESOLUTIONS if x == self.resolution_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return

        elif self.default_custom.isChecked():
            try:
                filename["resolution"] = \
                [x for x, y, z in app_lists.CUSTOM_RESOLUTIONS if x == self.resolution_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return

    def set_extension(self):
        filename["extension"] = self.extension_combo.currentText()

        return self.set_results()

    def set_results(self):
        self.results_line.clear()
        for key in filename.keys():
            self.results_line.insert(filename[key])

        if self.default_ma.isChecked():
            self.validate_ma()

        if self.default_mezz.isChecked():
            self.validate_mezz()

        if self.default_custom.isChecked():
            self.validate_custom()

    def validate_ma(self):
        self.validation_text.clear()

        if filename["title"] == "_":
            self.validation_text.appendPlainText("Title missing.")

        if filename["reel"] == "_":
            self.validation_text.appendPlainText("Reel # missing.")

        else:
            try:
                int(filename["reel"].replace("_", ""))

            except ValueError:
                self.validation_text.appendPlainText("Reel # is not a valid number.")

        self.character_count()

    def validate_mezz(self):
        self.validation_text.clear()

        if not filename["title"]:
            self.validation_text.appendPlainText("Title missing.")

        if not filename["reel"]:
            self.validation_text.appendPlainText("Reel # missing.")

        else:
            try:
                int(filename["reel"])

            except ValueError:
                self.validation_text.appendPlainText("Reel # is not a valid number.")

        self.character_count()

    def validate_custom(self):
        self.validation_text.clear()

        if not filename["title"]:
            self.validation_text.appendPlainText("Title missing.")

        if not filename["reel"]:
            self.validation_text.appendPlainText("Reel # missing.")

        else:
            try:
                int(filename["reel"])

            except ValueError:
                self.validation_text.appendPlainText("Reel # is not a valid number.")

        self.character_count()

    def copy_filename(self):
        clipboard = QtGui.QApplication.clipboard()
        clipboard.clear()
        clipboard.setText(self.results_line.text())

    def character_count(self):
        self.lcd.display(len(self.results_line.text()))


def main():
    app = QtGui.QApplication(sys.argv)
    gui = FileRenamerApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

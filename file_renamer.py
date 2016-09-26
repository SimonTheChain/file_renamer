#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Renamer
#
# Author: Simon Lachaîne


import os
import sys
from collections import OrderedDict

from PyQt4 import QtCore, QtGui

import app_lists
import ui_file_renamer as main_frame

filename = OrderedDict([
    ("title", ""),
    ("year", ""),
    ("notes", ""),
    ("content", ""),
    ("reel", ""),
    ("resolution", ""),
    ("audio_config", ""),
    ("extension", ""),
])


class FileRenamerApp(QtGui.QMainWindow, main_frame.Ui_FileRenamerWindow):
    def __init__(self, parent=None):
        super(FileRenamerApp, self).__init__(parent)

        self.config_count = 0
        self.audio_configs = OrderedDict()

        self.setupUi(self)

        self.default_ma.toggled.connect(self.set_default_ma)
        self.default_mezz.toggled.connect(self.set_default_mezz)
        self.default_custom.toggled.connect(self.set_default_custom)

        self.title_line.textChanged.connect(self.set_title)
        self.year_lbl.dateChanged.connect(self.set_year)
        self.notes_combo.currentIndexChanged.connect(self.set_notes)
        self.content_combo.currentIndexChanged.connect(self.set_content)
        self.reel_line.textChanged.connect(self.set_reel)
        self.resolution_combo.currentIndexChanged.connect(self.set_resolution)
        self.extension_combo.currentIndexChanged.connect(self.set_extension)
        self.add_config_btn.clicked.connect(self.add_audio)
        self.del_config_btn.clicked.connect(self.del_audio)

        self.copy_btn.clicked.connect(self.copy_filename)

        self.default_ma.toggle()

        self.show()

    def set_default_ma(self):
        temp_notes = self.notes_combo.currentText()
        self.notes_combo.clear()
        self.notes_combo.addItems([(tup[0]) for tup in app_lists.CUSTOM_NOTES])

        if temp_notes in [self.notes_combo.itemText(i) for i in range(self.notes_combo.count())]:
            index_notes = self.notes_combo.findText(temp_notes)
            self.notes_combo.setCurrentIndex(index_notes)

        temp_content = self.content_combo.currentText()
        self.content_combo.clear()
        self.content_combo.addItems([(tup[0]) for tup in app_lists.CUSTOM_CONTENT])

        if temp_content in [self.content_combo.itemText(i) for i in range(self.content_combo.count())]:
            index_content = self.content_combo.findText(temp_content)
            self.content_combo.setCurrentIndex(index_content)
        
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
        self.set_year()
        self.set_reel()

    def set_default_mezz(self):
        temp_notes = self.notes_combo.currentText()
        self.notes_combo.clear()
        self.notes_combo.addItems([(tup[0]) for tup in app_lists.CUSTOM_NOTES])

        if temp_notes in [self.notes_combo.itemText(i) for i in range(self.notes_combo.count())]:
            index_notes = self.notes_combo.findText(temp_notes)
            self.notes_combo.setCurrentIndex(index_notes)

        temp_content = self.content_combo.currentText()
        self.content_combo.clear()
        self.content_combo.addItems([(tup[0]) for tup in app_lists.CUSTOM_CONTENT])

        if temp_content in [self.content_combo.itemText(i) for i in range(self.content_combo.count())]:
            index_content = self.content_combo.findText(temp_content)
            self.content_combo.setCurrentIndex(index_content)

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
        self.set_year()
        self.set_reel()

    def set_default_custom(self):
        temp_notes = self.notes_combo.currentText()
        self.notes_combo.clear()
        self.notes_combo.addItems([(tup[0]) for tup in app_lists.CUSTOM_NOTES])

        if temp_notes in [self.notes_combo.itemText(i) for i in range(self.notes_combo.count())]:
            index_notes = self.notes_combo.findText(temp_notes)
            self.notes_combo.setCurrentIndex(index_notes)

        temp_content = self.content_combo.currentText()
        self.content_combo.clear()
        self.content_combo.addItems([(tup[0]) for tup in app_lists.CUSTOM_CONTENT])

        if temp_content in [self.content_combo.itemText(i) for i in range(self.content_combo.count())]:
            index_content = self.content_combo.findText(temp_content)
            self.content_combo.setCurrentIndex(index_content)

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
        self.set_year()
        self.set_reel()

    def set_title(self):
        if self.default_ma.isChecked():
            filename["title"] = str(self.title_line.text()).upper().replace(" ", "") + "_"

        elif self.default_mezz.isChecked():
            filename["title"] = str(self.title_line.text()).lower().replace(" ", "")

        elif self.default_custom.isChecked():
            filename["title"] = self.title_line.text()

        return self.set_results()

    def set_year(self):
        filename["year"] = str(self.year_lbl.date().toPyDate())[:4]

        return self.set_results()

    def set_notes(self):
        if self.default_ma.isChecked():
            try:
                filename["notes"] = \
                    [y for x, y, z in app_lists.CUSTOM_NOTES if x == self.notes_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return

        elif self.default_mezz.isChecked():
            try:
                filename["notes"] = \
                    [z for x, y, z in app_lists.CUSTOM_NOTES if x == self.notes_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return

        elif self.default_custom.isChecked():
            try:
                filename["notes"] = \
                [x for x, y, z in app_lists.CUSTOM_NOTES if x == self.notes_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return
    
    def set_content(self):
        if self.default_ma.isChecked():
            try:
                filename["content"] = \
                    [y for x, y, z in app_lists.CUSTOM_CONTENT if x == self.content_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return

        elif self.default_mezz.isChecked():
            try:
                filename["content"] = \
                    [z for x, y, z in app_lists.CUSTOM_CONTENT if x == self.content_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return

        elif self.default_custom.isChecked():
            try:
                filename["content"] = \
                [x for x, y, z in app_lists.CUSTOM_CONTENT if x == self.content_combo.currentText()][0]
                self.set_results()

            except IndexError:
                return
    
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

    def add_audio(self):
        box = QtGui.QComboBox(self)
        box.addItems([(tup[0]) for tup in sorted(app_lists.AUDIO_CONFIGS)])
        box.setObjectName("config%d" % self.config_count)
        box.currentIndexChanged.connect(self.set_audio_signal)
        index_audio = box.findText("5.1 Surround", QtCore.Qt.MatchFixedString)
        box.setCurrentIndex(index_audio)

        self.audio_lyt.addWidget(box, 0, self.config_count)
        self.config_count = len(self.audio_configs.keys())

    def del_audio(self):
        if self.audio_lyt.count() > 0:
            to_delete = self.audio_lyt.takeAt(self.audio_lyt.count() - 1)

            widget = to_delete.widget()
            if widget:
                widget.deleteLater()

        if len(self.audio_configs.keys()) > 0:
            self.audio_configs.pop(self.audio_configs.keys()[-1])

        self.config_count = len(self.audio_configs.keys())

        return self.set_audio_config()

    def set_audio_signal(self):
        sender = self.sender()
        self.audio_configs.update({str(sender.objectName()): str(sender.currentText())})

        return self.set_audio_config()

    def set_audio_config(self):
        filename["audio_config"] = ""
        for index in range(len(self.audio_configs.values())):
            filename["audio_config"] += \
            [y for x, y in app_lists.AUDIO_CONFIGS if x == self.audio_configs.values()[index]][0] + "_"

        return self.set_results()

    def set_results(self):
        temp_filename = ""
        self.results_line.clear()

        for key in filename.keys():
            temp_filename += str(filename[key])

        if os.path.splitext(temp_filename)[0].endswith("_"):
            final_filename = os.path.splitext(temp_filename)[0][:-1] + filename["extension"]

        else:
            final_filename = temp_filename

        self.results_line.insert(final_filename)

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

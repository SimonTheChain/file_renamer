#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Renamer
#
# Author: Simon Lachaîne


import datetime
import os
import re
import sys
from PyQt4 import QtCore, QtGui
from collections import OrderedDict

import app_lists
import ui_file_renamer as main_frame
import file_renamer_about as about_dlg

filename = OrderedDict([
    ("title", ""),
    ("year", ""),
    ("notes", ""),
    ("content", ""),
    ("trailer_nb", ""),
    ("trailer_pass", ""),
    ("season_nb", ""),
    ("episode_nb", ""),
    ("codec", ""),
    ("resolution", ""),
    ("ratio", ""),
    ("speed", ""),
    ("audio_language", ""),
    ("audio_config", ""),
    ("sub_language", ""),
    ("sub_notes", ""),
    ("reel", ""),
    ("date", ""),
    ("facility", ""),
    ("version", ""),
    ("extension", ""),
])


filename_mezz = OrderedDict([
    ("title", ""),
    ("notes", ""),
    ("content", ""),
    ("trailer_nb", ""),
    ("trailer_pass", ""),
    ("season_nb", ""),
    ("episode_nb", ""),
    ("codec", ""),
    ("resolution", ""),
    ("ratio", ""),
    ("speed", ""),
    ("audio_language", ""),
    ("audio_config", ""),
    ("sub_language", ""),
    ("date", ""),
    ("version", ""),
    ("extension", ""),
])


class AboutDlg(QtGui.QDialog, about_dlg.Ui_About):
    def __init__(self, parent=None):
        super(AboutDlg, self).__init__(parent)

        self.setupUi(self)


class FileRenamerApp(QtGui.QMainWindow, main_frame.Ui_FileRenamerWindow):
    def __init__(self, parent=None):
        super(FileRenamerApp, self).__init__(parent)

        # sets up the audio configs
        self.config_count = 0
        self.audio_configs = OrderedDict()

        self.setupUi(self)

        # gets the current date
        filename["date"] = str(datetime.date.today()).replace("-", "") + "-"
        filename_mezz["date"] = str(datetime.date.today()).replace("-", "") + "_"

        # connects the widgets to functions
        self.actionAbout.triggered.connect(self.about_dlg)
        self.actionQuit.triggered.connect(self.quit_fcn)

        self.default_ma.toggled.connect(self.set_default_ma)
        self.default_mezz.toggled.connect(self.set_default_mezz)

        self.title_line.textChanged.connect(self.set_title)
        self.year_lbl.dateChanged.connect(self.set_year)
        self.notes_combo.currentIndexChanged.connect(self.set_notes)
        self.content_combo.currentIndexChanged.connect(self.set_content)
        self.trailer_nb_line.textChanged.connect(self.set_trailer_nb)
        self.trailer_pass_line.textChanged.connect(self.set_trailer_pass)
        self.season_nb_line.textChanged.connect(self.set_season_nb)
        self.episode_nb_line.textChanged.connect(self.set_episode_nb)
        self.reel_line.textChanged.connect(self.set_reel)
        self.codec_combo.currentIndexChanged.connect(self.set_codec)
        self.speed_combo.currentIndexChanged.connect(self.set_speed)
        self.audio_language_combo.currentIndexChanged.connect(self.set_audio_language)
        self.sub_language_combo.currentIndexChanged.connect(self.set_sub_language)
        self.sub_notes_combo.currentIndexChanged.connect(self.set_sub_notes)
        self.resolution_combo.currentIndexChanged.connect(self.set_resolution)
        self.ratio_combo.currentIndexChanged.connect(self.set_ratio)
        self.version_line.textChanged.connect(self.set_version)
        self.extension_combo.currentIndexChanged.connect(self.set_extension)
        self.facility_combo.currentIndexChanged.connect(self.set_facility)
        self.add_config_btn.clicked.connect(self.add_audio)
        self.del_config_btn.clicked.connect(self.del_audio)

        self.results_line.textChanged.connect(self.character_count)
        self.copy_btn.clicked.connect(self.copy_filename)

        # need to activate this prior to showing the ui
        self.default_ma.toggle()

        # sets the default values
        self.reel_line.setText("0")
        self.version_line.setText("v1r0")
        index_codec_default = self.codec_combo.findText("ProRes 422 HQ")
        self.codec_combo.setCurrentIndex(index_codec_default)
        index_ratio_default = self.ratio_combo.findText("1.78:1")
        self.ratio_combo.setCurrentIndex(index_ratio_default)
        index_audio_language_default = self.audio_language_combo.findText("English (United States)")
        self.audio_language_combo.setCurrentIndex(index_audio_language_default)

        self.show()

    @staticmethod
    def about_dlg():
        about = AboutDlg()
        about.exec_()

    def quit_fcn(self):
        self.close()

    def set_default_ma(self):
        self.year_lbl.setEnabled(True)
        self.sub_notes_combo.setEnabled(True)
        self.reel_line.setEnabled(True)
        self.facility_combo.setEnabled(True)
        self.version_line.setEnabled(False)

        temp_notes = self.notes_combo.currentText()
        self.notes_combo.clear()
        self.notes_combo.addItems([(tup[0]) for tup in app_lists.NOTES])

        if temp_notes in [self.notes_combo.itemText(i) for i in range(self.notes_combo.count())]:
            index_notes = self.notes_combo.findText(temp_notes)
            self.notes_combo.setCurrentIndex(index_notes)

        temp_content = self.content_combo.currentText()
        self.content_combo.clear()
        self.content_combo.addItems([(tup[0]) for tup in app_lists.CONTENT])

        if temp_content in [self.content_combo.itemText(i) for i in range(self.content_combo.count())]:
            index_content = self.content_combo.findText(temp_content)
            self.content_combo.setCurrentIndex(index_content)

        temp_codec = self.codec_combo.currentText()
        self.codec_combo.clear()
        self.codec_combo.addItems([(tup[0]) for tup in app_lists.CODECS])

        if temp_codec in [self.codec_combo.itemText(i) for i in range(self.codec_combo.count())]:
            index_codec = self.codec_combo.findText(temp_codec)
            self.codec_combo.setCurrentIndex(index_codec)

        temp_resolution = self.resolution_combo.currentText()
        self.resolution_combo.clear()
        self.resolution_combo.addItems([(tup[0]) for tup in app_lists.RESOLUTIONS])

        if temp_resolution in [self.resolution_combo.itemText(i) for i in range(self.resolution_combo.count())]:
            index_resolution = self.resolution_combo.findText(temp_resolution)
            self.resolution_combo.setCurrentIndex(index_resolution)

        temp_ratio = self.ratio_combo.currentText()
        self.ratio_combo.clear()
        self.ratio_combo.addItems([(tup[0]) for tup in app_lists.RATIOS])

        if temp_ratio in [self.ratio_combo.itemText(i) for i in range(self.ratio_combo.count())]:
            index_ratio = self.ratio_combo.findText(temp_ratio)
            self.ratio_combo.setCurrentIndex(index_ratio)

        temp_speed = self.speed_combo.currentText()
        self.speed_combo.clear()
        self.speed_combo.addItems([(tup[0]) for tup in app_lists.SPEED])

        if temp_speed in [self.speed_combo.itemText(i) for i in range(self.speed_combo.count())]:
            index_speed = self.speed_combo.findText(temp_speed)
            self.speed_combo.setCurrentIndex(index_speed)

        temp_audio_language = self.audio_language_combo.currentText()
        self.audio_language_combo.clear()
        self.audio_language_combo.addItems([(tup[0]) for tup in app_lists.LANGUAGES])

        if temp_audio_language in [self.audio_language_combo.itemText(i) for i in range(self.audio_language_combo.count())]:
            index_audio_language = self.audio_language_combo.findText(temp_audio_language)
            self.audio_language_combo.setCurrentIndex(index_audio_language)

        temp_sub_language = self.sub_language_combo.currentText()
        self.sub_language_combo.clear()
        self.sub_language_combo.addItems([(tup[0]) for tup in app_lists.LANGUAGES])

        if temp_sub_language in [self.sub_language_combo.itemText(i) for i in
                                   range(self.sub_language_combo.count())]:
            index_sub_language = self.sub_language_combo.findText(temp_sub_language)
            self.sub_language_combo.setCurrentIndex(index_sub_language)

        temp_sub_notes = self.sub_notes_combo.currentText()
        self.sub_notes_combo.clear()
        self.sub_notes_combo.addItems([(tup[0]) for tup in app_lists.SUB_NOTES])

        if temp_sub_notes in [self.sub_notes_combo.itemText(i) for i in
                                   range(self.sub_notes_combo.count())]:
            index_sub_notes = self.sub_notes_combo.findText(temp_sub_notes)
            self.sub_notes_combo.setCurrentIndex(index_sub_notes)

        temp_facility = self.facility_combo.currentText()
        self.facility_combo.clear()
        self.facility_combo.addItems([(tup[0]) for tup in app_lists.FACILITY])

        if temp_facility in [self.facility_combo.itemText(i) for i in
                              range(self.facility_combo.count())]:
            index_facility = self.facility_combo.findText(temp_facility)
            self.facility_combo.setCurrentIndex(index_facility)

        temp_extension = self.extension_combo.currentText()
        self.extension_combo.clear()
        self.extension_combo.addItems(app_lists.EXTENSIONS)

        if temp_extension in [self.extension_combo.itemText(i) for i in range(self.extension_combo.count())]:
            index_extension = self.extension_combo.findText(temp_extension)
            self.extension_combo.setCurrentIndex(index_extension)

        self.set_title()
        self.set_reel()
        self.set_year()

    def set_default_mezz(self):
        self.year_lbl.setEnabled(False)
        self.sub_notes_combo.setEnabled(False)
        self.reel_line.setEnabled(False)
        self.facility_combo.setEnabled(False)
        self.version_line.setEnabled(True)

        temp_notes = self.notes_combo.currentText()
        self.notes_combo.clear()
        self.notes_combo.addItems([(tup[0]) for tup in app_lists.NOTES])

        if temp_notes in [self.notes_combo.itemText(i) for i in range(self.notes_combo.count())]:
            index_notes = self.notes_combo.findText(temp_notes)
            self.notes_combo.setCurrentIndex(index_notes)

        temp_content = self.content_combo.currentText()
        self.content_combo.clear()
        self.content_combo.addItems([(tup[0]) for tup in app_lists.CONTENT])

        if temp_content in [self.content_combo.itemText(i) for i in range(self.content_combo.count())]:
            index_content = self.content_combo.findText(temp_content)
            self.content_combo.setCurrentIndex(index_content)

        temp_codec = self.codec_combo.currentText()
        self.codec_combo.clear()
        self.codec_combo.addItems([(tup[0]) for tup in app_lists.CODECS])

        if temp_codec in [self.codec_combo.itemText(i) for i in range(self.codec_combo.count())]:
            index_codec = self.codec_combo.findText(temp_codec)
            self.codec_combo.setCurrentIndex(index_codec)

        temp_resolution = self.resolution_combo.currentText()
        self.resolution_combo.clear()
        self.resolution_combo.addItems([(tup[0]) for tup in app_lists.RESOLUTIONS])

        if temp_resolution in [self.resolution_combo.itemText(i) for i in range(self.resolution_combo.count())]:
            index_resolution = self.resolution_combo.findText(temp_resolution)
            self.resolution_combo.setCurrentIndex(index_resolution)

        temp_ratio = self.ratio_combo.currentText()
        self.ratio_combo.clear()
        self.ratio_combo.addItems([(tup[0]) for tup in app_lists.RATIOS])

        if temp_ratio in [self.ratio_combo.itemText(i) for i in range(self.ratio_combo.count())]:
            index_ratio = self.ratio_combo.findText(temp_ratio)
            self.ratio_combo.setCurrentIndex(index_ratio)

        temp_speed = self.speed_combo.currentText()
        self.speed_combo.clear()
        self.speed_combo.addItems([(tup[0]) for tup in app_lists.SPEED])

        if temp_speed in [self.speed_combo.itemText(i) for i in range(self.speed_combo.count())]:
            index_speed = self.speed_combo.findText(temp_speed)
            self.speed_combo.setCurrentIndex(index_speed)

        temp_extension = self.extension_combo.currentText()
        self.extension_combo.clear()
        self.extension_combo.addItems(app_lists.EXTENSIONS)

        temp_audio_language = self.audio_language_combo.currentText()
        self.audio_language_combo.clear()
        self.audio_language_combo.addItems([(tup[0]) for tup in app_lists.LANGUAGES])

        if temp_audio_language in [self.audio_language_combo.itemText(i) for i in
                                   range(self.audio_language_combo.count())]:
            index_audio_language = self.audio_language_combo.findText(temp_audio_language)
            self.audio_language_combo.setCurrentIndex(index_audio_language)

        temp_sub_language = self.sub_language_combo.currentText()
        self.sub_language_combo.clear()
        self.sub_language_combo.addItems([(tup[0]) for tup in app_lists.LANGUAGES])

        if temp_sub_language in [self.sub_language_combo.itemText(i) for i in
                                 range(self.sub_language_combo.count())]:
            index_sub_language = self.sub_language_combo.findText(temp_sub_language)
            self.sub_language_combo.setCurrentIndex(index_sub_language)

        temp_sub_notes = self.sub_notes_combo.currentText()
        self.sub_notes_combo.clear()
        self.sub_notes_combo.addItems([(tup[0]) for tup in app_lists.SUB_NOTES])

        if temp_sub_notes in [self.sub_notes_combo.itemText(i) for i in
                              range(self.sub_notes_combo.count())]:
            index_sub_notes = self.sub_notes_combo.findText(temp_sub_notes)
            self.sub_notes_combo.setCurrentIndex(index_sub_notes)

        temp_facility = self.facility_combo.currentText()
        self.facility_combo.clear()
        self.facility_combo.addItems([(tup[0]) for tup in app_lists.FACILITY])

        if temp_facility in [self.facility_combo.itemText(i) for i in
                             range(self.facility_combo.count())]:
            index_facility = self.facility_combo.findText(temp_facility)
            self.facility_combo.setCurrentIndex(index_facility)

        if temp_extension in [self.extension_combo.itemText(i) for i in range(self.extension_combo.count())]:
            index_extension = self.extension_combo.findText(temp_extension)
            self.extension_combo.setCurrentIndex(index_extension)

        self.set_title()

    def set_title(self):
        filename["title"] = str(self.title_line.text()).upper().replace(" ", "") + "_"
        filename_mezz["title"] = str(self.title_line.text()).lower().replace(" ", "_") + "_"

        return self.set_results()

    def set_year(self):
        filename["year"] = str(self.year_lbl.date().toPyDate())[:4] + "_"

        return self.set_results()

    def set_notes(self):
        try:
            filename["notes"] = \
                [y for x, y, z in app_lists.NOTES if x == self.notes_combo.currentText()][0] + "_"
            filename_mezz["notes"] = \
                [z for x, y, z in app_lists.NOTES if x == self.notes_combo.currentText()][0] + "_"

        except IndexError:
            return

        if filename["notes"] == "_":
            filename["notes"] = ""

        if filename_mezz["notes"] == "_":
            filename_mezz["notes"] = ""

        return self.set_results()

    def set_content(self):
        try:
            filename["content"] = \
                [y for x, y, z in app_lists.CONTENT if x == self.content_combo.currentText()][0]

            filename_mezz["content"] = \
                [z for x, y, z in app_lists.CONTENT if x == self.content_combo.currentText()][0] + "_"

            if filename["content"] == "FTR" or filename_mezz["content"] == "ftr_":
                self.trailer_nb_line.setEnabled(False)
                self.trailer_pass_line.setEnabled(False)
                self.season_nb_line.setEnabled(False)
                self.episode_nb_line.setEnabled(False)

            else:
                self.trailer_nb_line.setEnabled(True)
                self.trailer_pass_line.setEnabled(True)
                self.season_nb_line.setEnabled(True)
                self.episode_nb_line.setEnabled(True)

            self.set_results()

        except IndexError:
            return

    def set_trailer_nb(self):
        filename["trailer_nb"] = str(self.trailer_nb_line.text())
        filename_mezz["trailer_nb"] = str(self.trailer_nb_line.text())

        return self.set_results()

    def set_trailer_pass(self):
        filename["trailer_pass"] = str(self.trailer_pass_line.text())
        filename_mezz["trailer_pass"] = str(self.trailer_pass_line.text())

        return self.set_results()

    def set_season_nb(self):
        filename["season_nb"] = str(self.season_nb_line.text())
        filename_mezz["season_nb"] = str(self.season_nb_line.text())

        return self.set_results()

    def set_episode_nb(self):
        filename["episode_nb"] = str(self.episode_nb_line.text())
        filename_mezz["episode_nb"] = str(self.episode_nb_line.text())

        return self.set_results()

    def set_reel(self):
        filename["reel"] = "R" + str(self.reel_line.text()).replace(" ", "") + "_"

        return self.set_results()

    def set_codec(self):
        try:
            filename["codec"] = \
                [y for x, y in app_lists.CODECS if x == self.codec_combo.currentText()][0] + "_"
            filename_mezz["codec"] = \
                [y for x, y in app_lists.CODECS if x == self.codec_combo.currentText()][0].lower() + "_"
            self.set_results()

        except IndexError:
            return

    def set_speed(self):
        try:
            filename["speed"] = \
                [y for x, y in app_lists.SPEED if x == self.speed_combo.currentText()][0] + "_"
            filename_mezz["speed"] = \
                [y for x, y in app_lists.SPEED if x == self.speed_combo.currentText()][0] + "_"
            self.set_results()

        except IndexError:
            return

    def set_audio_language(self):
        try:
            filename["audio_language"] = \
                [y for x, y, z in app_lists.LANGUAGES if x == self.audio_language_combo.currentText()][0] + "_"
            filename_mezz["audio_language"] = \
                [z for x, y, z in app_lists.LANGUAGES if x == self.audio_language_combo.currentText()][0] + "_"
            self.set_results()

        except IndexError:
            return

    def set_sub_language(self):
        try:
            filename["sub_language"] = \
                [z for x, y, z in app_lists.LANGUAGES if x == self.sub_language_combo.currentText()][0] + "_"
            filename_mezz["sub_language"] = \
                [y for x, y, z in app_lists.LANGUAGES if x == self.sub_language_combo.currentText()][0] + "_"
            self.set_results()

        except IndexError:
            return

    def set_sub_notes(self):
        try:
            filename["sub_notes"] = \
                [y for x, y in app_lists.SUB_NOTES if x == self.sub_notes_combo.currentText()][0] + "_"

        except IndexError:
            return

        if filename["sub_notes"] == "_":
            filename["sub_notes"] = ""

        return self.set_results()

    def set_resolution(self):
        try:
            filename["resolution"] = \
                [y for x, y, z in app_lists.RESOLUTIONS if x == self.resolution_combo.currentText()][0] + "-"
            filename_mezz["resolution"] = \
                [z for x, y, z in app_lists.RESOLUTIONS if x == self.resolution_combo.currentText()][0]
            self.set_results()

        except IndexError:
            return

    def set_ratio(self):
        try:
            filename["ratio"] = \
                [y for x, y in app_lists.RATIOS if x == self.ratio_combo.currentText()][0] + "_"
            filename_mezz["ratio"] = \
                [y for x, y in app_lists.RATIOS if x == self.ratio_combo.currentText()][0] + "_"
            self.set_results()

        except IndexError:
            return

    def set_version(self):
        filename_mezz["version"] = str(self.version_line.text()).lower()

        return self.set_results()

    def set_extension(self):
        filename["extension"] = self.extension_combo.currentText()
        filename_mezz["extension"] = self.extension_combo.currentText()

        return self.set_results()

    def set_facility(self):
        try:
            filename["facility"] = \
                [y for x, y in app_lists.FACILITY if x == unicode(self.facility_combo.currentText())][0]
            self.set_results()

        except IndexError:
            return

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
            [y for x, y in app_lists.AUDIO_CONFIGS if x == self.audio_configs.values()[index]][0] + "-"

        filename_mezz["audio_config"] = ""
        for index in range(len(self.audio_configs.values())):
            filename_mezz["audio_config"] += \
                [y for x, y in app_lists.AUDIO_CONFIGS if x == self.audio_configs.values()[index]][0] + "-"
        head, sep, tail = filename_mezz["audio_config"].rpartition("-")
        filename_mezz["audio_config"] = head + "_"

        return self.set_results()

    def set_results(self):
        if self.default_ma.isChecked():
            temp_filename = ""
            self.results_line.clear()

            if not filename["trailer_nb"]:
                if filename["content"].endswith("-"):
                    filename["content"] = filename["content"][:-1]
                    filename["content"] += "_"

                elif filename["content"].endswith("_"):
                    pass

                else:
                    filename["content"] += "_"

            else:
                if filename["content"].endswith("_"):
                    filename["content"] = filename["content"][:-1]
                    filename["content"] += "-"

            for key in filename.keys():
                temp_filename += str(filename[key])

            if os.path.splitext(temp_filename)[0].endswith("_"):
                final_filename = os.path.splitext(temp_filename)[0][:-1] + filename["extension"]

            else:
                final_filename = temp_filename

            self.results_line.insert(final_filename)

            return self.validate_ma()

        elif self.default_mezz.isChecked():
            temp_filename = ""
            self.results_line.clear()

            if not filename_mezz["trailer_nb"]:
                if filename_mezz["content"].endswith("-"):
                    filename_mezz["content"] = filename_mezz["content"][:-1]
                    filename_mezz["content"] += "_"

                elif filename_mezz["content"].endswith("_"):
                    pass

                else:
                    filename_mezz["content"] += "_"

            else:
                if filename_mezz["content"].endswith("_"):
                    filename_mezz["content"] = filename_mezz["content"][:-1]
                    filename_mezz["content"] += "-"

            for key in filename_mezz.keys():
                temp_filename += str(filename_mezz[key])

            if os.path.splitext(temp_filename)[0].endswith("_"):
                final_filename = os.path.splitext(temp_filename)[0][:-1] + filename_mezz["extension"]

            else:
                final_filename = temp_filename

            self.results_line.insert(final_filename)

            return self.validate_mezz()

    def validate_ma(self):
        self.validation_text.clear()

        if filename["title"] == "_":
            self.validation_text.appendPlainText("Title missing.")

        if filename["reel"] == "R_":
            self.validation_text.appendPlainText("Reel # missing.")

        elif not re.match("^R[0-9]+_$", filename["reel"]):
            self.validation_text.appendPlainText("Reel # is not a valid number.")

        self.character_count()

    def validate_mezz(self):
        self.validation_text.clear()

        if filename_mezz["title"] == "_":
            self.validation_text.appendPlainText("Title missing.")

        if not filename_mezz["version"]:
            self.validation_text.appendPlainText("Version missing.")

        elif not re.match("^v[0-9]+r[0-9]+$", filename_mezz["version"]):
            self.validation_text.appendPlainText("Version not valid; must be 'v#r#'.")

        self.character_count()

    def copy_filename(self):
        clipboard = QtGui.QApplication.clipboard()
        clipboard.clear()
        clipboard.setText(self.results_line.text())

    def character_count(self):
        self.lcd.display(len(self.results_line.text()))

        if len(self.results_line.text()) > 99:
            self.validation_text.appendPlainText("Warning: the filename exceeds 99 characters.")


def main():
    app = QtGui.QApplication(sys.argv)
    gui = FileRenamerApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

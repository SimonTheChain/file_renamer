# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_renamer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FileRenamerWindow(object):
    def setupUi(self, FileRenamerWindow):
        FileRenamerWindow.setObjectName(_fromUtf8("FileRenamerWindow"))
        FileRenamerWindow.resize(999, 540)
        self.centralwidget = QtGui.QWidget(FileRenamerWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.results_line = QtGui.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.results_line.setFont(font)
        self.results_line.setReadOnly(False)
        self.results_line.setObjectName(_fromUtf8("results_line"))
        self.horizontalLayout_3.addWidget(self.results_line)
        self.copy_btn = QtGui.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.copy_btn.setFont(font)
        self.copy_btn.setObjectName(_fromUtf8("copy_btn"))
        self.horizontalLayout_3.addWidget(self.copy_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.validation_text = QtGui.QPlainTextEdit(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validation_text.sizePolicy().hasHeightForWidth())
        self.validation_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.validation_text.setFont(font)
        self.validation_text.setReadOnly(True)
        self.validation_text.setObjectName(_fromUtf8("validation_text"))
        self.verticalLayout_3.addWidget(self.validation_text)
        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 2)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.title_line = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_line.sizePolicy().hasHeightForWidth())
        self.title_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_line.setFont(font)
        self.title_line.setObjectName(_fromUtf8("title_line"))
        self.horizontalLayout.addWidget(self.title_line)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_3 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_7.addWidget(self.label_3)
        self.reel_line = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reel_line.sizePolicy().hasHeightForWidth())
        self.reel_line.setSizePolicy(sizePolicy)
        self.reel_line.setObjectName(_fromUtf8("reel_line"))
        self.horizontalLayout_7.addWidget(self.reel_line)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_8.addWidget(self.label_4)
        self.resolution_combo = QtGui.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resolution_combo.setFont(font)
        self.resolution_combo.setObjectName(_fromUtf8("resolution_combo"))
        self.horizontalLayout_8.addWidget(self.resolution_combo)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.extension_combo = QtGui.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.extension_combo.setFont(font)
        self.extension_combo.setObjectName(_fromUtf8("extension_combo"))
        self.horizontalLayout_2.addWidget(self.extension_combo)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.default_ma = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.default_ma.setFont(font)
        self.default_ma.setChecked(False)
        self.default_ma.setObjectName(_fromUtf8("default_ma"))
        self.horizontalLayout_5.addWidget(self.default_ma)
        self.default_mezz = QtGui.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.default_mezz.setFont(font)
        self.default_mezz.setObjectName(_fromUtf8("default_mezz"))
        self.horizontalLayout_5.addWidget(self.default_mezz)
        self.default_custom = QtGui.QRadioButton(self.groupBox)
        self.default_custom.setChecked(True)
        self.default_custom.setObjectName(_fromUtf8("default_custom"))
        self.horizontalLayout_5.addWidget(self.default_custom)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 1, 1, 1)
        FileRenamerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FileRenamerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        FileRenamerWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FileRenamerWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FileRenamerWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(FileRenamerWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(FileRenamerWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(FileRenamerWindow)
        QtCore.QMetaObject.connectSlotsByName(FileRenamerWindow)

    def retranslateUi(self, FileRenamerWindow):
        FileRenamerWindow.setWindowTitle(_translate("FileRenamerWindow", "Filename Creator", None))
        self.copy_btn.setText(_translate("FileRenamerWindow", "Copy", None))
        self.label.setText(_translate("FileRenamerWindow", "Title", None))
        self.label_3.setText(_translate("FileRenamerWindow", "Reel #", None))
        self.label_4.setText(_translate("FileRenamerWindow", "Resolution", None))
        self.label_2.setText(_translate("FileRenamerWindow", "Extension", None))
        self.groupBox.setTitle(_translate("FileRenamerWindow", "Platform", None))
        self.default_ma.setText(_translate("FileRenamerWindow", "MediAffinity", None))
        self.default_mezz.setText(_translate("FileRenamerWindow", "Mezz", None))
        self.default_custom.setText(_translate("FileRenamerWindow", "Custom", None))
        self.menuFile.setTitle(_translate("FileRenamerWindow", "File", None))
        self.actionAbout.setText(_translate("FileRenamerWindow", "About", None))
        self.actionQuit.setText(_translate("FileRenamerWindow", "Quit", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_prefs\RnD\maya\python\Export\pw_MayaToHoudiniChannelExport\widgets\channelExportWindow.ui'
#
# Created: Thu Jul 17 10:09:35 2014
#      by: PyQt4 UI code generator 4.11
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

class Ui_channelExportWindow(object):
    def setupUi(self, channelExportWindow):
        channelExportWindow.setObjectName(_fromUtf8("channelExportWindow"))
        channelExportWindow.resize(432, 596)
        self.centralwidget = QtGui.QWidget(channelExportWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.tree_ly = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.tree_ly.setMargin(0)
        self.tree_ly.setObjectName(_fromUtf8("tree_ly"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addSelectedObject_btn = QtGui.QPushButton(self.groupBox)
        self.addSelectedObject_btn.setObjectName(_fromUtf8("addSelectedObject_btn"))
        self.verticalLayout.addWidget(self.addSelectedObject_btn)
        self.addFromChannelBox_btn = QtGui.QPushButton(self.groupBox)
        self.addFromChannelBox_btn.setObjectName(_fromUtf8("addFromChannelBox_btn"))
        self.verticalLayout.addWidget(self.addFromChannelBox_btn)
        self.addFromSet_btn = QtGui.QPushButton(self.groupBox)
        self.addFromSet_btn.setObjectName(_fromUtf8("addFromSet_btn"))
        self.verticalLayout.addWidget(self.addFromSet_btn)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.saveToSet_btn = QtGui.QPushButton(self.groupBox_3)
        self.saveToSet_btn.setObjectName(_fromUtf8("saveToSet_btn"))
        self.verticalLayout_5.addWidget(self.saveToSet_btn)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.removeSelected_btn = QtGui.QPushButton(self.groupBox_2)
        self.removeSelected_btn.setObjectName(_fromUtf8("removeSelected_btn"))
        self.verticalLayout_2.addWidget(self.removeSelected_btn)
        self.removeAll_btn = QtGui.QPushButton(self.groupBox_2)
        self.removeAll_btn.setObjectName(_fromUtf8("removeAll_btn"))
        self.verticalLayout_2.addWidget(self.removeAll_btn)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.info_lb = QtGui.QLabel(self.layoutWidget)
        self.info_lb.setObjectName(_fromUtf8("info_lb"))
        self.verticalLayout_3.addWidget(self.info_lb)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.splitter)
        self.outFile_ly = QtGui.QHBoxLayout()
        self.outFile_ly.setObjectName(_fromUtf8("outFile_ly"))
        self.verticalLayout_4.addLayout(self.outFile_ly)
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scale_ly = QtGui.QHBoxLayout()
        self.scale_ly.setObjectName(_fromUtf8("scale_ly"))
        self.gridLayout_2.addLayout(self.scale_ly, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout.setContentsMargins(4, 5, 4, 4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.endRange_spb = QtGui.QSpinBox(self.groupBox_4)
        self.endRange_spb.setMinimum(-999999999)
        self.endRange_spb.setMaximum(999999999)
        self.endRange_spb.setObjectName(_fromUtf8("endRange_spb"))
        self.gridLayout.addWidget(self.endRange_spb, 0, 2, 1, 1)
        self.startRange_spb = QtGui.QSpinBox(self.groupBox_4)
        self.startRange_spb.setMinimum(-999999999)
        self.startRange_spb.setMaximum(999999999)
        self.startRange_spb.setObjectName(_fromUtf8("startRange_spb"))
        self.gridLayout.addWidget(self.startRange_spb, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.currentTimeToEnd_btn = QtGui.QPushButton(self.groupBox_4)
        self.currentTimeToEnd_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.currentTimeToEnd_btn.setObjectName(_fromUtf8("currentTimeToEnd_btn"))
        self.gridLayout.addWidget(self.currentTimeToEnd_btn, 1, 2, 1, 1)
        self.currentTimeToStart_btn = QtGui.QPushButton(self.groupBox_4)
        self.currentTimeToStart_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.currentTimeToStart_btn.setObjectName(_fromUtf8("currentTimeToStart_btn"))
        self.gridLayout.addWidget(self.currentTimeToStart_btn, 1, 1, 1, 1)
        self.setTimeLineRange_btn = QtGui.QPushButton(self.groupBox_4)
        self.setTimeLineRange_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setTimeLineRange_btn.setObjectName(_fromUtf8("setTimeLineRange_btn"))
        self.gridLayout.addWidget(self.setTimeLineRange_btn, 2, 1, 1, 2)
        self.autoRange_cbx = QtGui.QCheckBox(self.groupBox_4)
        self.autoRange_cbx.setObjectName(_fromUtf8("autoRange_cbx"))
        self.gridLayout.addWidget(self.autoRange_cbx, 1, 0, 2, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.batchMode_btn = QtGui.QPushButton(self.centralwidget)
        self.batchMode_btn.setMinimumSize(QtCore.QSize(40, 30))
        self.batchMode_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.batchMode_btn.setObjectName(_fromUtf8("batchMode_btn"))
        self.horizontalLayout.addWidget(self.batchMode_btn)
        self.export_btn = QtGui.QPushButton(self.centralwidget)
        self.export_btn.setMinimumSize(QtCore.QSize(40, 30))
        self.export_btn.setObjectName(_fromUtf8("export_btn"))
        self.horizontalLayout.addWidget(self.export_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.progress_pbr = QtGui.QProgressBar(self.centralwidget)
        self.progress_pbr.setProperty("value", 0)
        self.progress_pbr.setObjectName(_fromUtf8("progress_pbr"))
        self.verticalLayout_4.addWidget(self.progress_pbr)
        self.verticalLayout_4.setStretch(0, 1)
        channelExportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(channelExportWindow)
        QtCore.QObject.connect(self.autoRange_cbx, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.startRange_spb.setDisabled)
        QtCore.QObject.connect(self.autoRange_cbx, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.endRange_spb.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(channelExportWindow)

    def retranslateUi(self, channelExportWindow):
        channelExportWindow.setWindowTitle(_translate("channelExportWindow", "Maya to Houdini channel exporter", None))
        self.groupBox.setTitle(_translate("channelExportWindow", "Add channel", None))
        self.addSelectedObject_btn.setText(_translate("channelExportWindow", "Selected objects", None))
        self.addFromChannelBox_btn.setText(_translate("channelExportWindow", "From Channel Box", None))
        self.addFromSet_btn.setText(_translate("channelExportWindow", "From Set", None))
        self.groupBox_3.setTitle(_translate("channelExportWindow", "Save channels", None))
        self.saveToSet_btn.setText(_translate("channelExportWindow", "To Set", None))
        self.groupBox_2.setTitle(_translate("channelExportWindow", "Remove channel", None))
        self.removeSelected_btn.setText(_translate("channelExportWindow", "Selected", None))
        self.removeAll_btn.setText(_translate("channelExportWindow", "All", None))
        self.info_lb.setText(_translate("channelExportWindow", "Info", None))
        self.groupBox_5.setTitle(_translate("channelExportWindow", "Options", None))
        self.groupBox_4.setTitle(_translate("channelExportWindow", "Range", None))
        self.label.setText(_translate("channelExportWindow", "Range:", None))
        self.currentTimeToEnd_btn.setText(_translate("channelExportWindow", "Current to end ▲ ", None))
        self.currentTimeToStart_btn.setText(_translate("channelExportWindow", "▲ Current to start", None))
        self.setTimeLineRange_btn.setText(_translate("channelExportWindow", "▲     From Time Line    ▲ ", None))
        self.autoRange_cbx.setToolTip(_translate("channelExportWindow", "<html><head/><body><p>Request range from all animation curves in scene and set maximum and minimum to range </p><p>Always On in batch mode</p></body></html>", None))
        self.autoRange_cbx.setText(_translate("channelExportWindow", "AUTO", None))
        self.batchMode_btn.setToolTip(_translate("channelExportWindow", "<html><head/><body><p>1. Open rig scene</p><p>2. Load objects to list</p><p>3. Press Batch ...</p><p>4. Select fbx files</p><p><br/></p><p>Auto will be turn ON</p><p>Out clip file path will same as fbx file path</p></body></html>", None))
        self.batchMode_btn.setText(_translate("channelExportWindow", "Batch...", None))
        self.export_btn.setText(_translate("channelExportWindow", "EXPORT", None))


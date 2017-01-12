#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from centralwidget.ui on Wed Mar  7 09:04:11 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CentralWidget(object):
    def setupUi(self, CentralWidget):
        CentralWidget.setObjectName(_fromUtf8("CentralWidget"))
        CentralWidget.resize(832, 590)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CentralWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(CentralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treeWidget = AkTreeWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setVisible(True)
        self.qwidget_1 = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwidget_1.sizePolicy().hasHeightForWidth())
        self.qwidget_1.setSizePolicy(sizePolicy)
        self.qwidget_1.setObjectName(_fromUtf8("qwidget_1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.qwidget_1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stack = QtGui.QStackedWidget(self.qwidget_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setObjectName(_fromUtf8("stack"))
        self.folderPage = FolderPage()
        self.folderPage.setObjectName(_fromUtf8("folderPage"))
        self.stack.addWidget(self.folderPage)
        self.phrasePage = PhrasePage()
        self.phrasePage.setObjectName(_fromUtf8("phrasePage"))
        self.stack.addWidget(self.phrasePage)
        self.scriptPage = ScriptPage()
        self.scriptPage.setObjectName(_fromUtf8("scriptPage"))
        self.stack.addWidget(self.scriptPage)
        self.verticalLayout.addWidget(self.stack)
        self.verticalLayout_2.addWidget(self.splitter)
        self.listWidget = QtGui.QListWidget(CentralWidget)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_2.addWidget(self.listWidget)

        self.retranslateUi(CentralWidget)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CentralWidget)

    def retranslateUi(self, CentralWidget):
        CentralWidget.setWindowTitle(kdecore.i18n(_fromUtf8("Form")))
        self.treeWidget.headerItem().setText(0, kdecore.i18n(_fromUtf8("Name")))
        self.treeWidget.headerItem().setText(1, kdecore.i18n(_fromUtf8("Abbr.")))
        self.treeWidget.headerItem().setText(2, kdecore.i18n(_fromUtf8("Hotkey")))

from .configwindow import AkTreeWidget, PhrasePage, ScriptPage, FolderPage

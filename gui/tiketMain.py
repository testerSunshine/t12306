# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tiketMain.ui'
#
# Created: Tue Aug 01 21:09:20 2017
#      by: PyQt4 UI code generator 4.11.3
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(836, 573)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(11, 10, 811, 511))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.listView = QtGui.QListView(self.tab_4)
        self.listView.setGeometry(QtCore.QRect(30, 20, 661, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 50, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 100, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 150, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(240, 290, 541, 181))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.checkBox = QtGui.QCheckBox(self.tab_4)
        self.checkBox.setGeometry(QtCore.QRect(240, 270, 91, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_4)
        self.checkBox_2.setGeometry(QtCore.QRect(350, 270, 91, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setTearOffEnabled(False)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        self.menu_4 = QtGui.QMenu(self.menubar)
        self.menu_4.setObjectName(_fromUtf8("menu_4"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.fileOpen = QtGui.QAction(MainWindow)
        self.fileOpen.setObjectName(_fromUtf8("fileOpen"))
        self.closeFile = QtGui.QAction(MainWindow)
        self.closeFile.setObjectName(_fromUtf8("closeFile"))
        self.actionTst = QtGui.QAction(MainWindow)
        self.actionTst.setObjectName(_fromUtf8("actionTst"))
        self.menu.addAction(self.fileOpen)
        self.menu.addAction(self.closeFile)
        self.menu.addAction(self.actionTst)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "易行", None))
        self.pushButton_2.setText(_translate("MainWindow", "创建任务", None))
        self.pushButton_3.setText(_translate("MainWindow", "编辑任务", None))
        self.pushButton_4.setText(_translate("MainWindow", "删除任务", None))
        self.checkBox.setText(_translate("MainWindow", "显示全部日志", None))
        self.checkBox_2.setText(_translate("MainWindow", "显示主要日志", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1", None))
        self.menu.setTitle(_translate("MainWindow", "任务", None))
        self.menu_2.setTitle(_translate("MainWindow", "系统设置", None))
        self.menu_3.setTitle(_translate("MainWindow", "查询订单", None))
        self.menu_4.setTitle(_translate("MainWindow", "帮助", None))
        self.fileOpen.setText(_translate("MainWindow", "打开", None))
        self.fileOpen.setToolTip(_translate("MainWindow", "打开", None))
        self.closeFile.setText(_translate("MainWindow", "关闭", None))
        self.closeFile.setToolTip(_translate("MainWindow", "关闭", None))
        self.actionTst.setText(_translate("MainWindow", "Tst", None))
        self.actionTst.setToolTip(_translate("MainWindow", "Tst", None))


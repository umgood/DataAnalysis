# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 268)
        MainWindow.setStyleSheet("background-color:#efe")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 5, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 6, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 7, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 7, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background:#eee")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 18))
        self.menubar.setStyleSheet("background-color:#eee")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("color:red")
        self.menuFile.setObjectName("menuFile")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setStyleSheet("color:blue")
        self.menuWindow.setObjectName("menuWindow")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        MainWindow.setMenuBar(self.menubar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.actionimport = QtWidgets.QAction(MainWindow)
        self.actionimport.setObjectName("actionimport")
        self.actions = QtWidgets.QAction(MainWindow)
        self.actions.setObjectName("actions")
        self.actionM = QtWidgets.QAction(MainWindow)
        self.actionM.setObjectName("actionM")
        self.actionL = QtWidgets.QAction(MainWindow)
        self.actionL.setObjectName("actionL")
        self.actiongetSUM = QtWidgets.QAction(MainWindow)
        self.actiongetSUM.setObjectName("actiongetSUM")
        self.actionget = QtWidgets.QAction(MainWindow)
        self.actionget.setObjectName("actionget")
        self.actionaddRationButton = QtWidgets.QAction(MainWindow)
        self.actionaddRationButton.setObjectName("actionaddRationButton")
        self.actionFull_Screen = QtWidgets.QAction(MainWindow)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionNormal = QtWidgets.QAction(MainWindow)
        self.actionNormal.setObjectName("actionNormal")
        self.actiongetDatabyInstitutionCode = QtWidgets.QAction(MainWindow)
        self.actiongetDatabyInstitutionCode.setObjectName("actiongetDatabyInstitutionCode")
        self.actiongetDateList = QtWidgets.QAction(MainWindow)
        self.actiongetDateList.setObjectName("actiongetDateList")
        self.actiongetIndex = QtWidgets.QAction(MainWindow)
        self.actiongetIndex.setObjectName("actiongetIndex")
        self.actiongetDataByDate = QtWidgets.QAction(MainWindow)
        self.actiongetDataByDate.setObjectName("actiongetDataByDate")
        self.actionCompareInstitution = QtWidgets.QAction(MainWindow)
        self.actionCompareInstitution.setObjectName("actionCompareInstitution")
        self.actioncompareInnerStorage = QtWidgets.QAction(MainWindow)
        self.actioncompareInnerStorage.setObjectName("actioncompareInnerStorage")
        self.menuFile.addAction(self.actionimport)
        self.menuWindow.addAction(self.actions)
        self.menuWindow.addAction(self.actionM)
        self.menuWindow.addAction(self.actionL)
        self.menuWindow.addAction(self.actionFull_Screen)
        self.menuWindow.addAction(self.actionNormal)
        self.menu.addAction(self.actiongetSUM)
        self.menu.addAction(self.actionget)
        self.menu.addAction(self.actionaddRationButton)
        self.menuFilter.addAction(self.actiongetDatabyInstitutionCode)
        self.menuFilter.addAction(self.actiongetDateList)
        self.menuFilter.addAction(self.actiongetIndex)
        self.menuFilter.addAction(self.actiongetDataByDate)
        self.menuFilter.addAction(self.actionCompareInstitution)
        self.menuFilter.addAction(self.actioncompareInnerStorage)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menu.setTitle(_translate("MainWindow", "SimpleOp"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.actionimport.setText(_translate("MainWindow", "import"))
        self.actions.setText(_translate("MainWindow", "S"))
        self.actionM.setText(_translate("MainWindow", "M"))
        self.actionL.setText(_translate("MainWindow", "L"))
        self.actiongetSUM.setText(_translate("MainWindow", "getSum"))
        self.actionget.setText(_translate("MainWindow", "drawTendency"))
        self.actionaddRationButton.setText(_translate("MainWindow", "addRationButton"))
        self.actionFull_Screen.setText(_translate("MainWindow", "Full_Screen"))
        self.actionNormal.setText(_translate("MainWindow", "Normal"))
        self.actiongetDatabyInstitutionCode.setText(_translate("MainWindow", "getDataByInstitutionCode"))
        self.actiongetDateList.setText(_translate("MainWindow", "getDateList"))
        self.actiongetIndex.setText(_translate("MainWindow", "getIndex"))
        self.actiongetDataByDate.setText(_translate("MainWindow", "getDataByDate"))
        self.actionCompareInstitution.setText(_translate("MainWindow", "compareInstitution"))
        self.actioncompareInnerStorage.setText(_translate("MainWindow", "compareInnerStorage"))


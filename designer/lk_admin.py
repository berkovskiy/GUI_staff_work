# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LK_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LK_admin(object):
    def setupUi(self, LK_admin):
        LK_admin.setObjectName("LK_admin")
        LK_admin.resize(1127, 708)
        self.centralwidget = QtWidgets.QWidget(LK_admin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(500, 90, 611, 571))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 281, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 230, 281, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 300, 281, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 90, 91, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 160, 281, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        LK_admin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LK_admin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
        self.menubar.setObjectName("menubar")
        LK_admin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LK_admin)
        self.statusbar.setObjectName("statusbar")
        LK_admin.setStatusBar(self.statusbar)

        self.retranslateUi(LK_admin)
        QtCore.QMetaObject.connectSlotsByName(LK_admin)

    def retranslateUi(self, LK_admin):
        _translate = QtCore.QCoreApplication.translate
        LK_admin.setWindowTitle(_translate("LK_admin", "MainWindow"))
        self.label.setText(_translate("LK_admin", "Приветствую, Администратор!"))
        self.pushButton.setText(_translate("LK_admin", "Создать пользователя(аккаунт)"))
        self.pushButton_2.setText(_translate("LK_admin", "Удалить пользователя"))
        self.pushButton_3.setText(_translate("LK_admin", "Редактировать карточку пользователя"))
        self.pushButton_4.setText(_translate("LK_admin", "Обновить"))
        self.pushButton_5.setText(_translate("LK_admin", "Создать пользователя(профиль)"))

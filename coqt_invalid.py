# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coqt_invalid.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Invalid_Window(object):
    def setupUi_invalid(self, Invalid_Window):
        Invalid_Window.setObjectName("Invalid_Window")
        Invalid_Window.resize(391, 75)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        Invalid_Window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Invalid_Window.setWindowIcon(icon)
        Invalid_Window.setWindowOpacity(0.93)
        self.centralwidget = QtWidgets.QWidget(Invalid_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 35, 35))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Images/images/error.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-100, -30, 561, 381))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Images/images/background_latest.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        Invalid_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Invalid_Window)
        QtCore.QMetaObject.connectSlotsByName(Invalid_Window)

    def retranslateUi(self, Invalid_Window):
        _translate = QtCore.QCoreApplication.translate
        Invalid_Window.setWindowTitle(_translate("Invalid_Window", "Error Window"))
        self.label.setText(_translate("Invalid_Window", "Country not found in database!"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Invalid_Window = QtWidgets.QMainWindow()
    ui = Ui_Invalid_Window()
    ui.setupUi(Invalid_Window)
    Invalid_Window.show()
    sys.exit(app.exec_())

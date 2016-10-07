# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(191, 169)
        self.aboutWidget = QtWidgets.QWidget(AboutWindow)
        self.aboutWidget.setObjectName("aboutWidget")
        self.label = QtWidgets.QLabel(self.aboutWidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 121, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.aboutWidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        AboutWindow.setCentralWidget(self.aboutWidget)
        self.menuBar = QtWidgets.QMenuBar(AboutWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 191, 21))
        self.menuBar.setObjectName("menuBar")
        AboutWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(AboutWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        AboutWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(AboutWindow)
        self.statusBar.setObjectName("statusBar")
        AboutWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(AboutWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "MainWindow"))
        self.label.setText(_translate("AboutWindow", "Jóhann Berentsson 2016"))
        self.pushButton.setText(_translate("AboutWindow", "PushButton"))
        self.actionAbout.setText(_translate("AboutWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QMainWindow()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())


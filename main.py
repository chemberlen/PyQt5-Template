from mainwindow import Ui_MainWindow
from about import Ui_AboutWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class my_application(QtWidgets.QMainWindow, Ui_MainWindow, Ui_AboutWindow):

    def __init__(self):
        super(my_application, self).__init__()
        self.setupUi(self)
        self.slider0.valueChanged.connect(self.slider)
        self.slider1.valueChanged.connect(self.slider)
        self.slider2.valueChanged.connect(self.slider)
        self.slider3.valueChanged.connect(self.slider)
        self.actionAbout.triggered.connect(self.dialogAbout)

    def slider(self, value):
        print(value)

    def dialogAbout(self):
        print("digalogAbout")

        #dialog = QtWidgets.QDialog()
        #dialog.ui = Ui_AboutWindow()
        #dialog.ui.setupUi(dialog)
        #dialog.exec_()
        #dialog.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = my_application()
    ui.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poten.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import threading
import serial
sp = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 343)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(30, 30, 331, 51))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(30, 90, 331, 51))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(30, 150, 331, 51))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_4.setGeometry(QtCore.QRect(30, 220, 331, 51))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        
        self.progressBar.setMaximum(1023) ## setting the bar 
        self.progressBar_2.setMaximum(1023)
        self.progressBar_3.setMaximum(1023)
        self.progressBar_4.setMaximum(1023)




        def update(self): ## updating the progress bar
            while True:
                ## getting the data
                sp.write("\n".encode())
                inputraw = sp.readline().decode()
                input = inputraw.replace('\r\n','')
                ## slicing for individual bar
                   
                val = input.split(",")
                val1 = int(val[0])
                val2 = int(val[1])
                val3 = int(val[2])
                val4 = int(val[3])
 
                ## update the bar
                self.progressBar.setValue(val1)
                self.progressBar_2.setValue(val2)
                self.progressBar_3.setValue(val3)
                self.progressBar_4.setValue(val4)
        time.sleep(3)
        threading.Thread(target=update, args=(self,)).start()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

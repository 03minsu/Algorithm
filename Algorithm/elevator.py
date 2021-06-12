import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("elevator.ui")[0]
n = 1
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        nowFloor = self.NowN.value()
        
        self.Ubtn5.clicked.connect(self.up5)
        self.Ubtn4.clicked.connect(self.up4)
        self.Ubtn3.clicked.connect(self.up3)
        self.Ubtn2.clicked.connect(self.up2)
        self.Ubtn1.clicked.connect(self.up1)

    def up5(self):
        floor = int(self.F5.toPlainText())
        self.NowN.setValue(floor)
    def up4(self):
        floor = int(self.F4.toPlainText())
        self.NowN.setValue(floor)
    def up3(self):
        floor = int(self.F3.toPlainText())
        self.NowN.setValue(floor)
    def up2(self):
        floor = int(self.F2.toPlainText())
        self.NowN.setValue(floor)
    def up1(self):
        floor = int(self.F1.toPlainText())
        self.NowN.setValue(floor)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
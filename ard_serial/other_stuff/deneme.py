from PyQt5 import QtWidgets	
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0,0, 300, 300)
        self.setWindowTitle("Meric")
        self.initUI()
        
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Test Label")
        self.label.move(50, 50)
        
        self.but1 = QtWidgets.QPushButton(self)
        self.but1.setText("click")
        self.but1.clicked.connect(self.clicked)
      
    def clicked(self):
        self.label.setText("Button Pressed")
            
    
    
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    
    win.show()
    sys.exit(app.exec_())





    
window()    
   
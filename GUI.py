import sys
from PyQt4 import QtCore, QtGui, uic
 
ui_file = ""
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(ui_file)
 
class GUI(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, visible_on_start = True):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.toggle_visability(visible_on_start)
        
    def get_value(self, key):
        """TODO"""
        
    def set_value(self, key, value):
        """TODO"""
        
    def toggle_visability(self, toggle):
        if toggle:
            self.show()
        else:
            self.hide()

def do_GUI():
    prog = QtGui.QApplication(sys.argv)
    window = GUI(visible_on_start = True)
    sys.exit(prog.exec_())
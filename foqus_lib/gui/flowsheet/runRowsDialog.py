from foqus_lib.gui.flowsheet.runRowsDialog_UI import *
from PySide import QtGui, QtCore
 
class runRowsDialog(QtGui.QDialog, Ui_runRowsDialog):
    def __init__(self, parent, dat):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.dat = dat
        self.stop_now = False
        self.disconnect_now = False
        self.samples = 0
        self.success = 0
        self.error = 0
        self.time = 0
        self.allDone = False
        self.stopButton.clicked.connect(self.stopPress)
        self.disButton.clicked.connect(self.disPress)
        
    def stopPress(self):
        if self.allDone:
            self.close()
        self.stop_now = True
    
    def disPress(self):
        self.disconnect_now = True
        
    def update(self):
        self.samplesLine.setText(str(self.samples))
        self.successLine.setText(str(self.success))
        self.errorLine.setText(str(self.error))
        self.timeLine.setText(str(self.time))
        if self.allDone:
            self.stopButton.setText("Done")
        self.dat.mainWin.app.processEvents()
        
    def closeEvent(self, event):
        '''
            Intercept close main window close event
            make sure you really want to quit
        '''
        if self.allDone:
            event.accept()
        else:
            event.ignore()
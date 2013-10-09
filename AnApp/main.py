'''
Created on 09/ott/2013

@author: bveronesi
'''
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import imp
import sys
import functools
import os

class AnApp(QWidget):
    
    mySignal = pyqtSignal()
    
    def __init__(self,mainapp,*args):        
        self.loaded_module = None
        self.app = mainapp
        self.app.ende_map = dict()
        QWidget.__init__(self,*args)
        self.a_label = QLabel("Testing Signals")
        self.a_button = QPushButton("TEST !")
        self.load_button = QPushButton("Load Module")
        self.test_emission_button = QPushButton("EMIT")
        load_ext_module = functools.partial(self.load_module,"SelfRegistering")
        emission = functools.partial(self.mySignal.emit)
        self.load_button.clicked.connect(load_ext_module)
        self.a_button.clicked.connect(self.test_func)
        self.test_emission_button.clicked.connect(emission)
        layout = QVBoxLayout()
        layout.addWidget(self.a_label)
        layout.addWidget(self.a_button)
        layout.addWidget(self.load_button)
        layout.addWidget(self.test_emission_button)
        self.setLayout(layout)
        self.app.ende_map["test"] = self.mySignal
        
        
        
    def load_module(self,module_name):
        path = list()
        cwd = os.getcwd()
        modulePath = cwd+os.sep+"plugins"
        path.append(modulePath)
        foundModule= imp.find_module(module_name, path)
        self.loaded_module = imp.load_module("test",*foundModule)
        self.loaded_module.register(self.app.ende_map)
    
    def test_func(self):
        if self.loaded_module is not None:
            self.loaded_module.test("ciao",10)
            self.mySignal.emit()
        else:
            print("No loaded module: "+str(self.loaded_module))
            print(self.app)
    
    
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    w = AnApp(app) 
    w.show() 
    sys.exit(app.exec_())
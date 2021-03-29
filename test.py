#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# import sys
# from PyQt5.Qt import *
# from PyQt5.QtWebEngineWidgets import *
# from PyQt5.QtWidgets import QApplication
 
 
 
 
# app = QApplication(sys.argv)
 
# web = QWebEngineView()
 
# web.load(QUrl("http://tracuucontainer.danangport.com:40004/p/container/"))
 
# web.show()
 
 
# sys.exit(app.exec_())
tracuucontainer = "http://tracuucontainer.danangport.com:40004/p/container/"
tracuuconbooking = "http://tracuucontainer.danangport.com:40004/p/booking/"
tracuutheobill = "http://tracuucontainer.danangport.com:40004/p/bill/"
taudanglamhang = "http://tracuucontainer.danangport.com:40004/p/tau-dang-lam-hang/"

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super(MainWindow,self).__init__(*args,**kwargs)
    self.main()
  def main(self):
      x = input("Nhập: ")
      if int(x) == 1:
        print("vào")
        self.initUI1()
      elif int(x) ==2:
        self.initUI2()
      elif int(x) ==3:
        self.initUI3()
      elif int(x) ==4:  
        self.initUI4()
      else:
        pass
  def initUI1(self):
    self.setWindowTitle("Robot Metech")
    print("vào 2")
    # self.brower = QWebEngineView()
    self.brower.load(QUrl(tracuucontainer))
    self.setCentralWidget(self.brower)  
  def initUI2(self):
    self.setWindowTitle("Robot Metech")
    self.brower = QWebEngineView()
    self.brower.load(QUrl(tracuuconbooking))
    self.setCentralWidget(self.brower)  
  def initUI3(self):
    self.setWindowTitle("Robot Metech")
    self.brower = QWebEngineView()
    self.brower.load(QUrl(tracuutheobill))
    self.setCentralWidget(self.brower)  
  def initUI4(self):
    self.setWindowTitle("Robot Metech")
    self.brower = QWebEngineView()
    self.brower.load(QUrl(taudanglamhang))
    self.setCentralWidget(self.brower)  

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec_()

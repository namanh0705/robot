from functools import partial
#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
# from PyQt5.QtWebEngineWidgets import *
import re
import sys
import os
import time

tracuucontainer = "http://tracuucontainer.danangport.com:40004/p/container/"
tracuubooking = "http://tracuucontainer.danangport.com:40004/p/booking/"
tracuutheobill = "http://tracuucontainer.danangport.com:40004/p/bill/"
taudanglamhang = "http://tracuucontainer.danangport.com:40004/p/tau-dang-lam-hang/"


top = 50
left = 0
wight = 1280
height = 720


class RobotFaceWindow(QMainWindow):
  def __init__(self, app,worker):
    super(RobotFaceWindow,self).__init__()
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    self.title = "Window"
    self.l = 450
    self.t = 450
    self.w = rect.width()
    self.h = rect.height() -  self.t
    self.initUI()
    self.worker = worker
    self.closeEvent = self._closeEvent

  def initUI(self):
    self.setWindowTitle(self.title)
    self.setWindowFlag(Qt.FramelessWindowHint)  
    self.setGeometry(left, top, wight, height)
    windowLayout = QGridLayout()
    widget = QWidget()
    self.displayCamLabel = QLabel(widget)
    self.movie = QMovie("1.gif")
    self.displayCamLabel.setMovie(self.movie)
    self.movie.start()
    infoWidget = QWidget(widget)
    infoWidgetLayout = QGridLayout()
    inputInfoLayout = QGridLayout()
    infoWidget.setLayout(infoWidgetLayout)
    windowLayout.addWidget(self.displayCamLabel)

    widget.setLayout(windowLayout)
    self.setCentralWidget(widget)
  
  def _closeEvent(self,even):
    if self.worker is not None:
        self.worker.flag = False
    print("Close RobotFaceWindow")
    for i in range(10000000):
      pass

class RobotTalkWindow(QMainWindow):
  def __init__(self, app):
    super(RobotTalkWindow,self).__init__()
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    self.title = "Window"
    self.l = 450
    self.t = 450
    self.w = rect.width()
    self.h = rect.height() -  self.t
    self.initUI()
    self.closeEvent = self._closeEvent

  def initUI(self):
    self.setWindowTitle(self.title) 
    self.setWindowFlag(Qt.FramelessWindowHint)  
    self.setGeometry(left, top, wight, height)
    windowLayout = QGridLayout()
    widget = QWidget()
    self.displayCamLabel = QLabel(widget)
    self.movie = QMovie("1.gif")
    self.displayCamLabel.setMovie(self.movie)
    self.movie.start()
    infoWidget = QWidget(widget)
    infoWidgetLayout = QGridLayout()
    inputInfoLayout = QGridLayout()
    infoWidget.setLayout(infoWidgetLayout)
    windowLayout.addWidget(self.displayCamLabel)

    widget.setLayout(windowLayout)
    self.setCentralWidget(widget)
  
  def _closeEvent(self,even):
    print("Close RobotFaceWindow")

# class ShowSearchContainer(QMainWindow):
#   def __init__(self, app):
#     super(ShowSearchContainer,self).__init__()
#     screen = app.primaryScreen()
#     rect = screen.availableGeometry()
#     self.title = "Window"
#     self.l = 450
#     self.t = 450
#     self.w = rect.width()
#     self.h = rect.height() -  self.t
#     self.initUI()
#     self.closeEvent = self._closeEvent

#   def initUI(self):
#     self.setWindowTitle(self.title) 
#     self.setWindowFlag(Qt.FramelessWindowHint)  
#     self.setGeometry(left, top, wight, height)
#     self.brower = QWebEngineView()
#     self.brower.load(QUrl(tracuucontainer))
#     windowLayout = QGridLayout()
#     # widget = QWidget()
#     # self.displayCamLabel = QLabel(widget)
#     # self.movie = QMovie("2.gif")
#     # self.displayCamLabel.setMovie(self.movie)
#     # self.movie.start()
#     # infoWidget = QWidget(widget)
#     # infoWidgetLayout = QGridLayout()
#     # inputInfoLayout = QGridLayout()
#     # infoWidget.setLayout(infoWidgetLayout)
#     windowLayout.addWidget(self.brower)

#     # widget.setLayout(windowLayout)
#     # self.setCentralWidget(widget)
#     self.setCentralWidget(self.brower)  
  
#   def _closeEvent(self,even):
#     print("Close RobotFaceWindow")

# class ShowSearchBooking(QMainWindow):
#   def __init__(self, app):
#     super(ShowSearchBooking,self).__init__()
#     screen = app.primaryScreen()
#     rect = screen.availableGeometry()
#     self.title = "Window"
#     self.l = 450
#     self.t = 450
#     self.w = rect.width()
#     self.h = rect.height() -  self.t
#     self.initUI()
#     self.closeEvent = self._closeEvent

#   def initUI(self):
#     self.setWindowTitle(self.title) 
#     self.setWindowFlag(Qt.FramelessWindowHint)  
#     self.setGeometry(left, top, wight, height)
#     self.brower = QWebEngineView()
#     self.brower.load(QUrl(tracuubooking))
#     windowLayout = QGridLayout()
#     # widget = QWidget()
#     # self.displayCamLabel = QLabel(widget)
#     # self.movie = QMovie("2.gif")
#     # self.displayCamLabel.setMovie(self.movie)
#     # self.movie.start()
#     # infoWidget = QWidget(widget)
#     # infoWidgetLayout = QGridLayout()
#     # inputInfoLayout = QGridLayout()
#     # infoWidget.setLayout(infoWidgetLayout)
#     windowLayout.addWidget(self.brower)

#     # widget.setLayout(windowLayout)
#     # self.setCentralWidget(widget)
#     self.setCentralWidget(self.brower)  
  
#   def _closeEvent(self,even):
#     print("Close RobotFaceWindow")

# class ShowSearchBill(QMainWindow):
#   def __init__(self, app):
#     super(ShowSearchBill,self).__init__()
#     screen = app.primaryScreen()
#     rect = screen.availableGeometry()
#     self.title = "Window"
#     self.l = 450
#     self.t = 450
#     self.w = rect.width()
#     self.h = rect.height() -  self.t
#     self.initUI()
#     self.closeEvent = self._closeEvent

#   def initUI(self):
#     self.setWindowTitle(self.title) 
#     self.setWindowFlag(Qt.FramelessWindowHint)  
#     self.setGeometry(left, top, wight, height)
#     self.brower = QWebEngineView()
#     self.brower.load(QUrl(tracuutheobill))
#     windowLayout = QGridLayout()
#     # widget = QWidget()
#     # self.displayCamLabel = QLabel(widget)
#     # self.movie = QMovie("2.gif")
#     # self.displayCamLabel.setMovie(self.movie)
#     # self.movie.start()
#     # infoWidget = QWidget(widget)
#     # infoWidgetLayout = QGridLayout()
#     # inputInfoLayout = QGridLayout()
#     # infoWidget.setLayout(infoWidgetLayout)
#     windowLayout.addWidget(self.brower)

#     # widget.setLayout(windowLayout)
#     # self.setCentralWidget(widget)
#     self.setCentralWidget(self.brower)  
  
#   def _closeEvent(self,even):
#     print("Close RobotFaceWindow")

# class ShowSearchLamhang(QMainWindow):
  def __init__(self, app):
    super(ShowSearchLamhang,self).__init__()
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    self.title = "Window"
    self.l = 450
    self.t = 450
    self.w = rect.width()
    self.h = rect.height() -  self.t
    self.initUI()
    self.closeEvent = self._closeEvent

  def initUI(self):
    self.setWindowTitle(self.title) 
    self.setWindowFlag(Qt.FramelessWindowHint)  
    self.setGeometry(left, top, wight, height)
    self.brower = QWebEngineView()
    self.brower.load(QUrl(taudanglamhang))
    windowLayout = QGridLayout()
    # widget = QWidget()
    # self.displayCamLabel = QLabel(widget)
    # self.movie = QMovie("2.gif")
    # self.displayCamLabel.setMovie(self.movie)
    # self.movie.start()
    # infoWidget = QWidget(widget)
    # infoWidgetLayout = QGridLayout()
    # inputInfoLayout = QGridLayout()
    # infoWidget.setLayout(infoWidgetLayout)
    windowLayout.addWidget(self.brower)

    # widget.setLayout(windowLayout)
    # self.setCentralWidget(widget)
    self.setCentralWidget(self.brower)  
  
  def _closeEvent(self,even):
    print("Close RobotFaceWindow")
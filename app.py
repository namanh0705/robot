#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import gui as GUI
import sys
import re
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class WorkerSignal(QObject):
  signal_robotfacewindow = pyqtSignal()
  signal_robottalkwindow = pyqtSignal()
  signal_searchcontainer = pyqtSignal()
  signal_searchbooking = pyqtSignal()
  signal_searchbill = pyqtSignal()
  signal_searchlamhang = pyqtSignal()

class Worker(QRunnable):
  def __init__(self):
    super(Worker,self).__init__()
    self.signals = WorkerSignal()
    self.flag = True
  
  @pyqtSlot()
  def run(self):
    while self.flag:
      x = input("Nhập: ")
      if int(x) == 1:
        print("Màn hình bình thường")
        self.signals.signal_robotfacewindow.emit()
      elif int(x) ==2:
        print("Màn hình nói chuyện")
        self.signals.signal_robottalkwindow.emit()
      elif int(x) ==3:
        print("Màn hình tra cứu container")
        self.signals.signal_searchcontainer.emit()
      elif int(x) ==4:
        print("Màn hình tra cứu booking")
        self.signals.signal_searchbooking.emit()
      elif int(x) ==5:
        print("Màn hình tra cứu theo bill")
        self.signals.signal_searchbill.emit()
      elif int(x) ==6:
        print("Màn hình làm hàng")
        self.signals.signal_searchlamhang.emit()
      else:
        pass
  def end_thread(self):
    self.flag = False
      
class Controller():
  def __init__(self,app):
    
    self.currentWindow = None

    self.thread = QThreadPool()
    self.worker = Worker()
    self.thread.start(self.worker)

    self.RobotFaceWindow = GUI.RobotFaceWindow(app,self.worker)
    self.RobotTalkWindow = GUI.RobotTalkWindow(app)
    self.ShowSearchContainer = GUI.ShowSearchContainer(app)
    self.ShowSearchBooking = GUI.ShowSearchBooking(app)
    self.ShowSearchBill = GUI.ShowSearchBill(app)
    self.ShowSearchLamHang = GUI.ShowSearchLamhang(app)

    self.worker.signals.signal_robotfacewindow.connect(self.showRobotFaceWindow)
    self.worker.signals.signal_robottalkwindow.connect(self.showRobotTalkWindow)
    self.worker.signals.signal_searchcontainer.connect(self.showShowSearchContainer)
    self.worker.signals.signal_searchbooking.connect(self.showShowSearchBooking)
    self.worker.signals.signal_searchbill.connect(self.showShowSearchBill)
    self.worker.signals.signal_searchlamhang.connect(self.showShowSearchLamHang)


    self.showRobotFaceWindow()
    # self.showRobotTalkWindow()
    # self.showShowSearchContainer()
    # self.showShowSearchBooking()
    # self.showShowSearchBill()
    # self.showShowSearchLamHang()

  def showXwindow(self,window,hide_prev = True):
    if window == self.currentWindow:
      return
    if hide_prev:
      self.currentWindow.hide()
    window.show()
    self.currentWindow =window
  
  def showRobotFaceWindow(self):
    self.showXwindow(self.RobotFaceWindow,self.currentWindow is not None)
  def showRobotTalkWindow(self):
    self.showXwindow(self.RobotTalkWindow,self.currentWindow is not None)
  def showShowSearchContainer(self):
    self.showXwindow(self.ShowSearchContainer,self.currentWindow is not None)
  def showShowSearchBooking(self):
    self.showXwindow(self.ShowSearchBooking,self.currentWindow is not None)
  def showShowSearchBill(self):
    self.showXwindow(self.ShowSearchBill,self.currentWindow is not None)
  def showShowSearchLamHang(self):
    self.showXwindow(self.ShowSearchLamHang,self.currentWindow is not None)


def main():
  app = QApplication(sys.argv)
  controller = Controller(app)
  sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
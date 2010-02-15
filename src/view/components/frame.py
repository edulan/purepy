# -*- coding: utf-8 -*-

from wx import Frame

class AppFrame(Frame):

  def __init__(self):
    Frame.__init__(self, parent=None, id=-1, title="App Skeleton",size=(660,535))
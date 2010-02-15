# -*- coding: utf-8 -*-

from wx import App
from frame import AppFrame

class WxApp(App):

  appFrame = None

  def OnInit(self):
    self.appFrame = AppFrame()
    self.appFrame.Show()

    return True
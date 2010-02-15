# -*- coding: utf-8 -*-

from puremvc.patterns.facade import Facade
from view.components.app import WxApp

class AppFacade(Facade):

  STARTUP = "startup"

  def __init__(self):
    self.initializeFacade()

  @staticmethod
  def getInstance():
    return AppFacade()

  def initializeFacade(self):
    super(AppFacade, self).initializeFacade()
    self.initializeController()
   
  def initializeController(self):
    super(AppFacade, self).initializeController()
    #super(AppFacade, self).registerCommand(AppFacade.STARTUP, controller.StartupCommand)

if __name__ == '__main__':

  app = AppFacade.getInstance()
  wxApp = WxApp()
  #app.sendNotification(AppFacade.STARTUP, wxApp.appFrame)
  wxApp.MainLoop()
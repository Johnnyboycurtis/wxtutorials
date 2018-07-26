'''
Reference: https://www.tutorialspoint.com/wxpython/wxpython_menus.htm
'''

import wx  

class MyApp(wx.App):
    def __init__(self):
        super().__init__()

        frame = MyFrame(parent=None, title="Menu Bar App")


class FileMenu(wx.Menu):
    def __init__(self):
        super().__init__()
        self.OnInit()
    
    def OnInit(self):
        newItem = wx.MenuItem(parentMenu=self, id=wx.ID_NEW, text="New", kind=wx.ITEM_NORMAL)
        self.Append(newItem)

        radioItem1 = wx.MenuItem(self, 200,text = "Radio1",kind = wx.ITEM_RADIO)
        self.Append(radioItem1)
        radioItem2 = wx.MenuItem(self, 300,text = "Radio2",kind = wx.ITEM_RADIO) 
        self.Append(radioItem2)

        self.AppendSeparator() 

        quitItem = wx.MenuItem(self, wx.ID_EXIT, '&Quit\tCtrl+Q') 
        self.Append(quitItem)    



class EditMenu(wx.Menu):
    def __init__(self):
        super().__init__()
        self.OnInit()

    def OnInit(self):
        copyItem = wx.MenuItem(self, 100,text = "Copy",kind = wx.ITEM_NORMAL)
        self.Append(copyItem) 
        cutItem = wx.MenuItem(self, 101,text = "Cut",kind = wx.ITEM_NORMAL) 
        self.Append(cutItem) 
        pasteItem = wx.MenuItem(self, 102,text = "Paste",kind = wx.ITEM_NORMAL) 
        self.Append(pasteItem)



class MyFrame(wx.Frame): 
            
   def __init__(self, parent, title): 
      super().__init__(parent, title = title, size = (500, 400))  
      self.InitUI() 
         
   def InitUI(self):    
      menuBar = wx.MenuBar() 
		
      fileMenu = FileMenu()
      menuBar.Append(fileMenu, '&File') 

      editMenu = EditMenu()
      menuBar.Append(editMenu, '&Edit')
		
      self.SetMenuBar(menuBar) 
      self.text = wx.TextCtrl(self,-1, style = wx.EXPAND|wx.TE_MULTILINE) 
      #self.Bind(wx.EVT_MENU, self.MenuHandler) 
      self.Centre() 
      self.Show(True)
		
   def MenuaHndler(self, event): 
      id = event.GetId() 
      if id == wx.ID_NEW: 
         self.text.AppendText("new"+"\n")


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
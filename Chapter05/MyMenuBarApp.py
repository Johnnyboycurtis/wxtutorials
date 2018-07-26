'''
Reference: https://www.tutorialspoint.com/wxpython/wxpython_menus.htm
'''
import os
import wx  

class MyApp(wx.App):
    def __init__(self):
        super().__init__()

        frame = MyFrame(parent=None, title="Menu Bar App")
        frame.Show()


class FileMenu(wx.Menu):
    def __init__(self, parentFrame):
        super().__init__()
        self.OnInit()
        self.parentFrame = parentFrame
    
    def OnInit(self):
        newItem = wx.MenuItem(parentMenu=self, id=wx.ID_NEW, text="New", kind=wx.ITEM_NORMAL)
        self.Append(newItem)

        openItem = wx.MenuItem(parentMenu=self, id=wx.ID_OPEN, text='Open...', kind=wx.ITEM_NORMAL)
        self.Append(openItem)
        self.Bind(wx.EVT_MENU, handler=self.onOpen, source=openItem)

        saveItem = wx.MenuItem(parentMenu=self, id=wx.ID_SAVE, text="Save", helpString="Save your file", kind=wx.ITEM_NORMAL)
        self.Append(saveItem)
        self.Bind(wx.EVT_MENU, handler=self.onSave, source=saveItem)

        self.AppendSeparator() 

        radioItem1 = wx.MenuItem(self, id=200, text = "Option 1", kind = wx.ITEM_RADIO)
        self.Append(radioItem1)
        radioItem2 = wx.MenuItem(self, id=300, text = "Option 2", kind = wx.ITEM_RADIO) 
        self.Append(radioItem2)

        self.AppendSeparator() 

        quitItem = wx.MenuItem(self, wx.ID_EXIT, '&Quit\tCtrl+Q') 
        self.Append(quitItem)
        self.Bind(wx.EVT_MENU, handler=self.onQuit, source=quitItem)

    def onOpen(self, event):
        wildcard = "TXT files (*.txt)|*.txt"
        #wx.FileDialog(parent=self.parentFrame)
        dialog = wx.FileDialog(self.parentFrame, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return None

        path = dialog.GetPath()
        if os.path.exists(path):
            with open(path) as myfile:
                for line in myfile:
                    self.parentFrame.text.WriteText(line)

    def onSave(self, event):
        dialog = wx.FileDialog(self.parentFrame, message="Save your data", 
                            defaultFile="Untitled.txt", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return None
        
        path = dialog.GetPath()
        data = self.parentFrame.text.GetValue()
        print(data)
        data = data.split('\n')
        print(data)
        with open(path, "w+") as myfile:
            for line in data:
                myfile.write(line+"\n")


    def onQuit(self, event):
        self.parentFrame.Close()


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
        self.text = wx.TextCtrl(self,-1, style = wx.EXPAND|wx.TE_MULTILINE) 
        menuBar = wx.MenuBar() 

        fileMenu = FileMenu(parentFrame=self)
        menuBar.Append(fileMenu, '&File') 

        editMenu = EditMenu()
        menuBar.Append(editMenu, '&Edit')

        self.SetMenuBar(menuBar) 

        #self.Bind(wx.EVT_MENU, self.MenuHandler)
        self.Centre() 
        self.Show(True)


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
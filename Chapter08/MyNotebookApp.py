import wx

class MyApp(wx.App):
    def __init__(self):
        super().__init__()
        frame = MainFrame()
        frame.Show()

class NBPage(wx.Panel):
    def __init__(self, parent, message):
        super().__init__(parent)
        text = wx.StaticText(parent=self, id=wx.ID_ANY, label=message, pos=(20,20))

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Simple Notebook Example", pos = (100, 100))

        # Here we create a panel and a notebook on the panel
        self.p = wx.Panel(self)
        self.nb = wx.Notebook(self.p) # notebook will go on panel within a sizer

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer()
        sizer.Add(window=self.nb, proportion=1, flag=wx.EXPAND) # The item will be expanded to fill the space assigned to the item.
        # set proporition = 1 to allow changes (i.e. new pages)
        self.p.SetSizer(sizer)

        self.createMenu() # initialize the menu bar

    def createMenu(self):
        menuBar = wx.MenuBar()

        fileMenu = wx.Menu() # first 
        newItem = wx.MenuItem(parentMenu=fileMenu, id=wx.ID_NEW, 
                text='New Page\tCtrl+N', helpString='Create New Page', 
                kind=wx.ITEM_NORMAL) # subMenu is final option
        fileMenu.Append(newItem)
        self.Bind(event=wx.EVT_MENU, handler=self.onNewItem, source=newItem)

        # finally, append the File Menu
        menuBar.Append(fileMenu, '&File')

        # finally, add the Menu Bar
        self.SetMenuBar(menuBar)

    def onNewItem(self, event):
        count = self.nb.GetPageCount() + 1 # add 1 for extra page
        message = "This is page {}".format(count)
        page = NBPage(self.nb, message)
        self.nb.AddPage(page, "Page " + str(count))



if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
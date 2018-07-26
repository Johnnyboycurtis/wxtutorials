import wx
import wx.grid as gridlib



import wx
import webbrowser

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        
        # init frame
        self.InitFrame()
    
    def InitFrame(self):
        frame = MyFrame(parent=None, title="Basic Frame")
        #frame._panel = MyPanel(frame)
        frame.Show(True)


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent=parent, title=title)
        self.OnInit()

    def OnInit(self):
        print("On Init from MyFrame")
        titlePanel = MyPanel(parent=self)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer()
        gridSizer = wx.BoxSizer()

        titleSizer.Add(titlePanel)
        mainSizer.Add(titleSizer)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)



class MyPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent=parent)
        welcomeText = wx.StaticText(self, label="Welcome to wxPython", pos=(20,20))
        print("hello!!!!")


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

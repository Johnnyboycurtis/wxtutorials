import wx
import webbrowser

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        
        # init frame
        self.InitFrame()
    
    def InitFrame(self):
        frame = MyFrame(parent=None, title="Basic Frame")
        frame._panel = MyPanel(frame)
        frame.Show(True)


class MyFrame(wx.Frame):
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can (usually) be changed by the user.
    # Usually represents the first/main window a user will see
    def __init__(self, parent, title):
        super().__init__(parent=parent, title=title)


class MyPanel(wx.Panel):
    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self,parent):
        super().__init__(parent=parent)
        
        # add a hello message to the panel
        welcomeText = wx.StaticText(self, id=wx.ID_ANY, label="Welcome to wxPython", pos=(20,20))
        # ID_ANY means that we don’t care about the id


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

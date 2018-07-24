import wx
import webbrowser

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        
        # init frame
        self.InitFrame()
    
    def InitFrame(self):
        frame = wx.Frame(parent=None, title="Basic Frame")
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
        welcomeText = wx.StaticText(self, label="To learn wxPython, click the link below!", pos=(20,20))

        # add a button to bring up the dialog box
        button = wx.Button(parent=self, label='Click Here!', pos = (20, 120))
        button.Bind(wx.EVT_BUTTON, self.onSubmit) # bind action to button


    def onSubmit(self, event):
        # stuff for the submit button to do
        webbrowser.open('https://wxpython.org/Phoenix/docs/html/index.html')
        



if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

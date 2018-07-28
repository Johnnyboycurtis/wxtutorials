import wx

app = wx.App(clearSigInt=True) # clearSigInt to allow terminating the program by CTRL+C
frame = wx.Frame(parent=None, title="") ## main window object
panel = wx.Panel(parent=frame)
text = wx.StaticText(parent=panel, label="Hello, from wxPython!!", pos = (40,40))
frame.Show()
app.MainLoop()
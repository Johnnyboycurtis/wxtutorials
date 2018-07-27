import matplotlib
matplotlib.use('WXAgg')

import numpy as np
import matplotlib.pyplot as plt


from matplotlib.backends.backend_wxagg import FigureCanvas # FigureCanvasWxAgg as FigureCanvas
#from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg

#from matplotlib.backends.backend_wx import _load_bitmap
from matplotlib.figure import Figure

import wx
import rw

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        # run frame
        self.InitFrame()
    
    def InitFrame(self):
        frame = wx.Frame(parent=None, title="Random Walk", size=(600, 550))
        frame._panel = MyPanel(frame)
        frame.Show(True)


class MyFrame(wx.Frame):
    # subclass of wx.Window; Frame is a top level window
    # A frame is a window whose size and position can (usually) be changed by the user.
    # Usually represents the first/main window a user will see
    def __init__(self, parent, title, size):
        super().__init__(parent=parent, title=title, size=size)

class MyPanel(wx.Panel):
    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self,parent):
        super().__init__(parent=parent)
        self._dont_show = False # for message dialog box

        self.Decorate()
        
    def Decorate(self):
        # add a hello message to the panel
        title = wx.StaticText(self, label="Random Walk Tool", pos=(20,20))

        # add separator
        separator = wx.StaticLine(self, style=wx.LI_HORIZONTAL)

        muLabel = wx.StaticText(parent=self, label="mu: ")
        self.muInput = self.stepsInput = wx.SpinCtrl(parent=self, value="0", min=0, max=100) # replace txtctrl with spin button

        stepsLabel = wx.StaticText(parent=self, label="Number of Steps: ")
        self.stepsInput = self.stepsInput = wx.SpinCtrl(parent=self, value="100", min=0, max=1000)
        submitButton = wx.Button(parent=self, label="Submit")
        submitButton.Bind(wx.EVT_BUTTON, self.onSubmit)


        # add sizers to control layout of content
        self.mainSizer = wx.BoxSizer(wx.VERTICAL) # things will flow in vertical manner
        titleSizer = wx.BoxSizer(wx.HORIZONTAL) # sizer for title
        toolSizer = wx.StaticBoxSizer(parent=self, orient=wx.HORIZONTAL, label='Params')


        # add content to their respective sizer
        titleSizer.Add(title, proportion=0, flag=wx.ALL|wx.ALIGN_CENTER_VERTICAL, border=5)
        toolSizer.Add(muLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        toolSizer.Add(self.muInput, 0, wx.ALL, 5)
        toolSizer.Add(stepsLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        toolSizer.Add(self.stepsInput, 0, wx.ALL, 5)
        toolSizer.Add(submitButton, 0, wx.ALL, 5)

        self.mainSizer.Add(titleSizer, 0, wx.ALIGN_LEFT)
        self.mainSizer.Add(separator , 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(toolSizer, 0, wx.ALL|wx.CENTER, 5)

        # set main sizer; Sets the window to have the given layout sizer.
        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self) # Sizes the window so that it fits around its subwindows.

        # include an additional sizer for embedding the plot
        plotSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.p = CanvasFrame(self)
        plotSizer.Add(self.p, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.mainSizer.Add(plotSizer, 0, wx.ALL|wx.CENTER|wx.ALIGN_CENTER, 5)
        self.Layout()

    
    def onSubmit(self, event):
        '''
        On Submit, run the random walk module
        '''
        mu = self.muInput.GetValue()
        steps = self.stepsInput.GetValue()
        demo = rw.RandomWalk(val=int(mu), steps=int(steps))
        #demo.plot()
        self.p.plot(y=demo.y)
        self.Layout()



class CanvasFrame(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.figure = Figure(figsize=(6, 6), dpi=100)
        self.axes = self.figure.add_subplot(111)

    def plot(self, y, label='random walk'):
        self.axes.clear() # clear the axes before creating a new plot
        self.axes.plot(y)
        self.legend = self.axes.legend([label], shadow=True)
        #self.axes.margins(9.9)
        self.axes.set_ylabel('Y-label')
        self.axes.set_xlabel('X-label')
        self.axes.set_title('Title')
        self.axes.set_ylim(bottom=-10, top=10)

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.TOP | wx.CENTER | wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Fit()



if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

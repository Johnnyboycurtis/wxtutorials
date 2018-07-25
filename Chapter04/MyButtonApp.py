'''
Reference: https://wiki.wxpython.org/BoxSizerTutorial
'''

import wx


class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        
        # init frame
        self.InitFrame()
    
    def InitFrame(self):
        #frame = MyForm()
        frame = MyFrame()
        frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, title="MyButtonApp"):
        super().__init__(None, title=title)
        # initialize the frame's contents
        self.OnInit()

    def OnInit(self):
        self.panel = MyForm(self)
        #self.Show()
        self.Fit()

class MyForm(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent=parent)

        # Add a panel so it looks correct on all platforms

        bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
        titleIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        title = wx.StaticText(self, wx.ID_ANY, 'My Title')

        bmp = wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_OTHER, (16, 16))
        inputOneIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelOne = wx.StaticText(self, wx.ID_ANY, 'Input 1')
        inputTxtOne = wx.TextCtrl(self, wx.ID_ANY, value='Text box')

        inputTwoIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelTwo = wx.StaticText(self, wx.ID_ANY, 'Input 2')
        inputTxtTwo = wx.SpinCtrl(self, wx.ID_ANY, value="0", min=0, max=100)

        inputThreeIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelThree = wx.StaticText(self, wx.ID_ANY, 'Input 3')
        inputTxtThree = wx.Choice(self, choices=['A', 'B', 'C'])

        inputFourIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelFour = wx.StaticText(self, wx.ID_ANY, 'Input 4')
        #inputTxtFour = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        inputFour1 = wx.CheckBox(parent=self, label="Choice 1")
        inputFour2 = wx.CheckBox(parent=self, label="Choice 2")
        inputFour3 = wx.CheckBox(parent=self, label="Choice 3")

        okBtn = wx.Button(self, wx.ID_ANY, 'OK')
        cancelBtn = wx.Button(self, wx.ID_ANY, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

        topSizer        = wx.BoxSizer(wx.VERTICAL)
        titleSizer      = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer   = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer   = wx.BoxSizer(wx.HORIZONTAL)
        inputThreeSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer  = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer        = wx.BoxSizer(wx.HORIZONTAL)

        titleSizer.Add(titleIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)

        inputOneSizer.Add(inputOneIco, 0, wx.ALL, 5)
        inputOneSizer.Add(labelOne, 0, wx.ALL, 5)

        inputOneSizer.Add(inputTxtOne, 1, wx.ALL|wx.EXPAND, 5)

        inputTwoSizer.Add(inputTwoIco, 0, wx.ALL, 5)
        inputTwoSizer.Add(labelTwo, 0, wx.ALL, 5)
        inputTwoSizer.Add(inputTxtTwo, 1, wx.ALL|wx.EXPAND, 5)

        inputThreeSizer.Add(inputThreeIco, 0, wx.ALL, 5)
        inputThreeSizer.Add(labelThree, 0, wx.ALL, 5)
        inputThreeSizer.Add(inputTxtThree, 1, wx.ALL|wx.EXPAND, 5)

        inputFourSizer.Add(inputFourIco, 0, wx.ALL, 5)
        inputFourSizer.Add(labelFour, 0, wx.ALL, 5)
        inputFourSizer.Add(inputFour1, 1, wx.ALL|wx.EXPAND, 5)
        inputFourSizer.Add(inputFour2, 1, wx.ALL|wx.EXPAND, 5)
        inputFourSizer.Add(inputFour3, 1, wx.ALL|wx.EXPAND, 5)

        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputOneSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputTwoSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputThreeSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(inputFourSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(topSizer)
        topSizer.Fit(self)
        self.Layout()


    def onOK(self, event):
        # Do something
        print('onOK handler')

    def onCancel(self, event):
        self.closeProgram()

    def closeProgram(self):
        # self.GetParent() will get the frame which
        # has the .Close() method to close the program
        self.GetParent().Close()


# Run the program
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
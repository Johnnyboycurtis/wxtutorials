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
        frame = MyFrame()
        frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, title="MyButtonApp", pos=(100,100)):
        super().__init__(None, title=title, pos=pos)
        # initialize the frame's contents
        self.OnInit()

    def OnInit(self):
        self.panel = MyForm(self)
        self.Fit()

class MyForm(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent=parent)

        # Add a panel so it looks correct on all platforms

        # art provider provides basic art https://wxpython.org/Phoenix/docs/html/wx.ArtProvider.html
        bmp = wx.ArtProvider.GetBitmap(id=wx.ART_INFORMATION, 
        client=wx.ART_OTHER, size=(16, 16))
        titleIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        title = wx.StaticText(self, wx.ID_ANY, 'My Title')

        inputOneIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelOne = wx.StaticText(self, wx.ID_ANY, 'Input 1')
        self.inputTxtOne = wx.TextCtrl(self, wx.ID_ANY, value='Text box')

        inputTwoIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelTwo = wx.StaticText(self, wx.ID_ANY, 'Input 2')
        # wx.SpinCtrl combines wx.TextCtrl and wx.SpinButton in one control.
        self.inputTwo = wx.SpinCtrl(self, wx.ID_ANY, value="0", min=0, max=100)

        inputThreeIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelThree = wx.StaticText(self, wx.ID_ANY, 'Input 3')
        self.inputThree = wx.Choice(self, choices=['A', 'B', 'C'])
        

        inputFourIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelFour = wx.StaticText(self, wx.ID_ANY, 'Input 4')
        self.inputFour1 = wx.CheckBox(parent=self, label="Choice 1")
        self.inputFour2 = wx.CheckBox(parent=self, label="Choice 2")
        self.inputFour3 = wx.CheckBox(parent=self, label="Choice 3")

        okBtn = wx.Button(self, wx.ID_ANY, 'OK')
        cancelBtn = wx.Button(self, wx.ID_ANY, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputThreeSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer = wx.BoxSizer(wx.HORIZONTAL)
        submitBtnSizer = wx.BoxSizer(wx.HORIZONTAL)

        titleSizer.Add(titleIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)

        inputOneSizer.Add(inputOneIco, 0, wx.ALL, 5)
        inputOneSizer.Add(labelOne, 0, wx.ALL, 5)

        inputOneSizer.Add(self.inputTxtOne, 1, wx.ALL|wx.EXPAND, 5)

        inputTwoSizer.Add(inputTwoIco, 0, wx.ALL, 5)
        inputTwoSizer.Add(labelTwo, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.inputTwo, 1, wx.ALL|wx.EXPAND, 5)

        inputThreeSizer.Add(inputThreeIco, 0, wx.ALL, 5)
        inputThreeSizer.Add(labelThree, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.inputThree, 1, wx.ALL|wx.EXPAND, 5)

        inputFourSizer.Add(inputFourIco, 0, wx.ALL, 5)
        inputFourSizer.Add(labelFour, 0, wx.ALL, 5)
        inputFourSizer.Add(self.inputFour1, 1, wx.ALL|wx.EXPAND, 5)
        inputFourSizer.Add(self.inputFour2, 1, wx.ALL|wx.EXPAND, 5)
        inputFourSizer.Add(self.inputFour3, 1, wx.ALL|wx.EXPAND, 5)

        submitBtnSizer.Add(okBtn, 0, wx.ALL, 5)
        submitBtnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        mainSizer.Add(titleSizer, 0, wx.CENTER)
        mainSizer.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(inputOneSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(inputTwoSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(inputThreeSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(inputFourSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(submitBtnSizer, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        self.Layout()


    def onOK(self, event):
        # Do something
        print('onOK handler')
        data = self.getData()
        print(data)

    def onCancel(self, event):
        self.closeProgram()

    def closeProgram(self):
        # self.GetParent() will get the frame which
        # has the .Close() method to close the program
        self.GetParent().Close()

    def getData(self):
        '''
        this here will procure data from all buttons
        '''
        data = []
        data.append(self.inputTxtOne.GetValue())
        data.append(self.inputTwo.GetValue())
        selection = self.inputThree.GetSelection()
        data.append((selection, 
                    self.inputThree.GetString(selection))
                    )
        data.append(self.inputFour1.GetValue())
        data.append(self.inputFour2.GetValue())
        data.append(self.inputFour3.GetValue())
        return data

# Run the program
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
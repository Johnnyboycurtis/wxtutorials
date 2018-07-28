import wx


buttons = ["7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "+", "="]



class CalcFrame(wx.Frame):
    def __init__(self, parent, title, size, buttons):
        super().__init__(parent=parent, size=size, title=title)
        self.p = CalcPanel(parent=self, buttons=buttons)
        self.p.Layout()
        self.Show(True)



class CalcPanel(wx.Panel):
    def __init__(self, parent, buttons):
        super().__init__(parent=parent)
        self._buttons = buttons

        self.makeButtons()

    def makeButtons(self):
        specialButtons = [wx.Button(parent=self, id=wx.ID_ANY, label="Clear")] # special calculator menu buttons
        mainButtons = [wx.Button(parent=self, id=wx.ID_ANY, label=b) for b in self._buttons]
        self.display = wx.TextCtrl(self, style= wx.TE_READONLY, value="", size=(240,50)) #wx.StaticText(self, wx.ID_ANY, 'OUTPUT HERE')
        self.needs_reset_display=False

        mainSizer = wx.BoxSizer(orient=wx.VERTICAL)
        displaySizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        rowZero = wx.BoxSizer(orient=wx.HORIZONTAL) # special buttons like clear
        rowOne = wx.BoxSizer(orient=wx.HORIZONTAL)
        rowTwo = wx.BoxSizer(orient=wx.HORIZONTAL)
        rowThree = wx.BoxSizer(orient=wx.HORIZONTAL)
        rowFour = wx.BoxSizer(orient=wx.HORIZONTAL)

        displaySizer.Add(self.display)

        rowZero.Add(specialButtons[0], 0, wx.ALL, 5)

        rowOne.Add(mainButtons[0], 0, wx.ALL, 5)
        rowOne.Add(mainButtons[1], 0, wx.ALL, 5)
        rowOne.Add(mainButtons[2], 0, wx.ALL, 5)
        rowOne.Add(mainButtons[3], 0, wx.ALL, 5)

        rowTwo.Add(mainButtons[4], 0, wx.ALL, 5)
        rowTwo.Add(mainButtons[5], 0, wx.ALL, 5)
        rowTwo.Add(mainButtons[6], 0, wx.ALL, 5)
        rowTwo.Add(mainButtons[7], 0, wx.ALL, 5)

        rowThree.Add(mainButtons[8], 0, wx.ALL, 5)
        rowThree.Add(mainButtons[9], 0, wx.ALL, 5)
        rowThree.Add(mainButtons[10], 0, wx.ALL, 5)
        rowThree.Add(mainButtons[11], 0, wx.ALL, 5)

        rowFour.Add(mainButtons[12], 0, wx.ALL, 5)
        rowFour.Add(mainButtons[13], 0, wx.ALL, 5)
        rowFour.Add(mainButtons[14], 0, wx.ALL, 5)
        rowFour.Add(mainButtons[15], 0, wx.ALL, 5)



        ## then bind all buttons to events
        for i in range(15):
            print("BUTTON:", mainButtons[i].GetLabel())
            self.Bind(wx.EVT_BUTTON, self.onSelect, mainButtons[i])

        self.Bind(wx.EVT_BUTTON, self.onEqual, mainButtons[15])
        self.Bind(wx.EVT_BUTTON, self.onClear, specialButtons[0])

        mainSizer.Add(displaySizer, 1, wx.ALL | wx.ALIGN_CENTER, 5)
        #mainSizer.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5) # divider
        mainSizer.AddStretchSpacer()
        mainSizer.Add(rowZero, 0,wx.ALL | wx.ALIGN_CENTER, 5)
        mainSizer.Add(rowOne, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        mainSizer.Add(rowTwo, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        mainSizer.Add(rowThree, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        mainSizer.Add(rowFour, 0, wx.ALL | wx.ALIGN_CENTER, 5)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self.Parent)
        mainSizer.Layout()

    
    def onSelect(self,event):
        buttonSelected = event.GetEventObject()
        text = buttonSelected.GetLabel()
        if text in "+-/*":
            text = " " + text + " " # add some simple spacing
        print(text)
        self.display.AppendText(text)

    def onEqual(self, event):
        text = self.display.GetLineText(0)
        print(text)
        result = str(eval(text)) # evaluate the string the convert back to string
        print(result)
        self.display.SetValue(result)

    def onClear(self, event):
        self.display.Clear()



if __name__ == "__main__":
    app = wx.App(False)
    frame = CalcFrame(None, title='Calculator', size=(400, 300), buttons=buttons)
    app.MainLoop()
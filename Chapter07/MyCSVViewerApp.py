import wx
import wx.grid as gridlib
import csv 

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


        self._grid = CSVEditorGrid(self)
        self._grid.LoadFile(self._file)
        self._grid.SetColReadOnly(0)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)


class MyPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent=parent)
        welcomeText = wx.StaticText(self, label="Welcome to wxPython", pos=(20,20))
        print("hello!!!!")



class CSVDataSource(gridlib.GridTableBase):
    def __init__(self):
        super().__init__()
        self._data = None
        self._header = None
        self._readOnly = list()

    def LoadFile(self,fileName='./sample_data.csv'):
        reader = csv.reader(open(fileName, 'r'))
        self._data = [row for row in reader]
        self._header = self._data.pop(0)
        self._readOnly = list()



class CSVEditorGrid(gridlib.Grid):
    def __init__(self, parent):
        super().__init__(parent)

        self._data = CSVDataSource()
        self.SetTable(self._data)

    def LoadFile(self, fileName):
        self._data.LoadFile(fileName)
        self.SetTable(self._data)
        self.AutoSizeColumns()




if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()

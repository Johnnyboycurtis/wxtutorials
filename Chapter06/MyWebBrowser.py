import wx
from wx import html2

class MyApp(wx.App):
    def OnInit(self):
        WebFrame(None, "Surfing the Web").Show()
        return True


class WebFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        
        self._browser = html2.WebView.New(self)
        self._browser.LoadURL("www.google.com") # home page
        self._bar = NavBar(self, self._browser)
        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._bar, 0, wx.EXPAND)
        sizer.Add(self._browser, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        self.Bind(html2.EVT_WEBVIEW_TITLE_CHANGED, self.OnTitle)

    def OnTitle(self, event):
        self.Title = event.GetString()



class NavBar(wx.Panel):
    def __init__(self, parent, browser):
        super().__init__(parent)

        self.browser = browser
        print("Current URL:", self.browser.GetCurrentURL())
        self._url = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self._url.SetHint("Enter URL here and press enter...")

        back = wx.Button(self, style=wx.BU_EXACTFIT)
        back.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_BACK, 
                                               wx.ART_TOOLBAR)
        fw = wx.Button(self, style=wx.BU_EXACTFIT)
        fw.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD,
                                             wx.ART_TOOLBAR)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(back, proporition=0, flag=wx.ALL, border=5)
        sizer.Add(fw, proportion=0, flag=wx.ALL, border=5)
        sizer.Add(window=self._url, proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)


    def onEnter(self, event):
        self.browser.LoadURL(self._url.Value)
    
    def goBack(self, event):
        event.Enable(self.browser.CanGoBack())
        self.browser.GoBack()

    def goForward(self, event):
        event.Enable(self.browser.CanGoForward())
        self.browser.GoForward()



if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
    
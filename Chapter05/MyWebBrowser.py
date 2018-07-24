# Chapter 4: Containers and Advanced Controls
# Recipe 9: Surfing the web in your app
#
import wx
import wx.html2 as html2

class NaviBar(wx.Panel):
    def __init__(self, parent, browser):
        super(NaviBar, self).__init__(parent)

        b = browser
        print("Current URL:", b.GetCurrentURL())
        self._url = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self._url.SetHint("Enter URL here and press enter...")

        back = wx.Button(self, style=wx.BU_EXACTFIT)
        back.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_BACK, 
                                               wx.ART_TOOLBAR)
        fw = wx.Button(self, style=wx.BU_EXACTFIT)
        fw.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD,
                                             wx.ART_TOOLBAR)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(back, 0, wx.ALL, 5)
        sizer.Add(fw, 0, wx.ALL, 5)
        sizer.Add(self._url, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        
        self.Bind(wx.EVT_TEXT_ENTER, 
                  lambda event: b.LoadURL(self._url.Value))
        self.Bind(wx.EVT_BUTTON, lambda event: b.GoBack(), back)
        self.Bind(wx.EVT_BUTTON, lambda event: b.GoForward(), fw)
        self.Bind(wx.EVT_UPDATE_UI,
                  lambda event: event.Enable(b.CanGoBack()),
                  back)
        self.Bind(wx.EVT_UPDATE_UI,
                  lambda event: event.Enable(b.CanGoForward()),
                  fw)

class WebFrame(wx.Frame):
    def __init__(self, parent, title):
        super(WebFrame, self).__init__(parent, title=title)
        
        self._browser = html2.WebView.New(self)
        self._browser.LoadURL("www.google.com") # home page
        self._bar = NaviBar(self, self._browser)
        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._bar, 0, wx.EXPAND)
        sizer.Add(self._browser, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        self.Bind(html2.EVT_WEBVIEW_TITLE_CHANGED, self.OnTitle)

    def OnTitle(self, event):
        self.Title = event.GetString()

class MyApp(wx.App):
    def OnInit(self):
        WebFrame(None, "Surfing the Web").Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
    
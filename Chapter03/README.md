# Chapter 03 - Message Box

Here you will create an app with a message pop up box.

## Window Styles

In this example, I used `wx.YES_NO` which puts Yes and No buttons in the message box. It is recommended to always use CANCEL with this style as otherwise the message box won’t have a close button under wxMSW and the user will be forced to answer it. On Windows, it is important to include `wx.CANCEL` to add a close button to the message window. Also included was `wx.CENTRE` style to center the message box on the parent window.

Reference: https://wxpython.org/Phoenix/docs/html/wx.MessageDialog.html
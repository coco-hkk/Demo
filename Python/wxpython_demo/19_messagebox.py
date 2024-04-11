"""
两种形式的消息对话框：
1. wx.MessageBox
2. wx.MessageDialog
"""

import wx

class SampleMessageBox(wx.Frame):

    def __init__(self, *args, **kw):
        super(SampleMessageBox, self).__init__(*args, **kw)
        self.InitUi()

    def InitUi(self):
        # 延迟 3 秒后调用 self.ShowMessage
        wx.CallLater(3000, self.ShowMessage)

        self.SetTitle("消息框")
        self.SetSize(400, 280)
        self.Centre()

    def ShowMessage(self):
        wx.MessageBox("消息框", "信息", wx.OK | wx.ICON_INFORMATION)

 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleMessageBox(None)
    sample.Show()
    app.MainLoop()
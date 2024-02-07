"""
在 wxPython 事件系统中，事件是通过标识来区分的，每个事件标识其实就是一个独一无二的整数，常见的事件标识有窗口标识，标准标识以及定制事件标识等等。

窗口标识符：唯一确定窗口标识的整数

1. 让系统自动生成一个标志符，标志符参数设置为 -1 或 wx.ID_ANY
2. 使用系统中定义的标志符；
3. 创建自己使用的标识符。
"""

import wx
 
class SampleWindowsIds(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleWindowsIds, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        panel = wx.Panel(self)

        # 自动创建的标识符 -1 或 wx.ID_ANY
        exitButton = wx.Button(panel, wx.ID_ANY, "退出 - 自动分配标识符", (10, 10))

        # 标准标识符
        wx.Button(panel, wx.ID_EXIT, "退出 - 标准标识符", (10, 40))
 
        # 通过 GetId 获取控件的标识符
        self.Bind(wx.EVT_BUTTON, self.OnExit, id=exitButton.GetId())

        self.Bind(wx.EVT_BUTTON, self.OnExit, id=wx.ID_EXIT)
 
        self.SetTitle("事件标识符")
        self.Centre()
 
    def OnExit(self, e):
        self.Close()
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleWindowsIds(None)
    sample.Show()
    app.MainLoop()
 
"""
键盘事件 wx.KeyEvent

盘事件所携带的主要信息是正在按下或释放的键。它可以使用GetUnicodeKey, GetKeyCode或GetRawKeyCode函数之一来访问。
对于可打印字符，应该使用GetUnicodeKey，因为它适用于任何键，包括使用国家键盘布局时可以输入的非latin -1字符。
GetKeyCode应该用于处理与wx对应的特殊字符(如光标箭头键或HOME或INS等)。

虽然因为兼容性要求，GetKeyCode还返回Latin-1键的字符代码，但它一般不适用于Unicode字符，并且对于任何非Latin-1键将返回WXK_NONE。
如果GetUnicodeKey和GetKeyCode都返回WXK_NONE，那么该键没有WXK_xxx映射，GetRawKeyCode可以用来区分键，但原始键代码是特定于平台上的。
出于这些原因，建议总是使用GetUnicodeKey，只有当GetUnicodeKey返回WXK_NONE时才返回GetKeyCode，这意味着该事件对应于一个不可打印的特殊键，如果GetKeyCode也返回WXK_NONE，则可考虑检查GetRawKeyCode，或者直接忽略该键。

当我们在键盘上按下按钮时，一个 wx.KeyEvent 会被触发并被发送到当前焦点控件。有三种不同的键盘事件：

- wx.EVT_KEY_DOWN
- wx.EVT_KEY_UP
- wx.EVT_CHAR
"""

import wx
 
class SampleKeyEvent(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleKeyEvent, self).__init__(*args, **kw)
        self.InitUi()
 
    def InitUi(self):
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        panel.SetFocus()
 
        self.SetSize(400, 280)
        self.SetTitle("键盘事件")
        self.Centre()
 
    def OnKeyDown(self, e):
        key = e.GetKeyCode()
 
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox("确定要退出应用?", "问题", wx.YES_NO|wx.NO_DEFAULT, self)
            if ret == wx.YES:
                self.Close()

 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleKeyEvent(None)
    sample.Show()
    app.MainLoop()
 
"""
有两种类型的事件：

1. 基本事件
2. 命令事件

传播方式：

1. 命令事件可以传播，它沿子控件向父控件进行传播
2. 基本事件则不会传播到父控件，比如对于 wx.CloseEvent, 这是一个基本事件，将其传播到父控件是没有意义的。

在默认情况下，在事件处理程序中捕获事件后，事件将停止传播。为了继续传播，可以调用 Skip() 方法使事件继续传播。
"""

import wx


class MyPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(MyPanel, self).__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):
        print("event reached panel class")
        e.Skip()


class MyButton(wx.Button):
    def __init__(self, *args, **kw):
        super(MyButton, self).__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):
        print("event reached button class")
        e.Skip()


class SampleEventPropagation(wx.Frame):
    def __init__(self, *args, **kw):
        super(SampleEventPropagation, self).__init__(*args, **kw)

        self.InitUi()

    def InitUi(self):
        my_panel = MyPanel(self)

        MyButton(my_panel, label="OK", pos=(15, 15))

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        self.SetTitle("事件传播演示")
        self.Centre()

    def OnButtonClicked(self, e):
        print("event reached frame class")
        e.Skip()


if __name__ == "__main__":
    app = wx.App()
    sample = SampleEventPropagation(None)
    sample.Show()
    app.MainLoop()

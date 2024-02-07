"""
布局方式可以分为绝对定位布局和相对定位布局。

wxPython提供了以下调节器：

1. wx.BoxSizer
2. wx.StaticBoxSizer
3. wx.GridSizer
4. wx.FlexGridSizer
5. wx.GridBagSizer
"""

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.SetTitle("BoxSizer/StaticBoxSizer 水平布局实例")
        self.SetSize(400, 300)

        self.InitUi()

        self.Centre()

    def InitUi(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#4f5049")

        # 相对于 wx.BoxSizer 多了框和标签
        box = wx.StaticBoxSizer(wx.HORIZONTAL, panel, label="有框")

        # wx.BoxSizer 通过将一个 sizer 进行水平和垂直布局设置后，放置到已经存在的 Sizer 中
        box = wx.BoxSizer(wx.HORIZONTAL)

        pan1 = wx.Panel(panel)
        pan1.SetBackgroundColour("#00eded")

        pan2 = wx.Panel(panel)
        pan2.SetBackgroundColour("#ed00ed")

        box.Add(pan1, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
        box.Add(pan2, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(box)


if __name__ == "__main__":
    app = wx.App()
    window = Example(None)
    window.Show()
    app.MainLoop()

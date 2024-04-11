"""
绘制事件 wx.PaintEvent

当窗口的内容需要重新绘制的时候，比如当我们调整窗口大小或者最大化的时候，会发送一个绘制事件(Paint Event)。
当然我们也可以通过程序来触发绘制事件，比如，在调用Set Label()方法来修改wx.StaticText控件的文字信息时，就会触发绘制事件。
注意，窗口最小化不会触发绘制事件。
"""

import wx

class SamplePaintEvent(wx.Frame):
    def __init__(self, *args, **kw):
        super(SamplePaintEvent, self).__init__(*args, **kw)
        self.InitUi()

    def InitUi(self):
        self.count = 0
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("绘制事件")
        self.SetSize(400, 280)
        self.Centre()

    def OnPaint(self, e):
        self.count += 1
        dc = wx.PaintDC(self)
        text = "Number of paint events: {0}".format(self.count)

        # 从客户区指定像素点 (20, 20) 显示 text
        dc.DrawText(text, 20, 20)


if __name__ == "__main__":
    app = wx.App()
    sample = SamplePaintEvent(None)
    sample.Show()
    app.MainLoop()

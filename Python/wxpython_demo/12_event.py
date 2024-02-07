"""
在 wxPython 中，事件(Event)是每个 GUI 应用程序不可分割的一部分，所有 GUI 应用程序都是事件驱动的。
应用程序对在其生命周期内生成的不同事件类型做出反应，事件主要由使用应用程序的用户生成。
但它们也可以通过其他方式产生，例如Internet连接、窗口管理器或计时器都会生成相应的事件。
当我们调用 MainLoop() 方法时，我们的应用程序等待事件生成。在退出应用程序时结束 MainLoop() 方法。

wx.MoveEvent 窗口移动到新位置时产生新的位置

使用事件的三个步骤是：

1. 标识事件绑定器的名称, 如 wx.EVT_SIZE, wx.EVT_CLOSE 等；
2. 创建一个事件处理程序，在事件生成时调用该方法来处理事件；
3. 将事件和事件处理程序相绑定。
"""

import wx


class SampleSimpleEvent(wx.Frame):

    def __init__(self, *args, **kw):
        super(SampleSimpleEvent, self).__init__(*args, **kw)

        self.SetTitle("事件实例")
        self.InitUi()

    def InitUi(self):

        wx.StaticText(self, label="x:", pos=(10, 10))
        wx.StaticText(self, label="y:", pos=(10, 30))

        self.stx = wx.StaticText(self, label="", pos=(30, 10))
        self.sty = wx.StaticText(self, label="", pos=(30, 30))

        self.Bind(wx.EVT_MOVE, self.OnMove)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        self.SetSize((320, 240))
        self.Centre()

    def OnMove(self, evt):
        """ 窗口移动事件 """
        x, y = evt.GetPosition()
        self.stx.SetLabel(str(x))
        self.sty.SetLabel(str(y))

    def OnCloseWindow(self, evt):
        """ 否决事件 """
        dlg = wx.MessageDialog(None, "确定要退出?", "问题", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
 
        ret = dlg.ShowModal()
 
        if(ret == wx.ID_YES):
            self.Destroy()
        else:
            evt.Veto()



if __name__ == "__main__":
    app = wx.App()
    sample = SampleSimpleEvent(None)
    sample.Show()
    app.MainLoop()

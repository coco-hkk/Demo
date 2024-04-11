"""
焦点事件 wx.FocusEvent

当窗口的焦点发生变化时，将发送焦点事件。
焦点表明了当前应用中被选中的控件(widget)，当控件被选中时，从键盘输入或从剪贴板拷入的文本将发送到该控件。

有两个事件和焦点相关，wx.EVT_SET_FOCUS 和 wx.EVT_KILL_FOCUS：
当一个控件获得焦点时，就会触发wx.EVT_SET_FOCUS事件，当一个控件失去焦点时，则会触发wx.EVT_KILL_FOCUS事件。
通过点击或者键盘按键比如Tab键或者Shift+Tab键可以在控件之间切换焦点。
"""

import wx
 
class MyWindow(wx.Panel):
 
    def __init__(self, parent):
        super(MyWindow, self).__init__(parent)
 
        #画笔颜色
        self.color = "#b3b3b3"
 
        #绑定事件处理
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
 
    def OnPaint(self, e):
        dc = wx.PaintDC(self)
 
        # 设置画笔
        dc.SetPen(wx.Pen(self.color))
        # 获得客户区的尺寸
        x,y = self.GetSize()
        # 绘制一个矩形
        dc.DrawRectangle(0, 0, x, y)
 
    def OnSize(self, e):
        #当客户区发生改变时，刷新客户区
        self.Refresh()
 
    def OnSetFocus(self, e):
        #当进入焦点区域时，将画笔颜色设置为红色并重绘客户区
        self.color = "#ff0000"
        self.Refresh()
 
    def OnKillFocus(self, e):
        #当离开焦点区域时，将画笔颜色恢复为初始颜色并重绘客户区
        self.color = "#b3b3b3"
        self.Refresh()
 
class SampleFocusEvent(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleFocusEvent, self).__init__(*args, **kw)
        self.InitUi()
 
    def InitUi(self):
        #创建一个2x2网格布局
        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([(MyWindow(self), 0, wx.EXPAND|wx.TOP|wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.TOP|wx.RIGHT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.BOTTOM|wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 9)])
        
        self.SetSizer(grid)
 
        self.SetSize(400, 280)
        self.SetTitle("焦点事件")
        self.Centre()
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleFocusEvent(None)
    sample.Show()
    app.MainLoop()
 
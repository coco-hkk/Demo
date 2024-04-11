"""
鼠标事件 wx.KeyEvent

鼠标事件类包含关于鼠标生成的事件的信息:它们包括鼠标按钮按下并释放事件和鼠标移动事件。

所有涉及按钮的鼠标事件都使用MOUSE_BTN_LEFT作为鼠标左键，MOUSE_BTN_MIDDLE作为中间键，MOUSE_BTN_RIGHT作为右边键。
如果系统支持更多按钮，还可以生成MOUSE_BTN_AUX1和MOUSE_BTN_AUX2事件。
注意，并不是所有的鼠标都有一个中间按钮，所以便携式应用程序应该避免依赖于它的事件(但是在Mac平台下，可以使用鼠标左键和控制键来模拟单击右键)。

注意：对于wxEVT_ENTER_WINDOW和wxEVT_LEAVE_WINDOW事件的目的，如果鼠标在窗口客户端区域中，而不在它的一个子窗口中，则认为鼠标在窗口内。
换句话说，父窗口不仅在鼠标完全离开窗口时接收wxEVT_LEAVE_WINDOW事件，而且在鼠标进入其中一个子窗口时也接收wxEVT_LEAVE_WINDOW事件。

与鼠标事件相关的位置用生成事件窗口的窗口坐标表示，我们可以使用wx.Window.ClientToScreen将其转换为屏幕坐标，也可以调用wx.Window.ScreenToClient将其转换为另一个窗口的窗口坐标。
"""

 
import wx
 
class SampleMouseEvent(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleMouseEvent, self).__init__(*args, **kw)
 
        self.info = ""
 
        self.Bind(wx.EVT_PAINT, self.OnPaint)
 
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
 
        self.SetTitle("鼠标事件")
        self.SetSize(400, 280)
        self.Centre()
 
    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.DrawText(self.info, 20, 20)
 
    def OnLeftDown(self, e):
        self.info = "Mouse left button is pressed"
        self.Refresh();
 
    def OnLeftUp(self, e):
        self.info = "Mouse left button is released"
        self.Refresh()
 
    def OnMouseMove(self, e):
        #如果按下左键并移动鼠标，则显示当前鼠标的坐标信息
        if e.Dragging() and e.LeftIsDown():
            x,y = e.GetPosition()
            self.info = "current pos: x=" + str(x) + ", y=" + str(y)
            self.Refresh()
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleMouseEvent(None)
    sample.Show()
    app.MainLoop()
 
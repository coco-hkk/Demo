"""
基本控件 - 按钮

wx.Button 是包含文本字符串的控件，可以放置在对话框或者 wx.Panel 面板，以及几乎任何窗口上。
wx.ToggleButton 切换按钮
wx.BitmapButton 位图控件
"""

#切换按钮(wx.ToggleButton)
 
import wx
import os
 
class SampleToggleButton(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleToggleButton, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("Button & ToggleButton")
        self.SetSize(400, 360)
 
        panel = wx.Panel(self)
 
        self.color = wx.Colour(0, 0, 0)
 
        # 切换按钮
        btn_red = wx.ToggleButton(panel, label="红色", pos = (20, 20))
        btn_green = wx.ToggleButton(panel, label="绿色", pos = (20, 60))
        btn_blue = wx.ToggleButton(panel, label="蓝色", pos = (20, 100))
 
        self.colorPanel = wx.Panel(panel, pos=(150, 20), size=(110, 110))
        self.colorPanel.SetBackgroundColour(self.color)
 
        btn_red.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleRed)
        btn_green.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleGreen)
        btn_blue.Bind(wx.EVT_TOGGLEBUTTON, self.OnToggleBlue)

        # 按钮
        btn_close = wx.Button(panel, label="关闭", pos=(20, 140))
        btn_close.Bind(wx.EVT_BUTTON, self.OnButtonClose)

        # 位图按钮
        bmp = wx.Image(os.path.dirname(__file__) + "/resources/wxpython.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        btn_bmp = wx.BitmapButton(panel, wx.ID_ANY, bmp, pos = (150, 140))
        btn_bmp.Bind(wx.EVT_BUTTON, self.OnButtonClose)
        btn_bmp.SetDefault()
 
        self.Centre()

    def OnButtonClose(self, e):
        self.Close(True)
 
    def OnToggleRed(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
 
        green = self.color.Green()
        blue = self.color.Blue()
 
        if isPressed:
            self.color.Set(255, green, blue)
        else:
            self.color.Set(0, green, blue)
        
        self.colorPanel.SetBackgroundColour(self.color)
        self.colorPanel.Refresh()
 
    def OnToggleGreen(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
 
        red = self.color.Red()
        blue = self.color.Blue()
 
        if isPressed:
            self.color.Set(red, 255, blue)
        else:
            self.color.Set(red, 0, blue)
        
        self.colorPanel.SetBackgroundColour(self.color)
        self.colorPanel.Refresh()
 
    def OnToggleBlue(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
 
        red = self.color.Red()
        green = self.color.Green()
 
        if isPressed:
            self.color.Set(red, green, 255)
        else:
            self.color.Set(red, green, 0)
        
        self.colorPanel.SetBackgroundColour(self.color)
        self.colorPanel.Refresh()
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleToggleButton(None)
    sample.Show()
    app.MainLoop()
 
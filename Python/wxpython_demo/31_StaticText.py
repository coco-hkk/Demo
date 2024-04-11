"""
静态文本控件 wx.StaticText
静态图片控件 wx.StaticBitmap
静态分割线 wx.StaticLine
静态框控件 wx.StaticBox
下拉列表框 wx.ComboBox
进度条显示条控件 wx.Gauge
"""


import wx
import os
 
class SampleStaticText(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleStaticText, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("静态控件 StaticText")
        self.SetSize(340, 480)
 
        panel = wx.Panel(self)

        # 静态文本
        font =  wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(panel, label="静态控件", pos = (40, 15), size = (200, -1))
        heading.SetFont(font)

        # 静态分割线
        wx.StaticLine(panel, pos = (40, 50), size = (240, 1))

        # 静态框
        sbox = wx.StaticBox(panel, label="静态框", pos = (40, 55), size=(240, 150))
        
        # as parent
        wx.CheckBox(sbox, label="测试一", pos = (15, 30))
        wx.CheckBox(sbox, label="测试二", pos = (15, 55))
        wx.StaticText(sbox, label="数量", pos = (15, 95))
        wx.SpinCtrl(sbox, value="30", pos = (55, 90), size = (60, -1), min=1, max=120)

        # 静态位图
        bmpOn = wx.Image(os.path.dirname(__file__) + "/resources/light_on.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        bmpOff = wx.Image(os.path.dirname(__file__) + "/resources/light_off.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
 
        wx.StaticBitmap(panel, wx.ID_ANY, bmpOn, pos = (40, 210), size = (128, 150))
        wx.StaticBitmap(panel, wx.ID_ANY, bmpOff, pos = (170, 210), size = (128, 150))

        # 下拉列表框
        wx.StaticText(panel, label="Linux 发行版本:", pos=(40, 370))
 
        #创建一个只读下拉列表，可选择Linux的各种发行版本
        distros = ["Ubuntu", "Arch", "Fedora", "Debian", "Mint"]
        cb = wx.ComboBox(panel, pos = (160, 370), choices = distros, style = wx.CB_READONLY)
        cb.SetSelection(0)
        cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)
 
        #用于显示选中的Linux版本
        self.stcInfo = wx.StaticText(panel, label="", pos=(40, 400))

        self.Centre()

    def OnSelect(self, e):
       linux = e.GetString()
       self.stcInfo.SetLabel("当前Linux 发行版本: " + linux)
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleStaticText(None)
    sample.Show()
    app.MainLoop()
 
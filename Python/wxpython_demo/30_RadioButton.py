"""
基本控件单选按钮 RadioButton
"""

 
import wx
import os
 
class SampleRadioButton(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleRadioButton, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("RadioButton 实例")
        self.SetSize(600, 600)
 
        panel = wx.Panel(self)
 
        light_on = wx.RadioButton(panel, label="开灯", pos = (10, 10));
        light_on.Bind(wx.EVT_RADIOBUTTON, self.OnLightOn)
        
        light_off = wx.RadioButton(panel, label="关灯", pos = (60, 10));
        light_off.Bind(wx.EVT_RADIOBUTTON, self.OnLightOff)
 
        self.bmpOn = wx.Image(os.path.dirname(__file__) + "/resources/light_on.jpeg", wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.bmpOff = wx.Image(os.path.dirname(__file__) + "/resources/light_off.jpeg", wx.BITMAP_TYPE_JPEG).ConvertToBitmap()

        self.stcLight = wx.StaticBitmap(panel, wx.ID_ANY, self.bmpOn, pos = (100, 20), size = (512, 512))
 
        self.Centre()
 
    def OnLightOn(self, e):
        sender = e.GetEventObject()
        if sender.GetValue():
            self.stcLight.SetBitmap(self.bmpOn)
        else:
            self.stcLight.SetBitmap(self.bmpOff)       
 
    def OnLightOff(self, e):
        sender = e.GetEventObject()
        if sender.GetValue():
            self.stcLight.SetBitmap(self.bmpOff)
        else:
            self.stcLight.SetBitmap(self.bmpOn)
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleRadioButton(None)
    sample.Show()
    app.MainLoop()
 
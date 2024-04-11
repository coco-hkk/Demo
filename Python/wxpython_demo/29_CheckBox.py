"""
基本控件复选框 CheckBox

wx.CheckBox 复选框是一个有标签的框，默认情况下是打开(复选标记可见)或关闭(没有复选标记)。
当 wx.CHK_3STATE 样式标志已设置后，它可以有第三种状态，称为混合状态或待定状态。
"""

 
import wx
 
class SampleCheckBox(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleCheckBox, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("CheckBox 实例")
        self.SetSize(400, 240)
 
        panel = wx.Panel(self)
        
        vBox = wx.BoxSizer(wx.HORIZONTAL)
 
        chkBox = wx.CheckBox(panel, label="显示标题")
        chkBox.SetValue(True)
        chkBox.Bind(wx.EVT_CHECKBOX, self.OnShowOrHideTitle)
 
        vBox.Add(chkBox, flag=wx.TOP|wx.LEFT, border=30)
 
        panel.SetSizer(vBox)
 
        self.Centre()
 
    def OnShowOrHideTitle(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
 
        if isChecked:
            self.SetTitle("CheckBox 实例")
        else:
            self.SetTitle("")
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleCheckBox(None)
    sample.Show()
    app.MainLoop()
 
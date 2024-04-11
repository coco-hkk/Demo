"""
消息对话框 wx.MessageDialog
消息对话框对话框显示单行或多行消息，它比消息框(wx.MessageBox)更加灵活，可定制更多的特性，比如可以更改消息对话框的图标或者按钮等。

wx.OK: 在对话框上显示一个OK按钮，它可以和CANCEL按钮组合；
wx.Cancel: 在对话框上显示一个Cancel按钮, 它可以和OK以及YES_NO按钮组合；
wx.YES_NO: 在对话框上同时显示Yes和No按钮，推荐使用这种样式的时候和CANCEL组合；
wx.HELP: 在对话框上显示Help按钮，如果其标签为系统缺省值，则它可以特殊的外观和位置；
wx.YES_DEFAULT： Yes按钮为默认值；
wx.NO_DEFAULT: No按钮为默认值；
wx.CANCEL_DEFAULT: Cancel按钮为默认值；
wx.ICON_NONE: 如果可能，在对话框上不显示任何图标；
wx.ICON_ERROR: 在对话框上显示一个错误图标；
wx.ICON_WARNING: 在对话框上显示一个警告图标；
wx.ICON_QUESTION: 在对话框上显示一个问号标志；
wx.ICON_INFOMATION: 在对话框上显示一个信息图标；
wx.ICON_EXCLAMATION: 同wx.ICON_WARNING；
wx.ICON_HAND: 同wx.ICON_ERROR;
wx.ICON_AUTH_NEEDED: 显示身份验证所需的符号；
wx.STAY_ON_TOP： 使消息框保持在所有其他窗口之上 (目前仅在MSW和GTK下实现)；
wx.CENTRE： 将消息框置于其父消息框的中央，如果未指定其父消息框，则将消息框置于屏幕中央。在MSW下设置此样式没有区别，因为对话框始终以父对象为中心。
"""

import wx
 
class SampleMessageDialog(wx.Frame):
    def __init__(self, *args, **kw):
        super(SampleMessageDialog, self).__init__(*args, **kw)
        self.InitUi()
 
    def InitUi(self):
        panel = wx.Panel(self)
        hbox = wx.BoxSizer()
        sizer = wx.GridSizer(2,2,2,2)
 
        btnInfo = wx.Button(panel, label="信息")
        btnError = wx.Button(panel, label="错误")
        btnQuestion = wx.Button(panel, label="问题")
        btnAlert = wx.Button(panel, label="警告")
 
        sizer.AddMany([btnInfo, btnError, btnQuestion, btnAlert])
        hbox.Add(sizer, 0, wx.ALL, 15)
        panel.SetSizer(hbox)
 
        btnInfo.Bind(wx.EVT_BUTTON, self.ShowMessageInfo)
        btnError.Bind(wx.EVT_BUTTON, self.ShowMessageError)
        btnQuestion.Bind(wx.EVT_BUTTON, self.ShowMessageQuestion)
        btnAlert.Bind(wx.EVT_BUTTON, self.ShowMessageAlert)
 
        self.SetTitle("消息对话框 MessageDialog")
        self.SetSize(400, 280)
        self.Centre()
 
    def ShowMessageInfo(self, e):
        dlg = wx.MessageDialog(None, "下载完成", "信息", wx.OK)
        dlg.ShowModal()
 
    def ShowMessageError(self, e):
        dlg = wx.MessageDialog(None, "错误加载文件", "错误", wx.OK | wx.ICON_ERROR)
        dlg.ShowModal()
 
    def ShowMessageQuestion(self, e):
        dlg = wx.MessageDialog(None, "确定退出应用?", "问题", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        dlg.ShowModal()
 
    def ShowMessageAlert(self, e):
        dlg = wx.MessageDialog(None, "不允许的操作", "警告", wx.OK | wx.ICON_EXCLAMATION)
        dlg.ShowModal()
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleMessageDialog(None)
    sample.Show()
    app.MainLoop()

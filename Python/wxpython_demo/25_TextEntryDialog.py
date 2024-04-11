"""
文本输入对话框 wx.TextEntryDialog 或 wx.GetTextFromUser
密码输入对话框 wx.PasswordEntryDialog 或 wx.GetPasswordFromUser
数字输入对话框 wx.NumberEntryDialog 或 wx.GetNumberFromUser
"""


import wx
 
class SampleTextEntryDialog(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleTextEntryDialog, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("单行文本输入对话框")
        self.SetSize(480, 360)
 
        panel = wx.Panel(self)
        
        # 创建输入对话框
        dlg = wx.TextEntryDialog(self, "你最喜欢的编程语言是?", "TextEntryDialog","Python")
        if dlg.ShowModal() == wx.ID_OK:
            lang = "我最喜欢的编程语言是:" + dlg.GetValue()
        else:
            lang = "我不会编程"
 
        dlg.Destroy()
 
        ### 或
        # lang = wx.GetTextFromUser("你最喜欢的编程语言是?", "编程语言调查","Python")

        #用一个静态文本框显示输入的内容
        wx.StaticText(panel, -1, lang, pos=(10, 10))
 
        self.Centre()
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleTextEntryDialog(None)
    sample.Show()
    app.MainLoop()
 
"""
文本控件 wx.TextCtrl 
用来显示和编辑文本的控件，它支持单行和多行的文本编辑
"""


import wx
 
class SampleTextCtrl(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleTextCtrl, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("TextCtrl 实例")
        self.SetSize(480, 320)
 
        panel = wx.Panel(self)
 
        #单行文本
        wx.StaticText(panel, label = "单行文本:", pos = (20, 10))
        self.txtSingle = wx.TextCtrl(panel, wx.ID_ANY, pos = (100, 10), size = (260, 24))
        
        #多行文本
        wx.StaticText(panel, label = "多行文本:", pos = (20, 50))
        self.txtMulti = wx.TextCtrl(panel, wx.ID_ANY, pos = (100, 50), size = (260, 100), style = wx.TE_MULTILINE)
 
        #富文本
        wx.StaticText(panel, label = "富文本:", pos = (20, 160))
        self.txtRich = wx.TextCtrl(panel, wx.ID_ANY, pos = (100, 160), size = (260, 100), style = wx.TE_RICH | wx.TE_MULTILINE)
 
        #添加文本按钮
        btnAppend = wx.Button(panel, label="添加", pos = (380, 10))
        btnAppend.Bind(wx.EVT_BUTTON, self.OnAppendText)
        
        #清除文本按钮
        btnClear = wx.Button(panel, label="清除", pos = (380, 236))
        btnClear.Bind(wx.EVT_BUTTON, self.OnClearText)
 
        self.Centre()
 
    #将单行文本中输入的文字添加到多行和富文本编辑框中
    def OnAppendText(self, e):
        txt = self.txtSingle.GetValue()
        if(len(txt) > 0):
            self.txtMulti.AppendText(txt)
            self.txtMulti.AppendText("\n")
            self.txtRich.AppendText(txt)
            self.txtRich.AppendText("\n")
 
    def OnClearText(self, e):
        self.txtSingle.Clear()
        self.txtMulti.Clear()
        self.txtRich.Clear()
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleTextCtrl(None)
    sample.Show()
    app.MainLoop()
 
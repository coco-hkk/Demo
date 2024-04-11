"""
单选列表对话框 wx.SingleChoiceDialog 或 wx.GetSingleChoice
多选列表对话框 wx.MultiChoiceDialog
"""


import wx
 
class SampleSingleChoiceDialog(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleSingleChoiceDialog, self).__init__(*args, **kw)
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("实战wxPython: 单选列表对话框")
        self.SetSize(480, 360)
 
        choices  =  ["一",  "二",  "三",  "四", "五", "六", "七", "八", "九", "十"]
        # dlg  =  wx.SingleChoiceDialog(None,  "选择一个数字",  "选择",  choices)
        # if dlg.ShowModal()  ==  wx.ID_OK:
        #     txt = "当前的选择数字是: " + dlg.GetStringSelection()
        # else:
        #     txt = "未选择"
 
        # dlg.Destroy()

        ## 或
        txt = wx.GetSingleChoice("选择一个数字", "单选列表对话框", choices, 0)
 
        panel = wx.Panel(self)

        #用一个静态文本框显示当前选择的内容
        wx.StaticText(panel, -1, txt, pos=(10, 10)) 
 
        self.Centre()
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleSingleChoiceDialog(None)
    sample.Show()
    app.MainLoop()
 
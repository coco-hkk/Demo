"""
对话框是 GUI 应用中一个重要组成部分。在 GUI 应用中，对话框常用于输入修改数据，选择文件、字体、颜色，参数配置，消息显示等交互操作。
wx.Dialog 类是所有对话框窗口类的的基类，一个对话框应用类一般都从 wx.Dialog 类或者其子类派生(wx.PrintDialog例外，它调用系统原生对话框)。
wx.Dialog 常用来完成一个交互任务或者作为应用的顶层窗口使用。


"""

 
import wx
 
class ChangeDepthDialog(wx.Dialog):
 
    def __init__(self, *args, **kw):
        super(ChangeDepthDialog, self).__init__(*args, **kw)
        
        self.InitUi()
 
    def InitUi(self):
        #设置标题
        self.SetTitle("改变颜色深度")
        #设置窗口尺寸
        self.SetSize(250, 200)
 
        panel = wx.Panel(self)
        vBox = wx.BoxSizer(wx.VERTICAL)
 
        stcBox = wx.StaticBox(panel, label="颜色")
        stcBoxSizer = wx.StaticBoxSizer(stcBox, orient=wx.VERTICAL)
        stcBoxSizer.Add(wx.RadioButton(panel, label="256色", style=wx.RB_GROUP))
        stcBoxSizer.Add(wx.RadioButton(panel, label="16色"))
        stcBoxSizer.Add(wx.RadioButton(panel, label="2色"))
 
        hBox1 = wx.BoxSizer(wx.HORIZONTAL)
        hBox1.Add(wx.RadioButton(panel, label="自定义"))
        hBox1.Add(wx.TextCtrl(panel), flag=wx.Left, border=5)
        stcBoxSizer.Add(hBox1)
 
        panel.SetSizer(stcBoxSizer)
 
        hBox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label="确认")
        closeButton = wx.Button(self, label="关闭")
        hBox2.Add(okButton)
        hBox2.Add(closeButton, flag=wx.LEFT, border=5)
 
        vBox.Add(panel, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        vBox.Add(hBox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)
 
        self.SetSizer(vBox)
 
        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
 
    def OnClose(self, e):
        self.Destroy()
 
class SampleDialog(wx.Frame):
    
    def __init__(self, *args, **kw):
        super(SampleDialog, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        #设置标题
        self.SetTitle("对话框演示")
        #设置窗口尺寸
        self.SetSize(360, 240)
 
        tBar = self.CreateToolBar()
        tBar.AddTool(toolId=wx.ID_ANY, label="", bitmap=wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_CDROM)))
        tBar.Realize()
        tBar.Bind(wx.EVT_TOOL, self.OnChangeDepth)
 
        self.Centre()
 
    def OnChangeDepth(self, e):
        dlg = ChangeDepthDialog(None)
        dlg.ShowModal()
        dlg.Destroy()
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleDialog(None)
    sample.Show()
    app.MainLoop()
 
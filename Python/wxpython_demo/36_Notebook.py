"""
选项卡 wx.Notebook 控件允许用户在各种面板之间切换。最常见的例子是带有选项卡界面的浏览器和系统选项对话框。

提供了一个选项卡栏和一个“页面区域” 。该页面区域用于显示与每个选项卡相关的页面。默认情况下，选项卡栏显示在页面区域上方，但是可以使用不同的配置。
每个选项卡都与一个不同的窗口（称为页面）相关联。页面区域中仅显示当前页面。其他所有页面均被隐藏。
"""

import wx
 
# === 第一个页面 === #
class TabPanelOne(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id = wx.ID_ANY)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, wx.ID_ANY, "页面1")
        txtEditor = wx.TextCtrl(self, wx.ID_ANY, "")
        sizer.Add(title, 0, wx.ALL|wx.EXPAND, 5)
        sizer.Add(txtEditor, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)
 
# === 第二个页面 === #
class TabPanelTwo(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id = wx.ID_ANY)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, wx.ID_ANY, "页面2")
        button = wx.Button(self, wx.ID_ANY, "按钮", size = (100, 40))
        sizer.Add(title, 0, wx.ALL, 5)
        sizer.Add(button, 0, wx.ALL, 5)
        self.SetSizer(sizer)
 
class MyNotebook(wx.Notebook):
 
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id = wx.ID_ANY, style = wx.BK_DEFAULT)
 
        #创建页面并添加到选项卡中
        tabOne = TabPanelOne(self)
        tabOne.SetBackgroundColour("Gray")
        self.AddPage(tabOne, "TabOne")
 
        tabTwo = TabPanelTwo(self)
        tabTwo.SetBackgroundColour("LightGray")
        self.AddPage(tabTwo, "TabTwo")
 
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)
 
    def OnPageChanged(self, e):
        old = e.GetOldSelection()
        new = e.GetSelection()
        sel = self.GetSelection()
        print("OnPageChanged,  old:%d, new:%d, sel:%d\n" % (old, new, sel))
        e.Skip()
 
    def OnPageChanging(self, e):
        old = e.GetOldSelection()
        new = e.GetSelection()
        sel = self.GetSelection()
        print("OnPageChanging,  old:%d, new:%d, sel:%d\n" % (old, new, sel))
        e.Skip()
 
class SampleNotebook(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleNotebook, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("Notebook 实例")
        self.SetSize(400, 300)
 
        panel = wx.Panel(self)
 
        notebook = MyNotebook(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
 
        self.Centre()
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleNotebook(None)
    sample.Show()
    app.MainLoop()
 
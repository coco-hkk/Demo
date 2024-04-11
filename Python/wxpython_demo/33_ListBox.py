"""
wx.ListBox 列表框控件从一个字符串列表中选择一个或者多个字符串。
所选字符串显示在一个可以滚动的列表框中，所选中的字符串将特别标记。列表框可以是单选 (如果选择了其中的一个项，则清除先前的选择项)或者多重选择(选择一个项的时，不影响对其他项的选择)。

列表框元素从 0 开始编号，虽然元素的最大数量是无限的，但通常最好使用虚拟控件，不需要一次性将所有项添加到其中。
由于这个控件没有做优化，比如在 wx.dataview.DataViewCtrl 或者使用 LC_VIRTUAL 样式的 wx.ListCtrl 时，需要加载超过上百的项时，性能会有所影响。

注意，列表框不支持除制表符以外的控制字符。

wx.CheckListBox 复选列表框
"""

import wx
 
class SampleListBox(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleListBox, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("ListBox 实例")
        self.SetSize(400, 240)
 
        panel = wx.Panel(self)
 
        hbox = wx.BoxSizer(wx.HORIZONTAL)
 
        # 添加一个列表框
        self.listbox = wx.ListBox(panel)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
 
        # 按钮面板
        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        newButon = wx.Button(btnPanel, wx.ID_ANY, "新建", size = (90, 30))
        renButton = wx.Button(btnPanel, wx.ID_ANY, "重命名", size = (90, 30))
        delButton = wx.Button(btnPanel, wx.ID_ANY, "删除", size = (90, 30))
        clrButton = wx.Button(btnPanel, wx.ID_ANY, "清理", size = (90, 30))
 
        newButon.Bind(wx.EVT_BUTTON, self.NewItem)
        renButton.Bind(wx.EVT_BUTTON, self.OnRename)
        delButton.Bind(wx.EVT_BUTTON, self.OnDelete)
        clrButton.Bind(wx.EVT_BUTTON, self.OnClear)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)
 
        vbox.Add((-1, 20)) #距离顶端20像素
        vbox.Add(newButon)
        vbox.Add(renButton, 0, wx.TOP, 5)
        vbox.Add(delButton, 0, wx.TOP, 5)
        vbox.Add(clrButton, 0, wx.TOP, 5)
 
        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)
 
        self.Centre()
 
    def NewItem(self, e):
        text = wx.GetTextFromUser("输入一个新项", "插入对话框")
        if text != "":
            self.listbox.Append(text)
 
    def OnRename(self, e):
        sel = self.listbox.GetSelection()
        if sel == -1:
            wx.MessageBox("请选择项", "提示")
            return

        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser("项重命名", "重命名对话框", text)
 
        if renamed != "":
            self.listbox.Delete(sel)
            item_id = self.listbox.Insert(renamed, sel)
            self.listbox.SetSelection(item_id)
 
    def OnDelete(self, e):
        sel = self.listbox.GetSelection()
        if sel != -1:
            self.listbox.Delete(sel)
 
    def OnClear(self, e):
        self.listbox.Clear()
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleListBox(None)
    sample.Show()
    app.MainLoop()
 
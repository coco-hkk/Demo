"""
wx.ListCtrl 是项列表的图形表示。一个 wx.ListBox 只能有一列，wx.ListCtrl 可以有多个列。

wx.ListCtrl 可以以三种不同的格式使用。列表视图、报表视图、图标视图和小图标视图。这些格式由 wx.ListCtrl 窗口样式 wx.LC_REPORT, wx.LC_LIST, wx.LC_ICON 和 wx.LC_SMALL_ICON 控制。

在任何情况下，元素都是从 0 开始编号的。对于所有这些模式，项都存储在控件中，必须使用 wx.ListCtrl.InsertItem 方法将项添加到控件中。

报表视图的一个特殊情况与列表控件的其他模式非常不同，它是一个虚拟控件，其中的项数据(包括文本、图像和属性)由主程序管理，只有在需要时才由控件本身请求，这允许拥有数百万项的控件而不消耗太多内存。

wx.ListView 继承自 wx.ListCtrl，它提供一个更容易使用的接口
"""
 

import wx
 
data = [
    ("鲁迅", "浙江", "1881"),
    ("艾青", "浙江", "1910"),
    ("沈从文", "湖南", "1902"),
    ("郁达夫", "浙江", "1896"),
    ("巴金", "四川", "1904"),
    ("莫言", "山东", "1955")
]
 
class SampleListCtrl(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleListCtrl, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("ListCtrl 实例")
        self.SetSize(400, 240)
 
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
 
        # wx.LC_REPORT：单列或者多列报告方式,并且可以设置可选的标题。
        self.list = wx.ListCtrl(panel, wx.ID_ANY, style = wx.LC_REPORT)
 
        self.list.InsertColumn(0, "名字", width = 140)
        self.list.InsertColumn(1, "出生地", width = 130)
        self.list.InsertColumn(2, "出生年份", wx.LIST_FORMAT_RIGHT, 90)
 
        idx = 0
 
        for i in data:
            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])
            idx += 1
 
        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)
 
        self.Centre()
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleListCtrl(None)
    sample.Show()
    app.MainLoop()

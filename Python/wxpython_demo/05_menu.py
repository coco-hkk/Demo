"""
菜单项有三种样式：

常规样式(normal item)
复选样式(check item)
单选样式(radio item)

上下文菜单常常也称作弹出菜单，在一个交互窗口中，上下文菜单就是一组操作命令的列表。右键单击显示出的列表。
"""

import wx

class MyPopupMenu(wx.Menu):
    """上下文菜单"""

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        menuItemMin = wx.MenuItem(self, wx.NewIdRef(), "最小化")
        self.Append(menuItemMin)
        self.Bind(wx.EVT_MENU, self.OnMinimize, menuItemMin)

        menuItemClose = wx.MenuItem(self, wx.NewIdRef(), "关闭")
        self.Append(menuItemClose)
        self.Bind(wx.EVT_MENU, self.OnClose, menuItemClose)

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.SetTitle("复选菜单项和上下文菜单")
        self.SetSize(400, 300)

        self.InitUi()

        self.Centre()

    def InitUi(self):
        menubar = wx.MenuBar()

        # 创建一个视图菜单，有两个复选项。
        viewMenu = wx.Menu()

        # 添加复选项菜单，将参数 kind 设置为 wx.ITEM_CHECK
        self.showStatus = viewMenu.Append(wx.ID_ANY, "显示状态条", "显示状态条", kind=wx.ITEM_CHECK)
        self.showTool = viewMenu.Append(wx.ID_ANY, "显示工具条", "显示工具条", kind=wx.ITEM_CHECK)

        # 启动时，工具栏和状态栏都是可见的，所以复选菜单都选上
        viewMenu.Check(self.showStatus.GetId(), True)
        viewMenu.Check(self.showTool.GetId(), True)

        # 绑定复选菜单选中动作
        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.showStatus)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.showTool)

        menubar.Append(viewMenu, "视图(&V)")
        self.SetMenuBar(menubar)

        # 创建工具栏
        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_NEW)))
        self.toolbar.AddTool(1, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN)))
        self.toolbar.AddTool(1, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE)))
        self.toolbar.Realize()

        # 创建状态栏
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("就绪")

        # 绑定右键单击
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

    def OnRightDown(self, e):
        """ PopupMenu 显示上下文菜单 """
        self.PopupMenu(MyPopupMenu(self), e.GetPosition())

    def ToggleStatusBar(self, e):

        if self.showStatus.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):

        if self.showTool.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()


if __name__ == "__main__":
    app = wx.App()
    window = Example(None)
    window.Show()
    app.MainLoop()

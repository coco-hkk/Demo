"""
工具栏也是 GUI 程序一个常见的组成部分，使用工具栏可以快速访问应用程序最常见的命令。
在 wxPython 中，工具栏通常位于 wx.Frame 中的菜单栏下方，由按钮或者其他控件构成工具栏, 工具栏由 wx.ToolBar 类来实现。

使用 wx.Frame.CreateToolBar() 来创建一个由 wx.Frame 调用管理的工具栏；
也可以创建一个工具栏，添加到布局中，再设置到窗口中去。
工具栏添加完所需的所有工具后，必须调用 Realize() 以有效地构造和显示工具栏。
"""

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.SetTitle("工具栏实例")
        self.SetSize(400, 300)

        self.InitUi()

        self.Centre()

    def InitUi(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 方法一：创建一个工具栏，默认情况下，工具栏是水平放置，没有边框，只显示图标
        # toolbar = self.CreateToolBar(wx.TB_FLAT)

        # 添加工具
        # quit = toolbar.AddTool( wx.ID_ANY, "退出", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT)))

        # 方法二
        toolbar = wx.ToolBar(self)
        quit = toolbar.AddTool(wx.ID_ANY, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT)))

        # 完成工具栏的构建
        toolbar.Realize()

        # 创建第二个工具栏
        toolbar1 = wx.ToolBar(self)
        toolbar1.AddTool(wx.ID_ANY, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_NEW)))
        toolbar1.AddTool(wx.ID_ANY, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN)))
        toolbar1.AddTool(wx.ID_ANY, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE)))
        toolbar1.Realize()

        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnQuit, quit)

        self.SetSizer(vbox)

    def OnQuit(self, e):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    window = Example(None)
    window.Show()
    app.MainLoop()

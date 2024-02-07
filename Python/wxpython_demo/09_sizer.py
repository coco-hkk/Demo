"""
wx.GridSizer, wx.FlexGridSizer, wx.GridBagSizer 提供在一个二维表格中进行布局的功能。

wx.GridSizer 提供基本的网格布局，表格中的每个单元格都具有相同的尺寸
wx.FlexGridSizer 则具有更灵活的布局
Wx.GirdBagSizer 则在 wx.FlexGridSizer 之上提供了更多的增强功能
"""

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.SetTitle("GridSizer 计算器")
        self.SetSize(400, 300)

        self.InitUi()

        self.Centre()

    def InitUi(self):

        # 设置应用退出菜单
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        miExit = wx.MenuItem(fileMenu, wx.ID_EXIT, "退出(&Q)\tCtrl+Q")
        fileMenu.Append(miExit)

        # 绑定菜单项的行为
        self.Bind(wx.EVT_MENU, self.OnQuit, miExit)

        menubar.Append(fileMenu, "文件(&F)")
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.Bottom, border=4)

        gs = wx.GridSizer(5, 4, 5, 5)
        gs.AddMany(
            [
                (wx.Button(self, label="Cls"), 0, wx.EXPAND),
                (wx.Button(self, label="Bck"), 0, wx.EXPAND),
                (wx.StaticText(self), wx.EXPAND),
                (wx.Button(self, label="Close"), 0, wx.EXPAND),
                (wx.Button(self, label="7"), 0, wx.EXPAND),
                (wx.Button(self, label="8"), 0, wx.EXPAND),
                (wx.Button(self, label="9"), 0, wx.EXPAND),
                (wx.Button(self, label="/"), 0, wx.EXPAND),
                (wx.Button(self, label="4"), 0, wx.EXPAND),
                (wx.Button(self, label="5"), 0, wx.EXPAND),
                (wx.Button(self, label="6"), 0, wx.EXPAND),
                (wx.Button(self, label="*"), 0, wx.EXPAND),
                (wx.Button(self, label="1"), 0, wx.EXPAND),
                (wx.Button(self, label="2"), 0, wx.EXPAND),
                (wx.Button(self, label="3"), 0, wx.EXPAND),
                (wx.Button(self, label="-"), 0, wx.EXPAND),
                (wx.Button(self, label="0"), 0, wx.EXPAND),
                (wx.Button(self, label="."), 0, wx.EXPAND),
                (wx.Button(self, label="="), 0, wx.EXPAND),
                (wx.Button(self, label="+"), 0, wx.EXPAND),
            ]
        )

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def OnQuit(self, e):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    window = Example(None)
    window.Show()
    app.MainLoop()

"""
菜单栏由称为菜单的对象组成。顶级菜单在菜单栏上具有自己的标签。菜单具有菜单项，菜单项是在应用程序内部执行特定操作的命令。菜单也可以具有子菜单，这些子菜单具有自己的菜单项。
创建菜单栏的三个类：wx.MenuBar, wx.Menu 和 wx.MenuItem。
"""

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        # 创建一个菜单栏对象
        menubar = wx.MenuBar()

        # 创建一个菜单对象
        fileMenu = wx.Menu()

        # 将菜单项添加到菜单对象中，第一个参数是菜单项的 ID，第二个参数是菜单项的名称
        fileItem = fileMenu.Append(wx.ID_EXIT, "退出", "退出应用")

        # 将菜单对象绑定到菜单栏对象
        menubar.Append(fileMenu, "文件(&F)")

        # 显示菜单栏
        self.SetMenuBar(menubar)

        # 绑定 wx.EVT_MENU 到自定义 OnQuit
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize(400, 300)
        self.SetTitle("菜单实例")
        self.Centre()

    def OnQuit(self, e):
        self.Close()


if __name__ == "__main__":
    app = wx.App()

    window = Example(None)
    window.Show()

    app.MainLoop()

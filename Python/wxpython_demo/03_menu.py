"""
类 wx.MenuItem 是 wxPython 中菜单项的实现，它表示菜单中的项。
通常情况下，我们无需直接创建 wx.MenuItem 对象，而是使用 wx.Menu 的方法来获得一个 wx.MenuItem 对象。

通过 wx.MenuItem 设置菜单各种功能。
"""

import wx

APP_EXIT = 1


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.SetTitle("为菜单栏添加快捷键和图标")
        self.SetSize(400, 300)

        self.InitUi()
        self.Centre()

    def InitUi(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        # 使用 wx.MenuItem 创建菜单项，& 字符指定加速键；设置快捷键，必须使用 \t 分割
        qmi = wx.MenuItem(fileMenu, APP_EXIT, "退出(&Q)\tCtrl+Q")

        # 设置自定义图标
        qmi.SetBitmap(wx.Bitmap("resources/03_menu_exit.png"))
        # qmi.SetBitmap(wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT)))

        fileMenu.Append(qmi)

        # 绑定菜单项的行为
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, "文件(&F)")
        self.SetMenuBar(menubar)

    def OnQuit(self, e):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    window = Example(None)
    window.Show()
    app.MainLoop()

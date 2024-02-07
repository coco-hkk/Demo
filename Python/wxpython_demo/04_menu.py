"""
wx.Menu 用于构造菜单栏或弹出菜单

菜单项具有ID与之关联的整数，该整数可用于标识选择或以某种方式更改菜单项。具有特殊标识符的菜单项wx.ID_SEPARATOR 是分隔符项，没有关联的命令，而只是使分隔线出现在菜单中。

菜单项可以是 普通(normal)项，复选项(check)或单选项(radio)。
1. 普通菜单项没有任何特殊属性，
2. 而复选项具有与其关联的布尔标志，并且当设置了标志时它们会在菜单中显示一个对勾。
3. 单选项目与复选项相似，不同之处在于，在选中某个单选项时，单选组中的所有其他菜单项都处于未选中状态。单选项组由一系列连续的单选项构成。它从此类的第一项开始，到另一种不同的项（或菜单的结尾）结束。
   请注意，由于单选项组是根据菜单项的位置定义的，因此在包含单选项的菜单中插入或删除菜单项可能会导致无法正常工作。
"""

import wx
import os


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.SetTitle("子菜单和分隔符")
        self.SetSize(400, 300)

        self.InitUi()

        self.Centre()

    def InitUi(self):
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()

        fileMenu.Append(wx.ID_NEW, "新建(&N)")
        fileMenu.Append(wx.ID_OPEN, "打开(&O)")
        fileMenu.Append(wx.ID_SAVE, "保存(&S)")

        # 带有水平分割符的子菜单
        fileMenu.AppendSeparator()

        # 创建子菜单，子菜单也是 wx.Menu
        subImport = wx.Menu()
        subImport.Append(wx.ID_ANY, "导入文章列表...")
        subImport.Append(wx.ID_ANY, "导入书签...")
        subImport.Append(wx.ID_ANY, "导入邮件...")

        # 使用 AppendSubMenu 将子菜单附加到文件菜单
        fileMenu.AppendSubMenu(subImport, "导入(&I)")

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, "退出(&Q)\tCtrl+W")
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, "文件(&F)")
        self.SetMenuBar(menubar)

    def OnQuit(self, e):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    window = Example(None)
    window.Show()
    app.MainLoop()

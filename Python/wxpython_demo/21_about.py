"""
创建 About 对话框前，需要新建两个对象：
- wx.AboutDialogInfo
- wx.AboutBox

wxPython 可以展示两种 About 框，取决于我们使用哪个平台以及调用哪个方法，可以是原生的对话框也可以是 wxPython 类的对话框。
Windows 原生对话框无法展示自定义的图标、许可文字以及URL链接。
如果我们忽略这三个参数， wxPython 将展示一个原生的对话框，否则它将展示一个 wxPython 对话框。
如果想尽可能的保持原生的话，建议在一个单独的菜单项提供许可信息。GTK+ 可以显示所有这些信息。

wx.AboutDialogInfo 提供了以系列方法来设置About对话框所需要的相关信息。其常用方法有：

SetIcon： 设置一个图标
SetName: 设置应用的名称
SetDescription: 设置应用的描述信息
SetCopyright: 设置应用的版权信息
SetWebSite: 设置网站地址
SetLicence： 设置应用的许可信息
AddDeveloper: 添加开发者
AddDocWriter: 添加文档作者
AddArtist: 添加美术设计者
AddTranslator: 添加翻译者
"""

 
import wx
import wx.adv
import os
 
class SampleAboutBox(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleAboutBox, self).__init__(*args, **kw)
        self.InitUi()
 
    def InitUi(self):
 
        menuBar = wx.MenuBar()
        help = wx.Menu()
        help.Append(wx.ID_ANY, "关于(&A)")
        help.Bind(wx.EVT_MENU, self.OnAboutBox)
 
        menuBar.Append(help, "帮助(&H)")
        self.SetMenuBar(menuBar)
 
        self.SetTitle("About 对话框")
        self.SetSize(400, 280)
        self.Centre()
 
    def OnAboutBox(self, e):
        # 要在 About 对话框中显示必要的信息，首先创建一个 wx.AboutDialogInfo 对象
        info = wx.adv.AboutDialogInfo()
 
        # 设置需要显示的信息
        info.SetIcon(wx.Icon(os.path.dirname(__file__) + '/resources/python-logo.png', wx.BITMAP_TYPE_PNG))
        info.SetName("My wxPython Program")
        info.SetVersion("1.0")
        info.SetDescription("这是一个 AboutBox 演示程序")
        info.SetCopyright("(C) 2023 My name")
        info.SetWebSite("http://www.myprogram.com")
        info.SetLicence("本程序放弃版权，可自由传播")
        info.AddDeveloper("Developer name")
        info.AddDocWriter("Document writer")
        info.AddArtist("Artist")
        info.AddTranslator("Translator")
 
        # 创建 AboutBox
        wx.adv.AboutBox(info)

 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleAboutBox(None)
    sample.Show()
    app.MainLoop()
 
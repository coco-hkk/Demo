"""
https://docs.wxpython.org/index.html

wxPython 由五个基本模块组成：Controls, Misc, Core, GDI, Windows

1. 控件(Control) 模块提供了图形应用程序中常见的部件(widget)。例如，按钮(Button)，工具条(Toolbar)，记事本(Noteboo)等。部件在Windows系统下一般称作控件(Control)。
2. 核心(Core) 模块包含了在开发中使用的基本类，这些类包括Object类(它是所有控件类的基类）；Sizers(用于部件布局)，Events(事件驱动)，基本几何对象类(如Point和Rectangle)。
3. 图形设备接口(GDI) 是一组用于绘制部件的类。它包含字体处理(Font)，颜色(Color)，画刷(Brush),画笔(Pen)和图像(Image)类。
4. 杂项(Misc)模块包含其他各种类和功能模块，这些类用于日志记录，应用程序设置，系统设置，显示或操纵杆的使用等等。
5. 视窗(Window)模块由形成各种应用程序的窗口类组成，例如面板(Panel),对话框(Dialog), 框架(Frame)或者滚动窗口(Scrolled Window)等

部件是 GUI 应用程序的基本构建模块，大致分为下面几类：

1. 基本部件：为派生部件提供基本功能。它们通常作为其它类的基类，一般不直接使用。wx.Window, wx.Control, wx.ControlWithItem
2. 顶层部件：彼此独立存在，通常用于提供各种窗口。wx.Frame, wx.Dialog, wx.ScrolledWindow
3. 容器：用于包含其它部件。wx.Panel, wx.NoteBook
4. 动态部件：可以由用户编辑其中的内容。wx.TextCtrl, wx.Button, wx.Grid, wx.ListBox
5. 静态部件：一般用于显示信息，用户不能编辑其中的内容。wx.StaticBox, wx.StaticText
6. 其它小工具：用于在应用程序中实现状态栏。wx.ToolBar, wx.MenuBar

wx.Frame()

1. wx.Frame 部件是一个容器，它可以包含不是框架或对话框的任何窗口。它由标题栏，边框和中央容器区域组成。标题栏和边框是可选的，可以通过各种标志将其删除。
2. wx.Frame 可以指定应用程序大小，通过构造函数或调用 SetSize() 实现
3. wx.Frame 可以指定窗口的位置
4. 应用程序屏幕居中，调用 Centre()
"""

# 导入基本 wxPython 模块，基本模块中所有的函数和对象都将以 wx. 前缀开头
import wx

# 创建应用程序对象，并启用日志输出
app = wx.App(redirect=True)

# 重定向内容输出到文件或新窗口
app.RedirectStdio()
# 若启用输出重定向，设置输出窗口属性
app.SetOutputWindowAttributes(title="日志")

print("日志输出：APP 已初始化")

# 创建 wx.Frame 对象，它是其它部件的父级部件，本身没有父级部件，所以 parent=None
# title 指定窗口标题，size 指定窗口大小
frame = wx.Frame(None, title="wxPython 简单实例", size=(350, 250))

# 应用程序屏幕居中
frame.Centre()

# 创建 wx.Frame 部件后，必须调用 Show() 才能将其显示在屏幕
frame.Show()

# 主循环，它是个死循环，捕获并调度应用程序生命周期内存在的所有事件
app.MainLoop()

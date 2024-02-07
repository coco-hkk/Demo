"""
wx.GridBagSizer

显式支持在指定的网格位置添加一个控件，同时也可以指定控件跨越行或者列。

1. Add(): 在网格指定位置处添加一个控件；
2. GetItemPosition(): 返回指定位置的控件项；
3. SetItemPosition(): 在网格指定位置放置一个控件项；
4. GetItemSpan(): 返回一个控件项的行/列跨越数；
5. SetItemSpan(): 设置一个控件项的行/列跨越数。
"""

import wx


class SampleGridBagSizer(wx.Frame):

    def __init__(self, parent, title):
        super(SampleGridBagSizer, self).__init__(parent, title=title)

        self.InitUi()
        self.Centre()

    def InitUi(self):

        panel = wx.Panel(self)

        # GridBagSizer 作为panel的主布局
        sizer = wx.GridBagSizer(5, 5)

        labelJavaClass = wx.StaticText(panel, label="Java类")  # Java class
        sizer.Add(labelJavaClass, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap("resources/python-logo.png"))
        sizer.Add(icon, pos=(0, 4), flag=wx.TOP | wx.RIGHT | wx.ALIGN_RIGHT, border=5)

        # 添加一条横线
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.BOTTOM, border=10)

        labelName = wx.StaticText(panel, label="名称")  # Name
        sizer.Add(labelName, pos=(2, 0), flag=wx.LEFT, border=10)

        tcName = wx.TextCtrl(panel)
        sizer.Add(tcName, pos=(2, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)

        labelPackage = wx.StaticText(panel, label="包")  # Package
        sizer.Add(labelPackage, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=10)

        tcPackage = wx.TextCtrl(panel)
        sizer.Add(tcPackage, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)

        buttonBrowse1 = wx.Button(panel, label="浏览...")  # Browse...
        sizer.Add(buttonBrowse1, pos=(3, 4), flag=wx.TOP | wx.RIGHT, border=5)

        labelExtends = wx.StaticText(panel, label="扩展")  # Extends
        sizer.Add(labelExtends, pos=(4, 0), flag=wx.TOP | wx.LEFT, border=10)

        comboExtends = wx.ComboBox(panel)
        sizer.Add(
            comboExtends, pos=(4, 1), span=(1, 3), flag=wx.Top | wx.EXPAND, border=5
        )

        buttonBrowse2 = wx.Button(panel, label="浏览...")  # Browse...
        sizer.Add(buttonBrowse2, pos=(4, 4), flag=wx.TOP | wx.RIGHT, border=5)

        sbOptAttr = wx.StaticBox(panel, label="可选属性")  # Optional Attributes

        # 垂直布局
        vboxSizer = wx.StaticBoxSizer(sbOptAttr, wx.VERTICAL)

        chkPublic = wx.CheckBox(panel, label="公共")  # Public
        vboxSizer.Add(chkPublic, flag=wx.LEFT | wx.TOP, border=5)

        chkGeneDefConstructor = wx.CheckBox(
            panel, label="创建缺省构造函数"
        )  # Generate Default Constructor
        vboxSizer.Add(chkGeneDefConstructor, flag=wx.LEFT, border=5)

        chkGeneMainMethod = wx.CheckBox(panel, label="创建Main方法")
        vboxSizer.Add(chkGeneMainMethod, flag=wx.LEFT | wx.BOTTOM, border=5)

        sizer.Add(
            vboxSizer,
            pos=(5, 0),
            span=(1, 5),
            flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT,
            border=10,
        )

        buttonHelp = wx.Button(panel, label="帮助")  # Help
        sizer.Add(buttonHelp, pos=(7, 0), flag=wx.LEFT, border=10)

        buttonOK = wx.Button(panel, label="确定")  # OK
        sizer.Add(buttonOK, pos=(7, 3))

        buttonCancel = wx.Button(panel, label="取消")
        sizer.Add(
            buttonCancel, pos=(7, 4), span=(1, 1), flag=wx.BOTTOM | wx.RIGHT, border=10
        )

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)


if __name__ == "__main__":
    app = wx.App()
    sample = SampleGridBagSizer(None, title="GridBagSizer 实例")
    sample.Show()
    app.MainLoop()

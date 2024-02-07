import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.SetTitle("禁用/启用工具栏按钮")
        self.SetSize(400, 300)

        self.InitUi()

        self.Centre()

    def InitUi(self):
        self.count = 5

        self.toolbar = self.CreateToolBar()
        tundo = self.toolbar.AddTool(
            wx.ID_UNDO, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_UNDO))
        )
        tredo = self.toolbar.AddTool(
            wx.ID_REDO, "", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_REDO))
        )

        # 调用 EnableTool 设置禁用/启用重做按钮功能
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()

        texit = self.toolbar.AddTool(
            wx.ID_EXIT, "退出", wx.Bitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT))
        )
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, texit)
        self.Bind(wx.EVT_TOOL, self.OnUndo, tundo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, tredo)

    def OnQuit(self, e):
        self.Close()

    def OnUndo(self, e):
        if self.count > 1 and self.count <= 5:
            self.count -= 1
        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)
        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, e):
        if self.count < 5 and self.count >= 1:
            self.count += 1
        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)
        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)


def main():
    app = wx.App()
    window = Example(None)
    window.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()

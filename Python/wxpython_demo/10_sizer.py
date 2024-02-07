"""
wx.FlexGridSizer

每行和每列可以有各自的尺寸
在默认情况下，对尺寸大小进行调节时，会改变行和列的整体尺寸，在 FlexGriderSizer 中，可以指定某行或者某列的尺寸进行调节
可以在行和列两个方向进行灵活调整，可以为指定个别子元素指定比列量，并且可以指定固定方向上的调整行为

AddGrowableCol(idx, proportion=0) 设定索引为 idx 的列为可增长列；
AddGrowableRow(idx, proportion=0) 设定索引为 idx 的行为可增长行。
参数：proportion=0 为默认，表示所有的可增长行或列 按照同比例缩放。如果要指定不一样的缩放比例，那么需要手动设置proportion 值。
例如，如 果你有两个尺寸可调整的行，并且它们的proportion分别是2和1，那么这第一个行将得到新空间的2/3，第二行将得到 1/3。
"""

import wx


class SampleFlexGridSizer(wx.Frame):
    def __init__(self, parent, title):
        super(SampleFlexGridSizer, self).__init__(parent, title=title)

        self.InitUi()
        self.Centre()

    def InitUi(self):
        panel = wx.Panel(self)

        hBox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(3, 2, 9, 25)

        title = wx.StaticText(panel, label="标题")
        author = wx.StaticText(panel, label="作者")
        review = wx.StaticText(panel, label="评审")

        tcTitle = wx.TextCtrl(panel)
        tcAuthor = wx.TextCtrl(panel)
        tcReview = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        fgs.AddMany(
            [
                (title),
                (tcTitle, 1, wx.EXPAND),
                (author),
                (tcAuthor, 1, wx.EXPAND),
                (review, 1, wx.EXPAND),
                (tcReview, 1, wx.EXPAND),
            ]
        )

        # 设定索引为 idx 的行或列为可增长行列
        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        hBox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hBox)


if __name__ == "__main__":
    app = wx.App()
    sample = SampleFlexGridSizer(None, "FlexGridSizer 实例")
    sample.Show()
    app.MainLoop()

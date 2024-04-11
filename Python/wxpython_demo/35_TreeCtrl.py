"""
树形控件 wx.TreeCtrl 将信息表示为层次结构，其中的项可以展开以显示更多的项。
"""

 
import wx
 
class SampleTreeCtrl(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleTreeCtrl, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("TreeCtrl 实例")
        self.SetSize(400, 320)
 
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
 
        #创建树形控件
        self.treectrl = wx.TreeCtrl(panel, wx.ID_ANY, wx.DefaultPosition, (-1, -1), wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS)
 
        #显示树形控件选中项的名称
        self.info = wx.StaticText(panel, wx.ID_ANY, "", wx.DefaultPosition, (-1, 40), style = wx.ALIGN_CENTER)
 
        #给树形控件添加数据 
        root = self.treectrl.AddRoot("程序员")
        os = self.treectrl.AppendItem(root, "操作系统");
        prog_lang = self.treectrl.AppendItem(root, "编程语言")
        tool_kit = self.treectrl.AppendItem(root, "工具包")
        self.treectrl.AppendItem(os, "Windows")
        self.treectrl.AppendItem(os, "Ubuntu")
        self.treectrl.AppendItem(os, "Android")
        compile_lang = self.treectrl.AppendItem(prog_lang, "编译语言")
        shell_lang = self.treectrl.AppendItem(prog_lang, "脚本语言")
        self.treectrl.AppendItem(compile_lang, "C")
        self.treectrl.AppendItem(compile_lang, "C++")
        self.treectrl.AppendItem(compile_lang, "JAVA")
        self.treectrl.AppendItem(shell_lang, "JS")
        self.treectrl.AppendItem(shell_lang, "PHP")
        self.treectrl.AppendItem(shell_lang, "Python")
        self.treectrl.AppendItem(shell_lang, "Lua")
        self.treectrl.AppendItem(tool_kit, "QT")
        self.treectrl.AppendItem(tool_kit, "wxWidgets")
        self.treectrl.AppendItem(tool_kit, "Gtk+")
        self.treectrl.AppendItem(tool_kit, "Swing")
        self.treectrl.ExpandAll()
 
        #事件处理
        self.treectrl.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged)
 
        vbox.Add(self.treectrl, 1, wx.EXPAND, border = 10)
        vbox.Add(self.info)
 
        panel.SetSizer(vbox)
 
        self.Centre()
 
    def OnSelChanged(self, e):
        item = e.GetItem()
        self.info.SetLabel(self.treectrl.GetItemText(item))
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleTreeCtrl(None)
    sample.Show()
    app.MainLoop()

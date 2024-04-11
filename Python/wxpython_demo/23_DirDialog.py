"""
文件夹选择对话框 wx.DirDialog

常用方法：
- GetMessage(self): 返回文件对话框的标题信息；
- GetPath(self): 返回缺省或者用户选择的文件夹，本方法不同用于带有 样式DD_MULTIPLE的窗口中；
- GetPaths(self, paths): 将选择的文件的全部路径填充到参数paths中；
- SetMessage(self, message): 设置对话框的标题信息；
- SetPath(self, path): 设置默认选择的文件路径；
- ShowModal(self): 显示对话框，如果点击了wx.OK按钮则返回wx.ID_OK,否则返回wx.ID_CANCEL。

wx.DirSelector 全局方法，可以弹出一个目录选择对话框
"""

#目录选择对话框(DirDialog)
import wx
import os
 
class SampleDirDialog(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleDirDialog, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        #设置标题
        self.SetTitle("文件夹选择对话框")
        #设置窗口尺寸
        self.SetSize(480, 360)
        #设置窗口位置
        self.SetPosition(wx.DefaultPosition)
        #设置窗口样式
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)
        #创建菜单栏
        self.BuildMenuBar()
        self.Centre()
 
        #===== 显示选中的文件夹名 =====#
        label = wx.StaticText(self, -1, "当前选择的文件夹:")
        self.txtBox = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size = (-1, 300))
        #水平布局
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(label, 0, wx.ALL|wx.ALIGN_TOP)
        sizer.Add(self.txtBox, 1, wx.ALL|wx.ALIGN_CENTER)
        #向窗口中添加布局
        self.SetSizer(sizer)
 
    def BuildMenuBar(self):
        mainMenuBar = wx.MenuBar()
 
        fileMenu = wx.Menu()
 
        dirBrowserItem = fileMenu.Append(-1, "文件夹浏览")
        self.Bind(wx.EVT_MENU, self.OnDirBrowser, dirBrowserItem)
 
        projectSaveAsItem = fileMenu.Append(-1, "项目另存为")
        self.Bind(wx.EVT_MENU, self.OnSaveProjectAs, projectSaveAsItem)
 
        newProjectItem = fileMenu.Append(-1, "新建项目")
        self.Bind(wx.EVT_MENU, self.OnNewProject, newProjectItem)
 
        mainMenuBar.Append(fileMenu, title="&文件")
        
        self.SetMenuBar(mainMenuBar)
 
    def OnDirBrowser(self, e):
        dlg = wx.DirDialog(self,message="选择一个文件夹", style=wx.DD_DEFAULT_STYLE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
        else:
            path = ""
        
        dlg.Destroy()
 
        self.txtBox.SetLabel(path)
 
    def OnNewProject(self, e):
        if wx.Platform == "__WXMSW__":
            path = os.getenv("USERPROFILE")
        else:
            path = os.getenv("HOME")
 
        dlg = wx.DirDialog(self, "选择一个项目", path, wx.DD_NEW_DIR_BUTTON)
        ret = dlg.ShowModal()
        if ret == wx.ID_OK:
            prjPath = dlg.GetPath()
            if os.path.isdir(prjPath) and len(os.listdir(prjPath)) == 0:
                self.txtBox.SetLabel(prjPath)
 
        dlg.Destroy()
 
    def OnSaveProjectAs(self, e):
        if wx.Platform == "__WXMSW__":
            path = os.getenv("USERPROFILE")
        else:
            path = os.getenv("HOME")
 
        dlg = wx.DirDialog(self, "选择一个目录来保存项目", path, wx.DD_NEW_DIR_BUTTON)
        ret = dlg.ShowModal()
        if ret == wx.ID_OK:
            newPrjPath = dlg.GetPath()
            self.txtBox.SetLabel(newPrjPath)
        
        dlg.Destroy()
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleDirDialog(None)
    sample.Show()
    app.MainLoop()
 
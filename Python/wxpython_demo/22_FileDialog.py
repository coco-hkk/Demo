"""
文件选择对话框 FileDialog

wx.FileDialog 构造函数支持设置文件的缺省路径：
1. 参数 defaultDir 指定要选择的文件所在的缺省文件夹，如果该参数为空白，则目录为当前文件夹；
2. 参数 defaultFile 为默认文件，如果该参数为空白，则不提供默认文件；
3. 参数 wardcard 为匹配通配符，wx.FileDialog 允许用户选择一个或者多个文件，在使用通配符的情况下，可以让用户才只选择关心的文件。
   例如，"BMP files (*.bmp)|*.bmp|GIF files (*.gif)|*.gif" 只会显示和选择图片后缀类型是bmp和gif 的文件；
4. 参数 style 则指定对话框的打开样式。这些样式包括：

   - wx.FD_OPEN: 单个文件选择对话框；
   - wx.FD_SAVE: 文件保存对话框；
   - wx. FD_OVERWRITE_PROMPT: 只对保存对话框有效，当覆盖文件的时候，会弹出提醒对话框；
   - wx.FD_MULTIPLE：只对打开对话框有效，支持选择多个文件；
   - wx.FD_CHANGE_DIR：改变当前工作目录为用户选择的文件夹。

wx.FileDirlog 的常用方法：
- GetDirectory(self): 返回对话框默认的文件夹；
- GetFilename(self): 返回对话框默认的文件名；
- GetFilenames(self): 返回用户选择的文件列表；
- GetFileIndex(self): 返回通配符参数中提供的默认筛列表的索引(可选)；
- GetMessage(self): 返回文件对话框的标题信息；
- GetPath(self): 返回选择的文件的全路径(包括文件路径和文件名);
- GetPaths(self): 在多选情况下，返回用户选择的文件全路径列表;
- GetWildcard(self): 返回通配符；
- SetDirectory(self, dir): 设置对话框默认的文件目录；SetFileName(self, name): 设置对话框默认的文件名；
- SetFilterIndex(self, filterIndex): 设置默认筛选器索引，从0开始；
- SetMessage(self, message): 设置对话框的标题信息；
- SetPath(self, path): 设置默认选择的文件全路径名；
- SetWildCard(self, wildcard): 设置对话框文件类型通配符；
- ShowModal(self): 显示对话框，如果点击了wx.OK按钮则返回wx.ID_OK,否则返回wx.ID_CANCEL。


wx.FileSelector 全局方法，可以弹出一个文件选择对话框，该方法的原型为：

wx.FileSelector(message, defautPath, defaultFile, defaultExtension, wildcard, flags, parent, x, y)

- message： 文件选择器的标题。
- defautPath： 默认路径，缺省为空白。
- defaultFile：默认文件名，缺省为空白。
- defaultExtension：默认文件扩展名，缺省为空白。
- wildcard：通配符，缺省为“*.*”。
- parent：父窗口。
- x：选择器水平显示位置。
- y：选择器垂直显示位置。
"""


#文件选择对话框(FileDialog)
 
import wx
 
class SampleFileDialog(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleFileDialog, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        #设置标题
        self.SetTitle("文件选择对话框")
        #设置窗口尺寸
        self.SetSize(480, 360)
        #设置窗口位置
        self.SetPosition(wx.DefaultPosition)
        #设置窗口样式
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)
        #创建状态栏
        self.CreateStatusBar()
        #创建菜单栏
        self.BuildMenuBar()
        self.Centre()
 
        #===== 显示选中的文件名 =====#
        label = wx.StaticText(self, -1, "当前选择的文件:")
        self.txtBox = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size = (-1, 300))
        #水平布局
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(label, 0, wx.ALL|wx.ALIGN_TOP)
        sizer.Add(self.txtBox, 1, wx.ALL|wx.ALIGN_CENTER)
        #向窗口中添加布局
        #self.SetSizerAndFit(sizer)
        self.SetSizer(sizer)
 
    def BuildMenuBar(self):
        mainMenuBar = wx.MenuBar()
 
        fileMenu = wx.Menu()
 
        openMenuItem = fileMenu.Append(-1, "打开单个文件")
        self.Bind(wx.EVT_MENU, self.OpenSingleFile, openMenuItem)
 
        saveMenuItem = fileMenu.Append(-1, "保存文件")
        self.Bind(wx.EVT_MENU, self.SaveFile, saveMenuItem)
 
        savePromptMenuItem = fileMenu.Append(-1, "保存文件及提示覆盖")
        self.Bind(wx.EVT_MENU, self.SavePromptFile, savePromptMenuItem)
 
        multipleOpenMenuItem = fileMenu.Append(-1,"多文件选择")
        self.Bind(wx.EVT_MENU, self.MultipleSelectFiles, multipleOpenMenuItem)
 
        mainMenuBar.Append(fileMenu, title="&文件")
 
        self.SetMenuBar(mainMenuBar)
 
    ## wx.FileDialog style: wx.FD_OPEN
    def OpenSingleFile(self, e):
        fileFilter = "Image Files (*.bmp)|*.bmp|" "All files (*.*)|*.*"
        fileDialog =wx.FileDialog(self, message="选择单个文件", wildcard=fileFilter, style=wx.FD_OPEN)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return
        path = fileDialog.GetPath()
        self.txtBox.SetLabel(path)
 
    ## wx.FileDialog style: wx.FD_SAVE
    def SaveFile(self, e):
        fileFilter = "Image Files (*.bmp)|*.bmp|" "All files (*.*)|*.*"
        fileDialog =wx.FileDialog(self, message="保存文件", wildcard=fileFilter, style=wx.FD_SAVE)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return
        path = fileDialog.GetPath()
        self.txtBox.SetLabel(path)
 
    ## wx.FileDialog style: wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
    def SavePromptFile(self, e):
        fileFilter = "Image Files (*.bmp)|*.bmp|" "All files (*.*)|*.*"
        fileDialog =wx.FileDialog(self, message="保存&prompt文件", wildcard=fileFilter, style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return
        path = fileDialog.GetPath()
        self.txtBox.SetLabel(path)
 
    ## wx.FileDialog style: wx.FD_OPEN | wx.FD_MULTIPLE
    def MultipleSelectFiles(self, e):
        fileFilter = "Image Files (*.bmp)|*.bmp|" "All files (*.*)|*.*"
        fileDialog =wx.FileDialog(self, message="多文件选择", wildcard=fileFilter, style=wx.FD_OPEN|wx.FD_MULTIPLE)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            return
        paths = fileDialog.GetPaths()
        for path in paths:
            self.txtBox.AppendText(path + "\n")
 
if __name__ == "__main__":
    app = wx.App()
    sample = SampleFileDialog(None)
    sample.Show()
    app.MainLoop()
 
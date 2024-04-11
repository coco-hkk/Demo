#网格控件(wx.grid)
 
import wx
import wx.grid
 
#grid column type
class GridColumnControlKind:
    Text = "Text"
    CheckBox = "CheckBox"
    Colour = "Colour"
 
class GridCellColorEditor(wx.grid.GridCellEditor):
    def Create(self, parent, id, evtHandler):
        """
        创建一个控件， 该控件必须继承自wx.Control
        *必须重载*
        """
 
        self.__parent = parent
        self.__dlgColor = None
        self.__btnColor = wx.Button(parent, id, "")
        self.SetControl(self.__btnColor)
 
        #添加新的事件句柄，防止窗口弹出后，单元格自动调用编辑器
        newEventHandler = wx._core.EvtHandler()
        if evtHandler:
            self.__btnColor.PushEventHandler(newEventHandler)
        self.__btnColor.Bind(wx.EVT_BUTTON, self.OnClick)
 
    def OnClick(self, e):
        self.__btnColor.SetFocus()
        self.ShowColorDialog()
 
    def SetSize(self, rect):
        """
        用于在单元格矩形中定位/调整编辑控件的大小。
        如果没有填充单元格(矩形)，那么一定要重写
        PaintBackground做一些必要的事情。
        """
        self.__btnColor.SetDimensions(rect.x, rect.y, rect.width + 2, rect.height + 2, wx.SIZE_ALLOW_MINUS_ONE)
 
    def Clone(self):
        """
        创建一个新对象，它是这个对象的副本
        *必须重载*
        """
        return GridCellColorEditor()
 
    def BeginEdit(self, row, col, grid):
        """
        从表中获取值并准备编辑控件开始编辑。将焦点设置为编辑控件。
        *必须重载*
        """
        self.startValue = grid.GetTable().GetValue(row, col)
        self.endValue = self.startValue
        self.__btnColor.SetBackgroundColour(self.startValue)
 
    def EndEdit(self, row, col, grid):
        """
        完成当前单元格的编辑。如果已发生改变，则返回True
        如有必要，可以销毁控件。
        *必须重载*
        """
        changed = False
        if self.endValue != self.startValue:
            changed = True
            grid.GetTable().SetValue(row, col, self.endValue) # 更新该表
            self.startValue = ""
        return changed
 
    def ShowColorDialog(self):
        colorDlg = wx.ColourDialog(self.__parent)
        self.__dlgColor = colorDlg
        colorDlg.GetColourData().SetColour(self.startValue)
        if wx.ID_OK == colorDlg.ShowModal():
            data = colorDlg.GetColourData()
            colour = data.GetColour()
            self.__btnColor.SetBackgroundColour(colour)
            self.endValue = colour
 
        del self.__dlgColor
        self.__dlgColor = None
 
class GridCellColorRender(wx.grid.GridCellRenderer):
    def __init__(self):
        wx.grid.GridCellRenderer.__init__(self)
 
    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        color = grid.GetTable().GetValue(row, col)
        dc.SetBrush(wx.Brush(color, wx.BRUSHSTYLE_SOLID))
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangle(rect)
        dc.SetBackgroundMode(wx.BRUSHSTYLE_TRANSPARENT)
 
    def GetBestSize(self, grid, attr, dc, row, col):
        return wx.Size(-1, -1)
 
    def Clone(self):
        return GridCellColorRender()
 
#根据具体业务逻辑定制grid的 table
class CustomGridTable(wx.grid.GridTableBase):
    def __init__(self):
        wx.grid.GridTableBase.__init__(self)
 
        #添加表的列的头
        self.colLabels = ["名字", "可见", "最小门限", "最大门限", "颜色"]
        #指定一个列的控制类型
        self.colControlKinds = [GridColumnControlKind.Text, 
                                GridColumnControlKind.CheckBox, 
                                GridColumnControlKind.Text,
                                GridColumnControlKind.Text,
                                GridColumnControlKind.Colour]
        self.colControlEditorEnableStatus = [True, True, False, False, True]
        self.rowLabels = ["", "", "", "", ""]
 
        #添加数据源
        self.data = [ 
            ['Mask 1', 1, "2.5","320.6",(200,20,100)]
            ,['Mask 2', 1, "2.5","320.6",(50,0,200)]
        ]
 
    def GetNumberRows(self):
        return len(self.data)
 
    def GetNumberCols(self):
        return len(self.colLabels)
 
    def IsEmptyCell(self, row, col):
        return False
 
    def GetValue(self, row, col):
        return self.data[row][col]
 
    def SetValue(self, row, col, value):
        self.data[row][col] = value
 
    def GetColLabelValue(self, col):
        return self.colLabels[col]
 
    def GetRowLabelValue(self, row):
        return self.rowLabels[row]
 
    def InsertRow(self, index, row):
        if len(self.data) < index:
            return
 
        self.data.insert(index, row)
        print(self.data)
        self.GetView().BeginBatch()
 
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_NOTIFY_ROWS_INSERTED, index, 1)
        self.GetView().ProcessTableMessage(msg)
 
        # ... same thing for columns ....
 
        self.GetView().EndBatch()
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_REQUEST_VIEW_GET_VALUES)
        self.GetView().ProcessTableMessage(msg)
 
    def DeleteRow(self, row):
        rowIndex = self.data.index(row)
        if rowIndex < 0:
            return
        
        self.data.remove(row)
 
        self.GetView().BeginBatch()
 
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED, rowIndex, 1)
        self.GetView().ProcessTableMessage(msg)
 
        # ... same thing for columns ....
        self.GetView().EndBatch()
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_REQUEST_VIEW_GET_VALUES)
        self.GetView().ProcessTableMessage(msg)
 
    def Clear(self):
        self.GetView().BeginBatch()
 
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED, 0, self.GetNumberRows())
        self.GetView().ProcessTableMessage(msg)
 
        # ... same thing for columns ....
        self.GetView().EndBatch()
        self.data = []
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_REQUEST_VIEW_GET_VALUES)
        self.GetView().ProcessTableMessage(msg)
        
 
    def AppendRow(self, row):
        self.data.append(row)
 
        self.GetView().BeginBatch()
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_NOTIFY_ROWS_APPENDED)
        self.GetView().ProcessTableMessage(msg)
 
        # ... same thing for columns ....
        self.GetView().EndBatch()
        msg = wx.grid.GridTableMessage(self, wx.grid.GRIDTABLE_REQUEST_VIEW_GET_VALUES)
        self.GetView().ProcessTableMessage(msg)
 
#对grid的功能进行封装 以方便处理
class CustomGrid(wx.grid.Grid):
    def __init__(self, parent, id, rowLabelSize = 0, customGridTable = None):
        wx.grid.Grid.__init__(self, parent, id)
 
        self.rowLabelSize = rowLabelSize
        self.__customTableSource = customGridTable
        self.SetTable(self.__customTableSource, True)
 
        self.__InitStyle()
 
        #设置column 对应的 editor
        self.__InitColumnsEditor()
 
        # self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK,self.__OnMouse)
        self.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.__OnCellSelected)
        self.Bind(wx.grid.EVT_GRID_EDITOR_CREATED, self.__OnEditorCreated)
 
    def __InitStyle(self):
        #设置选中后的背景色
        self.SetSelectionBackground(wx.Colour(237, 145, 33))
 
    def __InitColumnsEditor(self):
        index = -1
        for columnKind in self.__customTableSource.colControlKinds:
            index += 1
            if columnKind == GridColumnControlKind.CheckBox:
                self.__InitCheckBoxColumnEditor(index)
            elif columnKind == GridColumnControlKind.Colour:
                self.__InitColorColumnEditor(index)
 
    def __InitCheckBoxColumnEditor(self, columnIndex):
        attr = wx.grid.GridCellAttr()
        attr.SetEditor(wx.grid.GridCellBoolEditor())
        attr.SetRenderer(wx.grid.GridCellBoolRenderer())
        self.SetColAttr(columnIndex, attr)
 
    def __InitColorColumnEditor(self, columnIndex):
        attr = wx.grid.GridCellAttr()
        attr.SetEditor(GridCellColorEditor())
        attr.SetRenderer(GridCellColorRender())
        self.SetColAttr(columnIndex, attr)
 
    def __OnCellSelected(self, e):
        if self.__customTableSource.colControlEditorEnableStatus[e.Col]:
            wx.CallAfter(self.EnableCellEditControl)
            e.Skip()
 
        #设置行为选中状态 
        self.SelectRow(e.Row)
 
    def __OnEditorCreated(self, event):
        pass
 
    def ForceRefresh(self):
        wx.grid.Grid.ForceRefresh(self)
 
class SampleGrid(wx.Frame):
 
    def __init__(self, *args, **kw):
        super(SampleGrid, self).__init__(*args, **kw)
 
        self.InitUi()
 
    def InitUi(self):
        self.SetTitle("Gird 实例")
        self.SetSize(500, 300)
 
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        addButton = wx.Button(self, -1, "添加")
        deleteButton = wx.Button(self, -1, "删除")
        clearButton = wx.Button(self, -1, "清理")
        sizer.Add(addButton, 0, wx.SHAPED)
        sizer.Add(deleteButton, 0, wx.SHAPED)
        sizer.Add(clearButton, 0, wx.SHAPED)
 
        table = CustomGridTable()
        grid = CustomGrid(self, id = -1, customGridTable = table)
        self.__grid = grid
 
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(sizer)
        mainSizer.Add(grid, 1, wx.EXPAND)
        self.SetSizerAndFit(mainSizer)
 
        addButton.Bind(wx.EVT_BUTTON, self.OnAddClick)
        deleteButton.Bind(wx.EVT_BUTTON, self.OnDeleteClick)
        clearButton.Bind(wx.EVT_BUTTON, self.OnClearClick)
 
        self.Centre()
 
    def OnClearClick(self, e):
        table  = self.__grid.GetTable()
        table.Clear()
        print(self.__grid.GetTable().data)
 
    def OnDeleteClick(self, e):
        table  = self.__grid.GetTable()
        firstRow = table.data[0]
        table.DeleteRow(firstRow)
        print(self.__grid.GetTable().data)
 
    def OnAddClick(self, e):
        table  = self.__grid.GetTable()
        table.InsertRow(0, ['insert index ', 1, "2.5","110.6",(50,200,30)])
        print(self.__grid.GetTable().data)
 

if __name__ == "__main__":
    app = wx.App()
    sample = SampleGrid(None)
    sample.Show()
    app.MainLoop()
 
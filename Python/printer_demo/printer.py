"""
打印机自动化打印
1. 提示缺纸时，可能是因为打印设置的纸张大小和打印机中实际大小不一致。如软件中设置的不是 A4，打印机检测到的是 A4 纸。
2. 报错：pywintypes.error: (31, 'ShellExecute', '连到系统上的设备没有发挥作用。')
   打印机打印文件时会先打开文件，若系统中默认安装的软件不支持打印机则报此错误。
   安装 adobe pdf 并设置为 pdf 默认打开工具。
3. pywin32 文档：https://timgolden.me.uk/pywin32-docs/win32_modules.html
"""

import win32api
import win32con
import win32print


def printer_working(file: str, printer):
    """ 设置打印机参数并打印文件

    :param file: 待打印文件
    :param printer: 默认打印机
    """
    # 获取打印机权限
    PRINTER_DEFAULTS = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}

    # 连接到打印机
    printer = win32print.OpenPrinter(printer, PRINTER_DEFAULTS)

    # 获取打印机的 Capabilities 信息
    properties = win32print.GetPrinter(printer, 2)
    devmode = properties["pDevMode"]

    devmode.Fields |= (win32con.DM_ORIENTATION |
                       win32con.DM_PAPERSIZE |
                       win32con.DM_SCALE |
                       win32con.DM_COPIES |
                       win32con.DM_DUPLEX)
    # 纸张大小 A4
    devmode.PaperSize = win32con.DMPAPER_A4
    # 单面打印
    devmode.Duplex = win32con.DMDUP_SIMPLEX
    # 打印份数
    devmode.Copies = 1

    if file.endswith(".pdf"):
        # 横向打印
        devmode.Orientation = win32con.DMORIENT_LANDSCAPE
        # 缩放
        devmode.Scale = 150
    else:
        devmode.Orientation = win32con.DMORIENT_PORTRAIT
        devmode.Scale = 100

    properties["pDevMode"] = devmode
    win32print.SetPrinter(printer, 2, properties, 0)

    # 这种方式没有使用 win32print 所提供的方法
    win32api.ShellExecute(0, "print", file, None, ".", 0)


if __name__ == "__main__":
    # 获取当前默认打印机
    doc = "file_path"
    default_printer = win32print.GetDefaultPrinter()
    printer_working(doc, default_printer)

from PyQt5.QtGui import *
# from functools import partial
import copy


# 负责解决Fliter菜单解决的事件
class Filter(object):

    def __init__(self, filename):
        import xlrd
        self.rbook = xlrd.open_workbook(filename)
        self.sheet_list = []
        self.rsheet = self.rbook.sheet_by_index(0)
        self.sheet_struct = {
            '日期': "",
            '机构代码': [],
            '本期日均余额': [],
            '本期增长': [],
            '活期存储': [],
            '定活两便': [],
            '通知存款': {
                x: [] for x in self.rsheet.row_values(4, 7, 9)
            },
            '定期储蓄': {
                '整存整取': {
                    x: [] for x in self.rsheet.row_values(4, 9, 16)
                },
                '整存整取协议存款': {
                    x: [] for x in self.rsheet.row_values(4, 16, 22)
                },
                '零存整取': {
                    x: [] for x in self.rsheet.row_values(4, 22, 25)
                }
            }
        }
        for i in range(self.rbook.nsheets):
            self.rsheet = self.rbook.sheet_by_index(i)
            start = 5
            end = 25
            sheet = copy.deepcopy(self.sheet_struct)
            sheet['日期'] = self.rsheet.cell_value(1, 12)
            sheet['机构代码'] = self.rsheet.col_values(0, start, end)
            sheet['本期日均余额'] = self.rsheet.col_values(2, start, end)
            sheet['本期增长'] = self.rsheet.col_values(4, start, end)
            sheet['活期存储'] = self.rsheet.col_values(5, start, end)
            sheet['定活两便'] = self.rsheet.col_values(6, start, end)
            col = 7
            # 录入带天数的数据]
            for i in list(sheet['通知存款'].keys()):
                sheet['通知存款'][i] = self.rsheet.col_values(col, start, end)
                col += 1
            for i in list(sheet['定期储蓄'].keys()):
                for j in list(sheet['定期储蓄'][i].keys()):
                    sheet['定期储蓄'][i][j] = self.rsheet.col_values(col, start, end)
                    col += 1
            self.sheet_list.append(sheet)

    def get_sheet_list(self):
        return self.sheet_list

    def get_date_list(self):
        return [x['日期'] for x in self.sheet_list]

    def get_index_dict(self):
        return self.sheet_struct

    def get_institution_code(self):
        return self.rsheet.col_values(0, 5, 25)

    def get_data_by_institution_code(self, code):
        index = '机构代码'
        dict = copy.deepcopy(self.sheet_struct)
        dict.pop(index)
        dict['日期'] = []  # 把字符串的值形式改为变为列表

        def updateDict(tmp, tmp_sheet):
            for key in tmp.keys():
                if type(tmp[key]) != type(tmp):
                    if key == "日期":
                        tmp[key].append(tmp_sheet[key])
                    else:
                        tmp[key].append(tmp_sheet[key][row])
                else:
                    updateDict(tmp[key], tmp_sheet[key])

        for sheet in self.sheet_list:
            row = 0  # 找到机构代码对应的行
            for i, codes in enumerate(sheet[index]):
                if code == codes:
                    row = i
                    break

            updateDict(dict, sheet)

        return dict
    def get_data_by_date(self, date):
        index = '日期'
        for sheet in self.get_sheet_list():
            if sheet['日期']==date:
                import copy
                return copy.deepcopy(sheet)
    def get_name_list(self):
        dict=self.sheet_struct
        name_list=[]
        def get_key_name(dict,name=""):
            for key in dict:
                name = name + " " + key
                if type(dict[key])!=type(dict):
                    name_list.append(name)
                else:
                    get_key_name(dict[key],name)
                name=" ".join(name.split(" ")[:-1])
        get_key_name(dict)
        import copy
        return copy.deepcopy(name_list)

# 负责解决Window菜单触发的事件
class WinSize(object):
    def __init__(self, window):
        self.window = window

    def adjust(self, *args):
        # 屏幕自适应
        screenSize = 2
        if (not args):
            f = open('setting.txt', 'r', encoding='utf8')
            try:  # 文件可能为空
                screenSize = float(f.readline().strip())
            except:
                pass
            f.close()
        else:
            screenSize = args[0]
        import win32api, win32con
        self.window.resize(win32api.GetSystemMetrics(win32con.SM_CXSCREEN) / screenSize,
                           win32api.GetSystemMetrics(win32con.SM_CYSCREEN) / screenSize)


# 负责解决菜单触发的事件
class FileController(object):
    def __init__(self, sc):
        self.sc = sc

    def openXLS(self, filename):
        import xlrd
        length = len(filename)
        if filename[length - 5:length] == ".xlsx" or filename[length - 4:length] == ".xls":
            rbook = xlrd.open_workbook(filename)  # 打开文件
            sheet = rbook.sheet_by_index(0)  # 打开对应的表
            nrow = sheet.nrows
            ncol = sheet.ncols  # 找到行列总数
            model = QStandardItemModel(nrow, ncol)
            # model.setHorizontalHeaderLabels(['0','1','2','3'])#设置表头
            for row in range(nrow):
                for col in range(ncol):
                    item = QStandardItem(str(sheet.cell_value(row, col)))
                    model.setItem(row, col, item)

            self.sc.setTableViewModel(model)
        else:
            self.sc.setText("不支持打开该文件")
        return sheet


# 负责解决操作菜单触发的事件
class Opration(object):
    def __init__(self, sheet, sc):
        self.sheet = sheet
        self.sc = sc

    def getSum(self):

        sum = 0
        for row in range(self.sheet.nrows):
            for col in range(self.sheet.ncols):
                sum += self.sheet.cell_value(row, col)
        self.sc.setText("总和 = %s" % sum)

    def drawTendency(self):
        import numpy as np
        import matplotlib.pyplot as plt
        x = np.linspace(0, self.sheet.nrows, self.sheet.nrows)
        y = []
        for row in range(self.sheet.nrows):
            for col in range(self.sheet.ncols):
                y.append(self.sheet.cell_value(row, col))
        plt.plot(x, y)
        plt.show()

    def addRatioButton(self):
        layout = self.sc.get_layout()
        self.sc.add_ratio_button("b6", layout)
        pass

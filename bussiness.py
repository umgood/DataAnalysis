from untitled import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from basicFuc import *
from showController import showController
import sys


class Bss(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)  # 生成应用
        self.window = QtWidgets.QMainWindow()  # 生成窗口q
        self.ui = Ui_MainWindow()  # 使用QTdesigner自动创建的类
        self.flag = 0

    def startWin(self):
        self.flag = 0  # 判断是否读入文件
        self.ui.setupUi(self.window)
        self.sc = showController(self.ui, self.window)
        self.winsize = WinSize(self.window)
        self.winsize.adjust()
        self.window.show()
        self.menuConnect()
        sys.exit(self.app.exec_())

    def menuConnect(self):
        self.ui.menuFile.triggered[QAction].connect(self.importFile)  # 菜单触发
        self.ui.menuWindow.triggered[QAction].connect(self.setWindowSize)  # 菜单触发调整窗口大小
        self.ui.menu.triggered[QAction].connect(self.op)  # 菜单触发调整窗口大小
        self.ui.menuFilter.triggered[QAction].connect(self.filterFunc)  # 菜单触发选择过滤器

    # 下拉菜单触发函数
    def handleActivatedInstitutionCode(self, index):
        code = self.combox.itemText(index)  # 通过下拉框索引找到相应的机构代码
        data = self.filter.get_data_by_institution_code(code)
        self.sc.setText(str(data))
        import functools
        date_list = data.pop('日期')

        def create_button(dict, name=""):
            for key in dict:
                name = name + " " + key
                if type(dict[key]) != type(dict):
                    b = self.sc.add_push_button(name + "变化", self.sc.get_layout())
                    b.clicked.connect(
                        functools.partial(self.sc.draw_tendency_by_date, date_list, dict[key], name + "变化"))

                else:
                    create_button(dict[key], name)
                name = " ".join(name.split(" ")[:-1])  # 减去上一个key

        create_button(data)  # 找到字典中最底层的键值,并添加按钮

    def handleActivatedDate(self, index):
        date = self.combox.itemText(index)  # 通过下拉框索引找到相应的日期
        data = self.filter.get_data_by_date(date)
        self.sc.setText(str(data))
        data.pop('日期')
        institution_list = data.pop('机构代码')

        import functools
        def create_button(dict, name=""):
            for key in dict:
                name = name + " " + key
                if type(dict[key]) != type(dict):
                    b = self.sc.add_push_button(name, self.sc.get_layout())
                    b.clicked.connect(
                        functools.partial(self.sc.draw_tendency, institution_list, dict[key], name))

                else:
                    create_button(dict[key], name)
                name = " ".join(name.split(" ")[:-1])  # 减去上一个key

        create_button(data)  # 找到字典中最底层的键值,并添加按钮

    # 按钮触发
    def handleActivatedCheckBox(self):
        checked_list = []
        for checkBox in self.checkBox_list:
            if checkBox.isChecked():
                checked_list.append(checkBox.text())
        data_list = []
        for code in checked_list:
            data_list.append(self.filter.get_data_by_institution_code(code))
        self.sc.setText(str(data_list))
        for data in data_list:
            date_list = data.pop('日期')
        key_value_list = []

        def findValue(dict):
            for key in dict:
                if type(dict[key]) != type(dict):
                    key_value_list.append(dict[key])
                else:
                    findValue(dict[key])

        key_value_list_list = []
        for data in data_list:
            key_value_list = []
            findValue(data)  # 找到字典中最底层的键值
            key_value_list_list.append(key_value_list)
        import functools
        def create_button(dict, i, name=""):
            # print(dict,i)
            for key in dict:
                name = name + " " + key
                if type(dict[key]) != type(dict):
                    i = i + 1
                    b = self.sc.add_push_button(name, self.sc.get_layout())
                    b.clicked.connect(
                        functools.partial(self.sc.draw_tendency_compare, date_list, [x[i] for x in key_value_list_list],
                                          checked_list,
                                          name))
                else:
                    create_button(dict[key], i, name)
                name = " ".join(name.split(" ")[:-1])  # 减去上一个key

        for i in range(self.sc.get_layout().count()):
            x = self.sc.get_layout().itemAt(i)
            x.widget().deleteLater()  # 清除布局内容
        create_button(data_list[0], 0)  # 找到字典中最底层的键,并添加按钮
        # print(key_value_list)

    def handleActivatedCheckBox2(self):
        checked_list = []  # 被选中的项目
        checked_index_list = []  # 选中项目的索引
        for index, checkBox in enumerate(self.checkBox_list):
            if checkBox.isChecked():
                checked_list.append(checkBox.text())
                checked_index_list.append(index)
        if not checked_list:  # 如果表为空则返回
            return
        combox_text = self.combox.currentText()
        comboxDate_text = self.comboxDate.currentText()
        data_list = []  # 获取某一月份的某一机构的数据，放入表中
        data = self.filter.get_data_by_date(comboxDate_text)
        data.pop('日期')
        for index, code in enumerate(data.pop('机构代码')):
            if code == combox_text:
                def findValue(dict):
                    for key in dict:
                        if type(dict[key]) != type(dict):
                            data_list.append(dict[key][index])
                        else:
                            findValue(dict[key])

                findValue(data)
                break
        checked_content_list = []
        for index in checked_index_list:
            checked_content_list.append(data_list[index])
        self.sc.draw_pie_compare(checked_content_list, checked_list, "机构" + combox_text + comboxDate_text + "储蓄占额比较")

    # menuFunction
    def filterFunc(self, q):
        if self.flag == 0:  # 判断表格是否读入
            self.sc.alert("请导入数据")
            return
        self.filter = Filter(self.filename)
        layout = self.sc.get_layout()
        # 删除layout中所用的Item
        for i in range(layout.count()):
            x = layout.itemAt(i)
            x.widget().deleteLater()
        try:
            self.ui.pushButton.disconnect()  # 解除按钮的所有绑定
        except:
            pass
        if q.text() == "getDataByInstitutionCode":
            # self.sc.add_vertical_spacer(layout)
            self.sc.add_textLabel("机构代码", layout)
            self.combox = self.sc.add_comboBox("cb", layout)
            institution_code = self.filter.get_institution_code()
            self.combox.addItems(institution_code)  # 给下拉菜单添加项目
            self.combox.activated.connect(self.handleActivatedInstitutionCode)  # 下拉菜单选中

        if q.text() == "getDateList":
            self.sc.setText("dateList as following...")
            for i in self.filter.get_date_list():
                self.sc.appendText(i)
        if q.text() == "getIndex":
            dict = self.filter.get_index_dict()
            self.sc.setText("indexList as following...")
            self.sc.printkeys(dict, 0)  # 打印字典中的键值
        if q.text() == "getDataByDate":
            self.sc.add_textLabel("日期", layout)
            self.combox = self.sc.add_comboBox("cb", layout)
            self.combox.addItems(self.filter.get_date_list())  # 给下拉菜单添加项目
            self.combox.activated.connect(self.handleActivatedDate)  # 下拉菜单选中
        if q.text() == "compareInstitution":
            self.sc.add_textLabel("请选择需要对比的机构", layout)
            code_list = self.filter.get_institution_code()
            self.checkBox_list = []
            for code in code_list:
                checkBox = self.sc.add_checkBox(code, layout)
                self.checkBox_list.append(checkBox)
            self.ui.pushButton.clicked.connect(self.handleActivatedCheckBox)
        if q.text() == "compareInnerStorage":
            self.sc.add_textLabel("请选择需要对比的机构以及月份", layout)
            self.combox = self.sc.add_comboBox("cb", layout)
            self.combox.addItems(self.filter.get_institution_code())  # 给下拉菜单添加项目
            self.comboxDate = self.sc.add_comboBox("cbDate", layout)
            self.comboxDate.addItems(self.filter.get_date_list())  # 给下拉菜单添加项目
            self.checkBox_list = []
            for name in self.filter.get_name_list():
                # 注意名字前有个空格
                if name == " 日期" or name == " 机构代码" or name == " 本期日均余额" or name == " 本期增长":
                    continue
                checkBox = self.sc.add_checkBox(name, layout)
                self.checkBox_list.append(checkBox)
            self.ui.pushButton.clicked.connect(self.handleActivatedCheckBox2)

    def importFile(self, q):
        # # 以下是打开文件对话框以及获取文件名的方法
        # import win32ui
        # dlg = win32ui.CreateFileDialog(1)
        # # dlg.SetOFNInitialDir('D:/Work')  # 设置打开文件对话框中的初始显示目录,无效
        # dlg.DoModal()
        # try:
        #     self.filename = dlg.GetPathName()  # 获取选择的文件名称
        #     fc = FileController(self.sc)
        #     self.sheet = fc.openXLS(self.filename)  # 返回表格内容
        #     self.flag = 1  # 文件已打开
        # except:
        #     print("fail")
        self.filename = "余额数据.xlsx"
        self.flag = 1  # 文件已打开

    def op(self, q):
        if self.flag == 0:  # 判断表格是否读入
            self.sc.alert("请导入数据")
            return
        text = q.text()
        opr = Opration(self.sheet, self.sc)
        if text == "getSum":
            opr.getSum()
        if text == "drawTendency":
            opr.drawTendency()
        if text == "addRationButton":
            opr.addRatioButton()

    def setWindowSize(self,
                      q):
        self.sc.setWindowSize(q)

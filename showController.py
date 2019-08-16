from PyQt5 import QtCore, QtWidgets
from basicFuc import WinSize
from PyQt5.QtWidgets import QMessageBox


class showController(object):

    def __init__(self, ui, window):
        self._translate = QtCore.QCoreApplication.translate  # 给UI加文字
        self.ui = ui
        self.window = window

    def draw_tendency_by_date(self, x_list, y_list, title):

        import matplotlib.pyplot as plt
        x = x_list.copy()
        for i, v in enumerate(x_list):
            x[i] = x_list[i][5:]
        y = y_list
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.title(title)
        plt.xlabel("date")
        plt.ylabel("单位：万元")
        plt.plot(x, y)
        plt.show()

    def draw_tendency(self, x_list, y_list, title):
        import matplotlib.pyplot as plt
        # 设置matplotlib正常显示中文和负号
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # 生成画布
        plt.figure(figsize=(20, 8), dpi=80)
        y = y_list
        x = x_list
        plt.title(title)
        plt.xlabel("机构代码")
        plt.ylabel("单位：万元")
        color = ['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c']
        plt.bar(x, y, width=0.5, color=color)
        # plt.xticks(x)

        plt.show()

    def draw_tendency_compare(self, x_list, y_list, checked_list, title):
        import matplotlib.pyplot as plt
        x = x_list.copy()

        for i, v in enumerate(x_list):
            x[i] = x_list[i][5:]
        # 生成画布
        plt.figure(figsize=(20, 8), dpi=80)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.title(title)
        plt.xlabel("date")
        plt.ylabel("单位：万元")

        for index, y in enumerate(y_list):
            plt.plot(x, y, label="机构" + checked_list[index])
        plt.legend()
        plt.show()

    def draw_pie_compare(self, value_list, label, title):
        import matplotlib.pyplot as plt
        plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
        plt.figure(figsize=(8, 8))  # 将画布设定为正方形，则绘制的饼图是正圆
        explode = [0.05] * len(value_list)        # 设定各项距离圆心n个半径
        plt.pie(value_list,explode=explode,labels=label, autopct='%1.1f%%')  # 绘制饼图
        plt.title(title)  # 绘制标题
        plt.show()

    def add_push_button(self, name, parent):
        new_object = QtWidgets.QPushButton(self.ui.centralwidget)
        new_object.setObjectName(name)
        parent.addWidget(new_object)
        new_object.setText(self._translate("MainWindow", name))
        return new_object

    def add_ratio_button(self, name, parent):
        new_object = QtWidgets.QRadioButton(self.ui.centralwidget)
        new_object.setObjectName(name)
        parent.addWidget(new_object)
        new_object.setText(self._translate("MainWindow", name))
        return new_object

    def add_checkBox(self, name, parent):
        new_object = QtWidgets.QCheckBox(self.ui.centralwidget)
        new_object.setObjectName(name)
        parent.addWidget(new_object)
        new_object.setText(self._translate("MainWindow", name))
        return new_object

    def add_comboBox(self, name, parent):
        new_object = QtWidgets.QComboBox(self.ui.centralwidget)
        new_object.setObjectName(name)
        parent.addWidget(new_object)
        # parent.insertWidget(1,new_object)
        return new_object

    def add_vertical_spacer(self, parent):
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        parent.addItem(spacerItem)

    def add_vertical_layout(self, name, parent):
        new_object = QtWidgets.QVBoxLayout(self.ui.centralwidget)
        new_object.setObjectName(name)
        parent.addLayout(new_object, 0, 7, 1, 1)
        new_object.setText(self._translate("MainWindow", name))
        return new_object

    def add_textLabel(self, name, parent):
        new_object = QtWidgets.QLabel(self.ui.centralwidget)
        new_object.setObjectName(name)
        parent.addWidget(new_object)
        new_object.setText(self._translate("MainWindow", name))
        return new_object

    def get_layout(self):
        return self.ui.verticalLayout

    def setWindowSize(self, q):
        f = open('setting.txt', 'w', encoding='utf8')
        self.winsize = WinSize(self.window)
        if q.text() == "S":
            self.winsize.adjust(2)
            f.write('2\n')
        if q.text() == "M":
            self.winsize.adjust(1.5)
            f.write('1.5\n')
        if q.text() == "L":
            self.winsize.adjust(1.2)
            f.write('1.2\n')
        if q.text() == "Full_Screen":
            self.window.showFullScreen()
        if q.text() == "Normal":
            self.window.showNormal()
        f.close()

    def setTableViewModel(self, model):
        self.ui.tableView.setModel(model)

    def setText(self, string):
        self.ui.textBrowser.setText(string)

    def appendText(self, string):
        self.ui.textBrowser.append(string)

    def alert(self, string, title="警告"):
        QMessageBox.information(self.window, title, string)

    def question(self, string, title="选择"):
        QMessageBox.question(self.window, title, string)

    # 用来打印字典键值的方法
    def printkeys(self, dict, space):  # space是空格，用来显示得更有层次
        for index, key in enumerate(dict, 1):
            space_str = str(index) + "." + str(key)
            for i in range(space):
                space_str = ">" * 2 + space_str
            self.appendText(space_str)
            if type(dict[key]) == type(dict):
                self.printkeys(dict[key], space + 1)

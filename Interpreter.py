# 不需要整天右键，直接执行该文件即可重新得到界面文件
from bussiness import Bss

if __name__ == '__main__':
    import reInterpreter as inter

    inter.reInterpreter('untitled')
    bss = Bss()
    bss.startWin()

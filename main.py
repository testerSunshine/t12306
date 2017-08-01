#-*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from gui import Splash, Login
from lib import logger
from config import configGui

app = QApplication(sys.argv)
app.processEvents()

# 显示Logo
splashWindow = Splash(QPixmap(configGui.getImage("splash.png")))
splashWindow.fadeInTicker()
splashWindow.fadeOutTicker()

# #显示登录页面
loginWindow = Login()
loginWindow.show()

#显示主页面
# mian = Main()
# mian.show()

sys.exit(app.exec_())
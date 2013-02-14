# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iris_ui.ui'
#
# Created: Sat Feb  2 17:15:24 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.splitter = QtGui.QSplitter(MainWindow)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName("splitter")
        
        self.treeWidget = QtGui.QTreeWidget(self.splitter)
        self.treeWidget.setHeaderLabel(u'文件')
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.treeWidget.setObjectName("treeView")
        
        self.textEdit = QtGui.QTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFocus()
        self.textEdit.setFont(QtGui.QFont("Times New Roman", 15, QtGui.QFont.Light))
        
        MainWindow.setCentralWidget(self.splitter)
        self.splitter.setStretchFactor(1,1)
        
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        self.actionNewfile = QtGui.QAction(MainWindow)
        
        self.actionNewfile.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/img/newfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNewfile.setIcon(icon1)
        self.actionNewfile.setObjectName("actionNewfile")
        self.actionImport = QtGui.QAction(MainWindow)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/img/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionImport.setIcon(icon2)
        self.actionImport.setObjectName("actionImport")
        self.actionNewtag = QtGui.QAction(MainWindow)
        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/img/newtag.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNewtag.setIcon(icon3)
        self.actionNewtag.setObjectName("actionNewtag")
        self.actionDel = QtGui.QAction(MainWindow)
        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionDel.setIcon(icon4)
        self.actionDel.setObjectName("actionDel")
        self.actionPreview = QtGui.QAction(MainWindow)
        
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/img/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionPreview.setIcon(icon5)
        self.actionPreview.setObjectName("actionPreview")
        self.actionExport = QtGui.QAction(MainWindow)
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/img/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExport.setIcon(icon6)
        self.actionExport.setObjectName("actionExport")
        self.actionUndo = QtGui.QAction(MainWindow)
        
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/img/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionUndo.setIcon(icon7)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/img/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionRedo.setIcon(icon8)
        self.actionRedo.setObjectName("actionRedo")
        self.actionAbout = QtGui.QAction(MainWindow)
        
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/img/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtGui.QAction(MainWindow)
        
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/img/savefile.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSave.setIcon(icon10)
        self.actionSave.setObjectName("actionSave")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Iris模联写作工具", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionNewfile.setText(QtGui.QApplication.translate("MainWindow", "新建文件", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewfile.setToolTip(QtGui.QApplication.translate("MainWindow", "新建文件", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewfile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "导入文件", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setToolTip(QtGui.QApplication.translate("MainWindow", "导入文件", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionNewtag.setText(QtGui.QApplication.translate("MainWindow", "保存为新版本", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewtag.setToolTip(QtGui.QApplication.translate("MainWindow", "保存为新版本", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewtag.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionDel.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDel.setToolTip(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDel.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionPreview.setText(QtGui.QApplication.translate("MainWindow", "预览", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setToolTip(QtGui.QApplication.translate("MainWindow", "预览", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "导出", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setToolTip(QtGui.QApplication.translate("MainWindow", "导出", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "撤销", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setToolTip(QtGui.QApplication.translate("MainWindow", "撤销", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "恢复", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setToolTip(QtGui.QApplication.translate("MainWindow", "恢复", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "关于", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setToolTip(QtGui.QApplication.translate("MainWindow", "关于Iris", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "保存", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("MainWindow", "保存", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        
        self.toolBar.addAction(self.actionNewfile)
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionNewtag)
        self.toolBar.addAction(self.actionDel)
        self.toolBar.addAction(self.actionPreview)
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.setIconSize(self.toolBar.iconSize()*1.3)
        
        
import res_rc

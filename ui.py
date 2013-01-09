# -*- coding: utf-8 -*-

import sys
import os
import time
import shutil

from PySide.QtGui import *
from PySide.QtCore import *

import mtf


class IrisUI(QMainWindow):
    
    currentFile = 'temp.mtf' 
    
    def __init__(self):
        super(IrisUI, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.fileList = QTreeWidget()
        self.textEdit = QTextEdit()
        splitter = QSplitter(self)
        
        self.fileList.setHeaderLabel('Files')
        self.textEdit.setFont(QFont("Times New Roman", 15, QFont.Light))
        splitter.addWidget(self.fileList)
        splitter.addWidget(self.textEdit)
        splitter.setStretchFactor(1,1)
        self.setIconSize(self.iconSize()*1.3)
        
        self.setCentralWidget(splitter)
        self.initToolBar()
        self.textEdit.setFocus()
        self.initFileList()
        self.setWindowIcon(QIcon(os.path.join('img', 'logo.jpg')))

        self.setGeometry(50, 50, 1000, 650)
        self.setWindowTitle('Iris')
        
    def initToolBar(self):
        newfileAction = QAction(QIcon(os.path.join('img', 'newfile.png')), u'新建文档', self)
        newfileAction.setShortcut('Ctrl+N')
        newfileAction.triggered.connect(self.newFile)
        
        saveAction = QAction(QIcon(os.path.join('img', 'savefile.png')), u'保存', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)
        
        newtagAction = QAction(QIcon(os.path.join('img', 'newtag.png')), u'保存为新版本', self)
        newtagAction.setShortcut('Ctrl+E')
        newtagAction.triggered.connect(self.newtagFile)
        
        previewAction = QAction(QIcon(os.path.join('img', 'preview.png')), u'预览', self)
        previewAction.setShortcut('Ctrl+P')
        previewAction.triggered.connect(self.preview)
        
        exportAction = QAction(QIcon(os.path.join('img', 'export.png')), u'导出为PDF', self)
        exportAction.setShortcut('Ctrl+O')
        exportAction.triggered.connect(self.export)
        
        importAction = QAction(QIcon(os.path.join('img', 'import.png')), u'导入文件', self)
        importAction.setShortcut('Ctrl+I')
        importAction.triggered.connect(self.importFile)
        
        undoAction = QAction(QIcon(os.path.join('img', 'undo.png')), u'撤销', self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.undo)
        
        redoAction = QAction(QIcon(os.path.join('img', 'redo.png')), u'恢复', self)
        redoAction.setShortcut('Ctrl+Y')
        redoAction.triggered.connect(self.redo)
        
        aboutAction = QAction(QIcon(os.path.join('img', 'about.png')), u'关于Iris', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.triggered.connect(self.about)

        
        self.toolbar = self.addToolBar('Toolbar')
        #self.toolbar.setMovable(False)
        
        self.toolbar.addAction(newfileAction)
        self.toolbar.addAction(importAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(undoAction)
        self.toolbar.addAction(redoAction)
        self.toolbar.addAction(newtagAction)
        self.toolbar.addAction(previewAction)
        self.toolbar.addAction(exportAction)
        self.toolbar.addAction(aboutAction)
    
    def newFile(self):
        print 'New File!'
        (newfileName, ok) = QInputDialog.getText(self, u'新建', u'请输入新文档名称')
        if ok:
            if os.path.isdir(newfileName):
                QMessageBox.warning(self, u'错误', u'文档'+newfileName+u'已存在！')
            else:
                os.mkdir(newfileName)
                self.currentFile = os.path.join(newfileName, newfileName+'-%d'%len(os.listdir(newfileName))+'.mtf') 
                f = open(self.currentFile, 'w')
                f.write('='+newfileName+'\n')
                f.close()
                self.textEdit.setText('='+newfileName)
                self.textEdit.textCursor().movePosition(QTextCursor.End)
                
                
    def saveFile(self):
        print 'Save File!'
        if not self.currentFile:
            self.currentFile = 'temp.mtf'
        f = open(self.currentFile, 'w')
        f.write(self.textEdit.toPlainText())
        f.close()
        
    def newtagFile(self):
        print 'Newtag!'
        self.currentFile = os.path.join(self.currentFile, self.currentFile+'-%d'%len(os.listdir(self.currentFile))+'.mtf') 
        f = open(self.currentFile, 'w')
        f.write(self.textEdit.toPlainText())
        
    def preview(self):
        print 'Preview!'
        self.saveFile()
        text = self.textEdit.toPlainText()
        if text:
            mtf.mtfToHtml(text)
            os.system(self.currentFile.split('.')[0]+'.html')
        print text
        
    def export(self):
        print 'Export!'
        self.saveFile()
        mtf.mtfToHtml(self.textEdit.toPlainText())
        print self.textEdit.toPlainText()
        if QMessageBox.information(self, u'导出',u'转换结束！点击确定打开文件。'):
            os.system('test.html')
        
    def importFile(self):
        print 'Import File!'
        (importFile, _) = QFileDialog.getOpenFileName(self, u'导入文件', os.path.expanduser('~'), '*.mtf')
        (_, newfileName) = os.path.split(importFile)
        if os.path.isdir(newfileName):
            if not QMessageBox.accept(self, u'提示', u'已有同名文档，是否导入成新的版本？'):
                (newfileName, ok) = QInputDialog.getText(self, u'重命名文档', u'请输入新文档名称')

        os.mkdir(newfileName)
        shutil.copy(importFile, os.path.join(newfileName, newfileName+'-%d'%len(os.listdir(newfileName))+'.mtf'))
        
    def undo(self):
        print 'Undo!'
        self.textEdit.undo()
        
    def redo(self):
        print 'redo!'
        self.textEdit.redo()

    def about(self):
        QMessageBox.about(self, u'关于Iris', \
                          u'''<h2>Iris 模联文件写作工具</h2>
                             <p>作者： IO_Error （东北育才学校）</p>
                             <p>本软件是基于PySide开发，并采用GPL v3协议授权的自由软件。</p>
                             <p>项目地址为：
                             <a href="https://github.com/Kevin6241/muntool-iris">https://github.com/Kevin6241/muntool-iris</a>
                             </p>''')
        
    def initFileList(self):
        print "File List inited!"
                
    def __del__(self):
        if os.path.exists('temp.mtf'):
            os.remove('temp.mtf')
        if os.path.exists('temp.html'):
            os.remove('temp.html')
    
def main():
    app = QApplication(sys.argv)
    iris = IrisUI()
    iris.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
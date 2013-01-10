# -*- coding: utf-8 -*-

import sys
import os
import time
import shutil

from PySide.QtGui import *
from PySide.QtCore import *

import mtf


class IrisUI(QMainWindow):
    
    tempMtf = os.path.join('work', 'temp.mtf')
    tempHtml = os.path.join('work', 'temp.html')
    currentMtf = tempMtf
    currentHtml = tempHtml
    
    def __init__(self):
        super(IrisUI, self).__init__()
        if not os.path.exists('work'):
            os.mkdir('work')
        self.initUI()
    
    def initUI(self):
        self.fileTree = QTreeWidget()
        self.textEdit = QTextEdit()
        splitter = QSplitter(self)
        self.fileTree.setHeaderLabel(u'文档')
        self.fileTree.itemClicked.connect(self.changeFile)
        self.textEdit.setFont(QFont("Times New Roman", 15, QFont.Light))
        splitter.addWidget(self.fileTree)
        splitter.addWidget(self.textEdit)
        splitter.setStretchFactor(1,1)
        self.setIconSize(self.iconSize()*1.3)
        self.setCentralWidget(splitter)
        self.initToolBar()
        self.textEdit.setFocus()
        self.refreshTree()
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
            if os.path.isdir(os.path.join('work', newfileName)):
                QMessageBox.warning(self, u'错误', u'文档'+newfileName+u'已存在！')
            else:
                workDir = os.path.join('work', newfileName)
                os.mkdir(workDir)
                fileCount = len(os.listdir(workDir))
                print fileCount
                self.currentMtf = os.path.join(workDir, newfileName+'-%d'%fileCount+'.mtf') 
                f = open(self.currentMtf, 'w')
                f.write('='+newfileName+'\n')
                f.close()
                self.textEdit.setText('='+newfileName)
                self.textEdit.textCursor().movePosition(QTextCursor.End)
                self.refreshTree(newfileName, newfileName+'-%d'%fileCount+'.mtf')
                
    def saveFile(self):
        print 'Save File!'
        if not self.currentMtf:
            self.currentMtf = self.tempMtf
            
        print self.currentMtf
        f = open(self.currentMtf, 'w')
        f.write(self.textEdit.toPlainText())
        f.close()

    def newtagFile(self):
        print 'Newtag!'
        if self.currentMtf != self.tempMtf:
            self.currentMtf = os.path.join('work', self.currentMtf, self.currentMtf+'-%d'%len(os.listdir(self.currentMtf[:-6]))+'.mtf') 
            f = open(self.currentMtf, 'w')
            f.write(self.textEdit.toPlainText())
            f.close()
            self.refreshTree()
        
    def preview(self):
        print 'Preview!'
        self.saveFile()
        text = self.textEdit.toPlainText()
        if text:
            htmlStr = mtf.mtfToHtml(text)
            f = open(self.currentHtml, 'w')
            f.write(htmlStr)
            f.close()
            os.system(self.currentHtml)
        print htmlStr
        os.remove(self.currentHtml)
        
    def export(self):
        print 'Export!'
        self.saveFile()
        htmlStr = mtf.mtfToHtml(self.textEdit.toPlainText())
        print htmlStr
        f = open(self.currentHtml, 'w')
        f.write(htmlStr)
        f.close()
        if QMessageBox.information(self, u'导出',u'转换结束！点击确定打开文件。'):
            os.system(os.path.join(('work', self.currentMtf)))
        
    def importFile(self):
        print 'Import File!'
        (importFile, _) = QFileDialog.getOpenFileName(self, u'导入文件', os.path.expanduser('~'), '*.mtf')
        (_, newfileName) = os.path.split(importFile)
        newfileName = newfileName[:-6]
        print newfileName
        if os.path.isdir(newfileName):
            ans = QMessageBox.question(self, u'提示', u'已有同名文档，建立新的文档？', QMessageBox.Ok, QMessageBox.Cancel)
            print ans
            if ans == QMessageBox.Ok:
                (newfileName, ok) = QInputDialog.getText(self, u'重命名文档', u'请输入新文档名称')
                if ok:
                    workDir = os.path.join('work', newfileName)
                    os.mkdir(workDir)
                    shutil.copy(importFile, os.path.join(workDir, newfileName+'-%d'%len(os.listdir(workDir))+'.mtf'))
            else:
                shutil.copy(importFile, os.path.join(workDir, newfileName+'-%d'%len(os.listdir(workDir))+'.mtf'))
        self.refreshTree()
    
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
        
    def refreshTree(self, fFolder = '', fFile = ''):
        print "File List inited!", fFolder, fFile
        docs = []
        self.fileTree.clear()
        dirList = [folder \
                   for folder in os.listdir('work') \
                       if os.path.isdir(os.path.join('work', folder))]
        for folder in dirList:
            print folder
            doc = QTreeWidgetItem(self.fileTree)
            doc.setText(0, folder)
            for file in os.listdir(os.path.join('work', folder)):
                if file.split('.')[1] == 'mtf':
                    tag = QTreeWidgetItem(doc)
                    tag.setText(0, u'版本'+file[-5:-4])
                    doc.addChild(tag) 
                    print 'tag:', file
                    if file == fFile:
                        print 'tag yes'
                        tag.setSelected(True)
            print folder
            if folder == fFolder:
                
                print 'folder yes'
                doc.setExpanded(True)
            docs.append(doc)
        if docs:
            self.fileTree.addTopLevelItems(docs)
                        
    def changeFile(self):
        print 'change file!'
        self.saveFile()
        thisItem = self.fileTree.currentItem().parent()
        if thisItem:
            workDir = os.path.join('work', thisItem.text(0))
            self.currentMtf = os.path.join(workDir, thisItem.text(0)+'-%d'%(len(os.listdir(workDir))-1)+'.mtf')
            f = open(self.currentMtf)
            self.textEdit.setText(f.read())
            f.close()
        
    def __del__(self):
        if os.path.exists(self.tempMtf):
            os.remove(self.tempMtf)
        if os.path.exists(self.tempHtml):
            os.remove(self.tempHtml)
    
def main():
    app = QApplication(sys.argv)
    iris = IrisUI()
    iris.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
# -*- coding: utf-8 -*-

import sys, os, webbrowser, shutil, time
import ui
import filedb
import lib
from PySide import QtCore, QtGui

class iris(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initFun()
        self.fileDB = filedb.FileDB('work', self)
        self.refresh()
        
    def initFun(self):
        self.ui.actionNewfile.triggered.connect(self.newFile)
        self.ui.actionImport.triggered.connect(self.importFile)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionNewtag.triggered.connect(self.newTag)
        self.ui.actionDel.triggered.connect(self.delete)
        self.ui.actionPreview.triggered.connect(self.preview)
        self.ui.actionExport.triggered.connect(self.export)
        self.ui.actionUndo.triggered.connect(self.undo)
        self.ui.actionRedo.triggered.connect(self.redo)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.treeWidget.itemClicked.connect(self.changeFile)
    
    def newFile(self):
        (newfileName, ok) = QtGui.QInputDialog.getText(self, u'新建', u'请输入文档名')
        if ok:
            if self.fileDB.newDoc(newfileName) == True:
                self.ui.textEdit.setText(self.fileDB.currentDoc.currentTag.text)
            else:
                self.newFile()
            self.refresh()
            return True
        else:
            return False
        
    
    def saveFile(self):
        self.fileDB.save()
    
    def newTag(self):
        (tagName, ok) = QtGui.QInputDialog.getText(self, u'新建', u'请输入版本名')
        if ok:
            if self.fileDB.newTag(tagName, self.ui.textEdit.toPlainText()) == True:
                self.fileDB.setCurrentTag(tagName)
                self.ui.textEdit.setText(self.fileDB.currentDoc.currentTag.text)
            else:
                self.newFile()
        self.refresh()
        
    def delete(self):
        item = self.ui.treeWidget.currentItem()
        if item.parent():
            self.fileDB.currentDoc.deleteTag(item.text(0))
        else:
            self.fileDB.deleteDoc(item.text(0))
        self.refresh()
    
    def preview(self):
        text = self.ui.textEdit.toPlainText()
        if text:
            htmlStr = self.fileDB.toHtml(text)
            f = open('temp.html', 'w')
            f.write(htmlStr)
            f.close()
            webbrowser.open_new('temp.html')
            time.sleep(1)
            os.remove('temp.html')
    
    def export(self):
        self.fileDB.save()
        text = self.ui.textEdit.toPlainText()
        if text:
            (importFile, _) = QtGui.QFileDialog.getOpenFileName(self, u'导出文件', os.path.expanduser('~'), '*.html')
            htmlStr = self.fileDB.toHtml(text)
            f = open(importFile, 'w')
            f.write(htmlStr)
            f.close()
            webbrowser.open_new(importFile)
    
    def importFile(self):
        (importFile, _) = QtGui.QFileDialog.getOpenFileName(self, u'导入文件', os.path.expanduser('~'), '*.mtf')
        f = open(importFile)
        text = f.read()
        f.close()
        (_, newfileName) = os.path.split(importFile)
        newfileName = newfileName[:-6]
        if newfileName in self.fileDB.docs.keys():
            ans = QtGui.QMessageBox.question(self, u'提示', u'已有同名文档，建立新的文档？', QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
            if ans == QtGui.QMessageBox.Ok:
                (newfileName, ok) = QtGui.QInputDialog.getText(self, u'重命名文档', u'请输入新文档名称')
                if ok:
                    self.fileDB.newDoc(newfileName)
        else:
            self.fileDB.newDoc(newfileName)
        f = open(self.fileDB.currentDoc.currentTag.path, 'w')
        f.write(text)
        f.close()
        self.ui.textEdit.setText(text)
        self.refresh()
    
    def undo(self):
        self.ui.textEdit.undo()
    
    def redo(self):
        self.ui.textEdit.redo()
        
    def changeFile(self):
        item = self.ui.treeWidget.currentItem()
        lib.info('changeFile')
        if item:
            if item.parent():
                self.fileDB.setCurrentDoc(item.parent().text(0))
                self.fileDB.setCurrentTag(item.text(0))
                f = open(self.fileDB.currentDoc.currentTag.path)
                lib.info(self.fileDB.currentDoc.currentTag.path)
                self.ui.textEdit.setText(f.read())
                f.close()
            else:
                self.fileDB.setCurrentDoc(item.parent())
    
    def refresh(self):
        self.ui.treeWidget.clear()
        treeList = []
        fileDict =  self.fileDB.getFileDict()
        currentTag = None
        currentDoc = None
        if fileDict.has_key('currentDoc'):
            currentDoc = fileDict['currentDoc']
        if fileDict.has_key('currentTag'):
            currentTag = fileDict['currentTag']
        for doc in fileDict.keys():
            if doc != 'currentDoc' and doc != 'currentTag':
                docTreeItem = QtGui.QTreeWidgetItem(self.ui.treeWidget)
                docTreeItem.setText(0, doc)
                for tag in fileDict[doc]:
                    tagTreeItem = QtGui.QTreeWidgetItem(docTreeItem)
                    tagTreeItem.setText(0, tag)
                    if tag == currentTag:
                        tagTreeItem.setSelected(True)
                    docTreeItem.addChild(tagTreeItem)
                treeList.append(docTreeItem)
            if doc == currentDoc:
                docTreeItem.setExpanded(True)
        if treeList:
            self.ui.treeWidget.addTopLevelItems(treeList)      
    
    def about(self):
        QtGui.QMessageBox.about(self,  u'关于Iris', \
                          u'''<h2>Iris 模联文件写作工具 0.2</h2>
                             <p>作者： IO_Error （东北育才学校）</p>
                             <p>本软件是基于PySide开发，并采用GPL v3协议授权的自由软件。</p>
                             <p>项目地址为：
                             <a href="https://github.com/Kevin6241/muntool-iris">https://github.com/Kevin6241/muntool-iris</a>
                             </p>''')

def main():
    app = QtGui.QApplication(sys.argv)
    iris_ui = iris()
    iris_ui.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
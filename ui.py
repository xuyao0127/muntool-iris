# -*- coding: utf-8 -*-

import sys
import os
from PySide.QtGui import *
from PySide.QtCore import *
import mtf


class IrisUI(QMainWindow):
    
    fileitems = []
    
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
        newfileAction = QAction(QIcon(os.path.join('img', 'newfile.png')), 'New File', self)
        newfileAction.setShortcut('Ctrl+N')
        newfileAction.triggered.connect(self.newFile)
        
        saveAction = QAction(QIcon(os.path.join('img', 'savefile.png')), 'Save File', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)
        
        emergeAction = QAction(QIcon(os.path.join('img', 'emerge.png')), 'Emerge Document', self)
        emergeAction.setShortcut('Ctrl+E')
        emergeAction.triggered.connect(self.emergeFile)
        
        cloneAction = QAction(QIcon(os.path.join('img', 'clone.png')), 'Clone Document', self)
        cloneAction.setShortcut('Ctrl+C')
        cloneAction.triggered.connect(self.cloneFile)
        
        previewAction = QAction(QIcon(os.path.join('img', 'preview.png')), 'Preview', self)
        previewAction.setShortcut('Ctrl+P')
        previewAction.triggered.connect(self.preview)
        
        exportAction = QAction(QIcon(os.path.join('img', 'export.png')), 'Export to PDF', self)
        exportAction.setShortcut('Ctrl+O')
        exportAction.triggered.connect(self.export)
        
        importAction = QAction(QIcon(os.path.join('img', 'import.png')), 'Import File', self)
        importAction.setShortcut('Ctrl+I')
        importAction.triggered.connect(self.importFile)
        
        undoAction = QAction(QIcon(os.path.join('img', 'undo.png')), 'Undo', self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.undo)
        
        forwardAction = QAction(QIcon(os.path.join('img', 'forward.png')), 'Forward', self)
        forwardAction.setShortcut('Ctrl+Y')
        forwardAction.triggered.connect(self.forward)
        
        aboutAction = QAction(QIcon(os.path.join('img', 'about.png')), 'About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.triggered.connect(self.about)

        
        self.toolbar = self.addToolBar('Toolbar')
        #self.toolbar.setMovable(False)
        
        self.toolbar.addAction(newfileAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(emergeAction)
        self.toolbar.addAction(cloneAction)
        self.toolbar.addAction(previewAction)
        self.toolbar.addAction(exportAction)
        self.toolbar.addAction(importAction)
        self.toolbar.addAction(undoAction)
        self.toolbar.addAction(forwardAction)
        self.toolbar.addAction(aboutAction)
    
    def newFile(self):
        print 'New File!'
        
    def saveFile(self):
        print 'Save File!'
        
    def emergeFile(self):
        print 'Emerge File!'
        
    def cloneFile(self):
        print 'Clone File!'
        
    def preview(self):
        print 'Preview!'
        mtf.mtfToHtml(self.textEdit.toPlainText())
        print self.textEdit.toPlainText()
        if QMessageBox.information(self, u'预览',u'转换结束！'):
            os.system('test.html')
        
    def export(self):
        print 'Export!'
        
    def importFile(self):
        print 'Import File!'
        
    def undo(self):
        print 'Undo!'
        
    def forward(self):
        print 'Forward!'

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
        
        
def main():
    app = QApplication(sys.argv)
    iris = IrisUI()
    iris.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
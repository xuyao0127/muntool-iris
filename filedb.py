# -*- coding: utf-8 -*-

import os
import document
import tag
import lib
from PySide import QtGui

class FileDB():
    def __init__(self, workPath, win):
        if os.path.exists(workPath):
            self.workPath = workPath
        else:
            os.mkdir(workPath)
        self.docs = {}
        self.win = win
        self.currentDoc = None
        lib.info('Initializing File DataBase')
        for item in os.listdir(self.workPath):
            if os.path.isdir(os.path.join(self.workPath, item)):
                doc = document.Doc(item, os.path.join(self.workPath, item))
                self.docs[doc.name] = doc
        lib.info('Done')
        
    def setCurrentDoc(self, docName):
        if self.docs.has_key(docName):
            self.currentDoc = self.docs[docName]
            lib.info('Current Doc has changed to "'+self.currentDoc.name+'"')
            lib.info('Current Tag has changed to the last tag in the folder')
        else:
            lib.info('No such Doc named "'+docName)
            
    def setCurrentTag(self, tagName):
        if self.currentDoc.tags.has_key(tagName):
            self.currentDoc.currentTag = self.currentDoc.tags[tagName]
            lib.info('Current Tag has changed to "'+self.currentDoc.currentTag.name+'" in Doc "'+self.currentDoc.name+'"')
        else:
            lib.info('No such Tag named "'+tagName+'in Doc "'+self.currentDoc.name+'"')
            
    def deleteDoc(self, docName):
        if self.docs.has_key(docName):
            d = self.docs[docName]
            for tag in d.tags.values():
                os.remove(tag.path)
            os.rmdir(d.path)
            self.docs.pop(d.name)
            lib.info('Doc "'+docName+'" has been removed')
        else:
            lib.info('No such Doc named "'+docName)
            
    def newTag(self, tagName, content):
        if not self.currentDoc.tags.has_key(tagName):
            #self.save()
            tagPath = os.path.join(self.currentDoc.path, tagName+'.mtf')
            f = open(tagPath, 'w')
            f.write(content)
            f.close()
            newTag = tag.Tag(tagName, tagPath)
            self.currentDoc.tags[newTag.name] = newTag
            self.currentDoc.setCurrentTag(newTag.name)
            return True
        else:
            QtGui.QMessageBox.warning(self.win, u'错误', u'版本'+tagName+u'已存在')
            return False
            
    def newDoc(self, docName):
        if not self.docs.has_key(docName):
            docPath = os.path.join(self.workPath, docName)
            if os.path.exists(docPath):
                QtGui.QMessageBox.warning(self.win, u'错误', u'文档'+docName+u'已存在')
                return False
            try:
                os.mkdir(docPath)
            except:
                QtGui.QMessageBox.warning(self.win, u'错误', u'无法建立文档'+docName)
                return False
            newDoc = document.Doc(docName, docPath)
            self.docs[newDoc.name] = newDoc
            self.setCurrentDoc(docName)
            if self.newTag(docName, "% "+docName) == True:
                return True
        else:
            QtGui.QMessageBox.warning(self.win, u'错误', u'文档'+docName+u'已存在')
    
    def save(self):
        if self.currentDoc:
            if self.currentDoc.currentTag:
                f = open(self.currentDoc.currentTag.path, 'w')
                f.write(self.win.ui.textEdit.toPlainText())
                f.close()
        else:
            text = self.win.ui.textEdit.toPlainText()
            if self.win.newFile():
                self.win.ui.textEdit.setText(text)
                self.save()
               
    def getFileDict(self):
        fileDict = {}
        for item in self.docs.keys():
            fileDict[item] = self.docs[item].tags.keys()
        if self.currentDoc:
            fileDict['currentDoc'] = self.currentDoc.name
            if self.currentDoc.currentTag:
                fileDict['currentTag'] = self.currentDoc.currentTag.name
        return fileDict
    
    def __convertStr(self, token, content):
        try:
            if content[-1] == '\n':
                content = content[:-1]
            while content[0] in [' ', '\n', '\t']:
                content= content[1:]
        except:
            pass
        if token =='#':
            if len(content.split(' ', 1)) > 1:
                rtnStr = lib.tagList[token][0]+'<b><u><i>'+content.split(' ', 1)[0]+'</i></u></b>'+' '+content.split(' ', 1)[1]+lib.tagList[token][1]
            else:
                rtnStr = lib.tagList[token][0]+'<b><u><i>'+content+'</i></u></b>'+lib.tagList[token][1]
        elif token =='*':
            if len(content.split(' ', 1)) > 1:
                rtnStr = lib.tagList[token][0]+'<b><u>'+content.split(' ', 1)[0]+'</u></b>'+' '+content.split(' ', 1)[1]+lib.tagList[token][1]
            else:
                rtnStr = lib.tagList[token][0]+'<b><u>'+content+'</u></b>'+lib.tagList[token][1]
        else:
            rtnStr = lib.tagList[token][0]+content+lib.tagList[token][1]
            
        if (lib.start_li == True) and (token == '#'):
            rtnStr = '<ol>\n'+rtnStr
            lib.start_li = False
            print "start_li has been changed"
        elif (lib.start_li == False) and (token != '#'):
            rtnStr = '</ol>\n'+rtnStr
            lib.start_li = True
        return rtnStr

    def toHtml(self, mtfStr):
        mtfList = []
        newItem = ''
        for char in mtfStr:
            if char in lib.tokenList:
                if newItem:
                    mtfList.append(newItem)
                    newItem = ''
            newItem += char   
        mtfList.append(newItem)  
        print mtfList
        htmlList = ['<head><style type="text/css">', lib.style,'</style></head>', '<body>']
        for item in mtfList:
            if item:
                if not item[0] in lib.tokenList:
                    htmlList.append(self.__convertStr('=',item[0:]))
                else:
                    htmlList.append(self.__convertStr(item[0], item[1:]))
                
        htmlList.append('</body>')
        print htmlList
        htmlStr = '\n'.join(htmlList)
        return htmlStr
    
                
            
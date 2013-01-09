# -*- coding: utf-8 -*-
import sys
from PySide import QtGui

tokenList = ['+', '=', '*', '#']

tagList = {
    '=':['<h2>', '</h2>'], \
    '+':['<h3>', '</h3>'], \
    '*':['<p>', '</p>'], \
    '#':['<li>', '</li>']
}
    
def convert(token, content):
    if content[-1] == '\n':
        content = content[:-1]
    return tagList[token][0]+content+tagList[token][1]

def mtfToHtml(mtfStr):
    mtfList = []
    newItem = ''
    for char in mtfStr:
        if char in tokenList:
            if newItem:
                mtfList.append(newItem)
                newItem = ''
        newItem += char
        
    mtfList.append(newItem)
        
    print mtfList
    
    htmlList = ['<head><title>', 'test2', '</title></head>', '<body>']
    
    for item in mtfList:
        if item:
            if not item[0] in ['*', '+', '=', '#']:
                print "Unknown token "+item[0]+" occurs!"
                sys.exit(2)
            else:
                htmlList.append(convert(item[0], item[1:]))
            
    htmlList.append('</body>')
    htmlStr = '\n'.join(htmlList)
    
    f = open('test.html','w')
    f.write(htmlStr)
    f.close()
    

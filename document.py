import os
import tag
import lib

# -*- coding: utf-8 -*-

class Doc:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.tags = {}  
        lib.info('    Initializing Doc'+ self.name+' '+ self.path)
        self.currentTag = None
        for item in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, item)) and os.path.splitext(item)[1] == '.mtf':
                t = tag.Tag(os.path.splitext(item)[0], os.path.join(self.path, item))
                self.tags[t.name] = t 
                self.currentTag = t 
    
    def setCurrentTag(self, tagName):
        if self.tags.has_key(tagName):
            self.currentTag = self.tags[tagName]
            lib.info('Current Tag has changed to "'+self.currentTag.name+'" in Doc "'+self.name+'"')
        else:
            lib.info('No such Tag named "'+tagName+'in Doc "'+self.name+'"')
            
    def deleteTag(self, tagName):
        if self.tags.has_key(tagName):
            os.remove(self.tags[tagName].path)
            self.tags.pop(tagName)
            lib.info(u'Tag "'+tagName+u'" has been removed')
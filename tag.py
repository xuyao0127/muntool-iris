import lib

class Tag:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        try:
            f = open(self.path)
        except IOError:
            print 'Failed to open file: ', self.path
            return None
        self.text = f.read()
        f.close()
        lib.info('        Tag'+self.name+ ' ['+self.path+'] '+ 'initialized')
        
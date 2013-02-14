import os
import time

tokenList = ['=', '*', '#', '%']

tagList = {
    '=':['<h2>', '</h2>'], \
    '*':['<p>', '</p>'], \
    '#':['<li>', '</li>'], \
    '%':['<!--', '-->']
}

start_li = True

style = '''
    h2 {
        font: "Times New Roman";
        font-size: 16pt;
    }
    p {
        font: "Times New Roman";
        font-size: 14pt;
    }
    li {
        font: "Times New Roman";
        font-size: 14pt;
        list-style-type: decimal;
    }
    b {
        font: "Times New Roman";
        font-size: 14pt;
    }
'''

def info(msg):
    try:
        print '['+time.strftime('%Y-%m-%d %H:%M:%S')+'] : ', msg
    except:
        print  '['+time.strftime('%Y-%m-%d %H:%M:%S')+'] : '
def log(*msg):
    logTime = '['+time.strftime('%Y-%m-%d %H:%M:%S')+'] : '
    f = open('log', 'a')
    f.write(logTime,  ' '.join(msg))
    f.close()
    print logTime,  ' '.join(msg)
    
if __name__ == '__main__':
    info('this is a test log', 'info')
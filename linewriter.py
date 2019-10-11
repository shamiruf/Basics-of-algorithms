import os
STATICKY_TEXT="This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
def writeTextToFile(a):
    f = open('file.txt', 'w')
    f.write(STATICKY_TEXT + str(a))
    f.close()
    p = os.path.abspath('file.txt')
    name = os.path.basename(p)
    print (name)
    return name
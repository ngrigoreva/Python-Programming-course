def readfile():
    fi = open('викистатья.txt','r', encoding = 'utf-8') 
    f = fi.read()
    fi.close()
    return f

def funf (f):
    import re
    regex = '([IVXL]+ (?:— |век.| н. э.| до н. э.))'
    res = re.findall(regex, f)
    for elem in res:
        a = '\n'.join(res)
    stringa = str(a)
    x = re.sub(' век.+?', '', stringa)
    x1 = re.sub(' —', '', x)
    print(x1)

#def acht(f):
    #import re
    #result_f = open('exam.csv', 'w', encoding = 'utf-8')
    #regexb = '[0-9][0-9]?(?: (?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)|/.[0-9]{2}/.[0-9]+)'
    #resb = re.findall(regexb, f)
    #for elem in resb:
     #   b = '\n'.join(resb)
    #stringb = str(b)
    #print(stringb)
    #for elemb in b:
     #   s = list.count(elemb)
     #   print(s)
            
def main():
    f = readfile()
    x = funf(f)
    #y = acht(f)

main()

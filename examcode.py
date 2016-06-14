def readfile():
    fi = open('викистатья.txt','r', encoding = 'utf-8') 
    f = fi.read()
    fi.close()
    return f

def sc_field (f):
    #result_f = open('C:\\Курчатов_result.txt', 'w', encoding = 'utf-8')
    import re
    regex = '([IVXL]+? век.+?(?: н. э.)?(?: до н. э.)?)'
    res = re.findall(regex, f)
    for elem in res:
        a = '\n'.join(res)
    stringa = str(a)
    x = re.sub(' век.+?', '', stringa)
    print(x)
            
def main():
    f = readfile()
    x = sc_field(f)

main()

import sys
    
def hindu(x):
    x = x.replace("IV", ":4").replace("IX", ":9").replace("XL", ":40").replace("XC", ":90").replace("CD", ":400").replace("CM", ":900").replace("I", ":1").replace("V", ":5").replace("X", ":10").replace("L", ":50").replace("C", ":100").replace("D", ":500").replace("M", ":1000").split(':')
    x.remove("")
    sum1 = 0
    for num in x:
        sum1 += int(num)
    return sum1
    
def main(x):
    line = 1
    res = ""
    if not x.endswith('rn'):
        print('FILE ERROR: SHOULD BE IN "RN" FILE EXTENSION')
        return
    try:
        filer = open(x, "r").read().splitlines()
    except:
        print('FILE ERROR: FILE NAMED "{}" NOT FOUND'.format(x))
        return
    for rochar in filer:
        if ':' in rochar:
            try:
                res += chr(hindu(rochar[rochar.index(":")+1:]))
            except:
                print('SYNTAX ERROR: LINE {};\n"{}" -> INVALID ROMAN CODE'.format(line, rochar))
                return
        line += 1
    print(res)

if True:
    try:
        main(sys.argv[1])
    except:
        if __name__ == '__main__':
            print("MUST OPEN MAIN.PY")

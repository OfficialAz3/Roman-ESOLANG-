try:
    from source.Roman import main
except:
    print("RUN ON MAIN.PY")
    quit()
import sys, os

allow_prefix = bool(open(sys.argv[0][:len(sys.argv[0])-12]+"DATA", "r").read())
prefix = sys.argv[0][:len(sys.argv[0])-12].split("/")
prefix = prefix[:len(prefix)-1]


if allow_prefix == True:
    switch = "ON"
else:
    switch = "OFF"

def modcmd(x):
    x = x.split(' ')
    echofold = echopref
    try:
        if x[0] == 'OPEN':
            main("".join(echofold) + x[1])
        elif x[0] == 'CD':
            prefix.append(x[1])
            echofolder = ""
            for folder in prefix:
                echofolder += folder + '/'
            if os.path.isdir(echofolder):
                pass
            else:
                print("FILE TERMINAL ERROR;\nNO DIRECTORY NAMED '{}' EXISTS.".format(echofolder))
                prefix.remove(prefix[len(prefix)-1])
        elif x[0] == 'BACK':
            prefix.remove(prefix[len(prefix)-1])
        else:
            return
    except:
        print("KEYWORD OUT OF RANGE")

if True:
    print("""
    WELCOME TO THE ROMAN1!
    AUTHOR BY OFFICIALAZ3
    VERSION IS 1.1.0
    
    TYPE "ECHO OFF" TO TURN OFF THE ECHO
    TYPE "ECHO ON"  TO TURN ON  THE ECHO
    DEFAULT IS {}
    
    TYPE "CD <FOLDERNAME>" TO OPEN A DIRECTORY
    TYPE "BACK" TO GO BACK
    
    TYPE "EXIT" TO EXIT
    
    TYPE "OPEN <SPACE> <ANY FILE>" TO COMPILE
    
    """.format(switch))
    echopref = ""
    for folder in prefix:
        echopref += folder + '/'
    while True:
        if allow_prefix == True:
            text = input('->{}'.format(echopref))
        else:
            text = input('->')
        print()
            
        if text == "ECHO OFF":
            filename = open(sys.argv[0][:len(sys.argv[0])-12]+"DATA", "w")
            allow_prefix = False
            filename.write("")
            filename.close()
        elif text == "ECHO ON":
            filename = open(sys.argv[0][:len(sys.argv[0])-12]+"DATA", "w")
            allow_prefix = True
            filename.write("HELLO")
            filename.close()
        elif text == "EXIT":
            break
        else:
            modcmd(text)
        print()

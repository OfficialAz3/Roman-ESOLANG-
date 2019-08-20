import sys

path = sys.argv[0][:len(sys.argv[0])-12]+"source/Terminal.py"
exec(open(path,'r').read())

import os
import sys

if len(sys.argv) < 2: 
    print("input commit's name plz")
    sys.exit(1)
elif len(sys.argv) == 2:
    os.system("git add .")
    os.system("git commit -m \""+sys.argv[1]+"\"")
    os.system("git push -u origin master")
    print("new commit name : \""+sys.argv[1]+"\"")
else : 
    print("error X(")
from os import getcwd
from sys import platform

operating_system=platform
dir=getcwd()

if operating_system=="linux" or operating_system=="Darwin":
    f1=open("code/dir.txt","w")
elif operating_system[0:3]=="win":
    f1=open("code\\dir.txt","w")
    f2=open("resources\\dir.txt","w")
    
f1.write(dir)
f1.close()
f2.write(dir)
f2.close()
print("Setup complete.")

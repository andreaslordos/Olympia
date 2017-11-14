from os import getcwd
dir=getcwd()
f=open("code\\dir.txt","w")
f.write(dir)
f.close()

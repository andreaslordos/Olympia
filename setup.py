from os import getcwd
dir=getcwd()
f=open("resources\\dir.txt","w")
f.write(dir)
f.close()

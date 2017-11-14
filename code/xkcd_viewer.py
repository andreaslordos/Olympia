def xkcd():
    from PIL import Image
    import xkcd
    from os import chdir
    dirFile=open("dir.txt","r")
    directory=dirFile.read()
    dirFile.close()
    comic=xkcd.getRandomComic()
    comic.download(output=directory+'\\resources',outputFile='xkcd.jpg',silent=False)
    chdir(directory+"\\resources")
    img=Image.open('xkcd.jpg')
    img.show()
    chdir(directory+"\\code")
    return img
    
    

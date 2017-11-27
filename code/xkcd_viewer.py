def xkcd():
    from changeDir import changeDirectory
    from PIL import Image
    import xkcd
    from os import chdir
    comic=xkcd.getRandomComic()
    changeDirectory("resources")
    comic.download(outputFile='xkcd.jpg',silent=False)
    img=Image.open('xkcd.jpg')
    img.show()
    changeDirectory("code")
    return img
    
    

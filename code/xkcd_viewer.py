def xkcd():
    from PIL import Image
    import xkcd
    import os
    os.chdir("C:\\Users\\user\\Desktop\\Smart Mirror Github")
    comic=xkcd.getRandomComic()
    comic.download(output='C:\\Users\\user\\Desktop\\Smart Mirror Github',outputFile='xkcd.jpg',silent=False)
    img=Image.open('xkcd.jpg')
    img.show()
    return img
    
    

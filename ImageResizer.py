from PIL import Image
def getScaledImage(image_path):
    imageob = Image.open(image_path).convert('RGB')
    width, height = imageob.size 
    scaledwidth=128
    scaledheight=128
    imageob = imageob.resize((scaledwidth,scaledheight), Image.ANTIALIAS)
    return imageob 
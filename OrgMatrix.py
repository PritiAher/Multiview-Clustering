import numpy as np
from PIL import Image

def getOrgImageMatrix(image_path):
    imageob = Image.open(image_path).convert('RGB')
    width, height = imageob.size
    size = width*height
    orgmat = np.array([0]*size).reshape(width,height) # 128 X 128
    pix=imageob.load() # normal matrix, Where each matrix element is an Array of RGB
    for i in range(width):
        for j in range(height):
            col=pix[i,j]
            matvalue=col[0]
            orgmat[i,j]=matvalue
           
       
    return orgmat

 


def getFusionImageMatrix(image_path):
    imageob = Image.open(image_path).convert('RGB')
    width, height = imageob.size
    size = width*height
    orgmat = np.array([0]*size).reshape(width,height)
    pix=imageob.load()
    for i in range(width):
        for j in range(height):
            col=pix[i,j]
            matvalue=col[0]
            orgmat[i,j]=matvalue
           
     
    AMat = np.random.randint(0,255,size=(len(orgmat[0]),len(orgmat)))  
    return AMat

 
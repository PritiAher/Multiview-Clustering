import numpy as np
from PIL import Image

def getNMFOriginalMatrix(image_path):
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
           
            
         
           
    return orgmat

      
imagepath="AXIAL CN 1.jpg"
orgmat=getNMFOriginalMatrix(imagepath)
rows=len(orgmat)
cols=len(orgmat[0])
for i in range(rows):
    for j in range(cols):
        val=orgmat[i,j]
        print(val, end = " ")
    print()    
        
def getAbsoluteGrayscaleImage(imageob):
    width, height = imageob.size 
    pix=imageob.load()
    for i in range(width):
        for j in range(height):
            col=pix[i,j]
            R=col[0]
            G=col[1]
            B=col[2]
            avg=(int)(R+G+B)/3
            absgray=int(avg)
            pix[i,j]=(absgray,absgray,absgray)
         
           
    return imageob

      
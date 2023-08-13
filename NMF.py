import numpy as np
import OrgMatrix 
from PIL import Image   

def formNMFParameterOptimzedImage(imagepath,optimagename,featureimgpath):
    
   # print("imagepath ",imagepath)
    #print("featureimgpath ",featureimgpath)
    
        
   # imagepath="sample.jpg"
    BMat=OrgMatrix.getOrgImageMatrix(imagepath)
 #   BMat = np.random.randint(1,10,size=(5,5))   
    # rows1=len(BMat)
    # cols1=len(BMat[0])
    # print("Orginal Image Matrix is \n")
    # for i in range(rows1):
    #     for j in range(cols1):
    #           val=BMat[i,j]
    #           print(val, end = " ")
    #     print()   
    # print("\n =====================================\n")
    
          
  #  AMat = OrgMatrix.getFusionImageMatrix(featureimgpath) 
   # AMat = np.random.randint(0,255,size=(cols1,rows1))  
    AMat=OrgMatrix.getFusionImageMatrix(featureimgpath) 
    # print("Feature Image Matrix is \n")
    # for i in range(rows1):
    #     for j in range(cols1):
    #           val=AMat[i,j]
    #           print(val, end = " ")
    #     print()    
           
    # print("\n =====================================\n")   
    
     
    C = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*BMat)] for X_row in AMat] # Bmat X Amat
    # print("Product Matrix is \n")
    # for r in C:
    #    print(r)
    # print("\n =====================================\n")    
       
    D= np.linalg.inv(AMat)
    # print("Inverse Matrix is \n")
    # print(D)
    # print("\n -----------------------------------------------\n")
    opt = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*C)] for X_row in D] # C X D
    
   # print("Optimized Matrix is \n")
    rows=len(opt)
    cols=len(opt[0])
   # print('Rows = ',rows)
  #  print('Cols = ',cols)
    
    mat = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            val=round(opt[i][j])
            mat[i][j]=val
          
            
           # print(mat[i][j], end = " ")
      #  print()
    
    imageob = Image.open(imagepath).convert('RGB')
    width, height = imageob.size
    size = width*height
    
    pix=imageob.load()
    for i in range(width):
        for j in range(height):
            col=pix[i,j]
            optvalue=mat[i][j]
            v1=optvalue
            v2=optvalue
            v3=optvalue
            pix[i,j]=(v1,v2,v3)
    imageob.save(optimagename)
    return 1
if __name__ == '__main__':
    formNMFParameterOptimzedImage()                  

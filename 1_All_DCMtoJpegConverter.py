import os
import pydicom as dicom
import cv2
import ImageResizer
import AbsoluteGrayScaler
 
inputhdatasetpath="RAW DATA"  
    
properdatasetpath="MULTIVIEW DATASET JPEG"
if not os.path.exists(properdatasetpath):
    os.makedirs(properdatasetpath)  
 
  
dir_list = os.listdir(inputhdatasetpath)
for dirname in dir_list:
    print('Directory name is ',dirname)
    newdirpath=properdatasetpath+"//"+dirname # MULTIVIEW DATASET/10_SAG LMC
    if not os.path.exists(newdirpath):
        os.makedirs(newdirpath)
    olddirpath=inputhdatasetpath+"//"+dirname #RAW DATA/10_SAG LMCI
    images_path = os.listdir(olddirpath) #list contains 1449
    imageno=1
    selecteddir=dirname #10_SAG LMCI
    st=selecteddir.split("_")
    filelabelname=st[1] #SAG LMCI
    print("filelabelname ",filelabelname)
    for n, image in enumerate(images_path):
        ds = dicom.dcmread(os.path.join(olddirpath, image))
        pixel_array_numpy = ds.pixel_array
        filename=str(imageno)
        imagename=filename+".jpg"
        newimagepath=newdirpath+"//"+filelabelname+" "+imagename #MULTIVIEW DATASET+ 10_SAG LMC/SAG LMCI + 1.jpg
        #print("newimagepath ",newimagepath)
        cv2.imwrite(newimagepath, pixel_array_numpy)
        imageob=ImageResizer.getScaledImage(newimagepath) # Rescaled
        imageob=AbsoluteGrayScaler.getAbsoluteGrayscaleImage(imageob)
        imageob.save(newimagepath)
        imageno=imageno+1
        print(newimagepath +" Image is Resized, Absolute Grayscaled and Stored")
        
    print(newdirpath+" all images are converted \n\n")
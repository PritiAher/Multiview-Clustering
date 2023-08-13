import os
import random
import cv2


numberofinputimages=50
inputhdatasetpath="TRAINING DATASET/TRAIN"  

inputimagefolder="INPUT IMAGES 50"
if not os.path.exists(inputimagefolder):
    os.makedirs(inputimagefolder) 
    
gendatapath=inputimagefolder+"//INPUT "+str(numberofinputimages)
if not os.path.exists(gendatapath):
    os.makedirs(gendatapath)  
 
dir_list = os.listdir(inputhdatasetpath) # List of 12 folders
num_dir = len(dir_list) #12
imagelist=[]
for i in range(numberofinputimages):
    while True:
        ran_dir=random.randint(0,(num_dir-1)) # 0 to 11-> 5
        dirname=dir_list[ran_dir] # 3_SAG EMCI
        findir=inputhdatasetpath+"//"+dirname # "TRAINING DATASET/TRAIN/3_SAG EMCI" 
        files_list = os.listdir(findir)
        num_files = len(files_list) # 1672
        ran_file=random.randint(0,(num_files-1)) # 1543
        filename=files_list[ran_file] # SAG EMCI 1543
        if filename not in imagelist:
            imagelist.append(filename)
            finalsrcpath=findir+"//"+filename
            finaldstpath=gendatapath+"//"+filename
            img=cv2.imread(finalsrcpath)
            cv2.imwrite(finaldstpath,img)
            break
            
            
    
        
        
       
   
print(numberofinputimages," Input images created")                       
                        
    
    
  
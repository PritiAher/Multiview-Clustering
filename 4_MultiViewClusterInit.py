import os
import random
import cv2
import NMF
import os
import TrainedWeightFusion
import Fuzzy
import collections
import matplotlib.pyplot as plt
import operator

inputdatapath="INPUT IMAGES//INPUT 50"

outputfolder="MULTI-VIEW CLUSTER RESULTS"
if not os.path.exists(outputfolder):
    os.makedirs(outputfolder)

dir_list = os.listdir(inputdatapath)
noi = len(dir_list)
rangefactor=int(noi/2)
print("Range Factor ",rangefactor)
# imahepathlist=[]
clusterlist=[]

for i in range(rangefactor):
    current_images = len(dir_list)
    print("Remaining_images : ",current_images)
    
    while True:
        ran_img1=random.randint(0,(current_images-1)) # 0 to 99 -> 49
        imagename1=dir_list[ran_img1]
        imgpath1=inputdatapath+"//"+imagename1
        
        ran_img2=random.randint(0,(current_images-1)) #0 to 99 -> 78
        imagename2=dir_list[ran_img2]
        imgpath2=inputdatapath+"//"+imagename2
        
        if imgpath1!=imgpath2:
         #   print(imgpath1)
           # print(imgpath2)
          #  dir_list.remove(imagename1)
          #  dir_list.remove(imagename2)
            optimage1="Optimized1.jpg"
            val1=NMF.formNMFParameterOptimzedImage(imgpath1, optimage1,imgpath2)
            optimage2="Optimized2.jpg"
            val2=NMF.formNMFParameterOptimzedImage(imgpath2, optimage2,imgpath1)
            if(val1==1 and val2==1):
                #print("done")
                index1=TrainedWeightFusion.getFusionScore(optimage1)
                index2=TrainedWeightFusion.getFusionScore(optimage2)
               # print(index1,index2)
                stageclustername1=Fuzzy.getStage(index1)
                clusterlist.append(stageclustername1)
                clusterfolder1=outputfolder+"//"+stageclustername1
                if not os.path.exists(clusterfolder1):
                    os.makedirs(clusterfolder1)
                finalpath1=clusterfolder1+"//"+imagename1
                img1=cv2.imread(imgpath1)
                cv2.imwrite(finalpath1,img1)
                
                
                stageclustername2=Fuzzy.getStage(index2)
                clusterlist.append(stageclustername2)
                clusterfolder2=outputfolder+"//"+stageclustername2
                if not os.path.exists(clusterfolder2):
                    os.makedirs(clusterfolder2)
                finalpath2=clusterfolder2+"//"+imagename2
                img2=cv2.imread(imgpath2)
                cv2.imwrite(finalpath2,img2)
                
                
                os.remove(optimage1)
                os.remove(optimage2)
                dir_list.remove(imagename1)
                dir_list.remove(imagename2)
                
               # print("Image Formed")
            
                
            break
            
    print("\n----------------------------------------\n")

frequency = collections.Counter(clusterlist)

stagefreq=dict(frequency)
sorted_d = sorted(stagefreq.items(), key=operator.itemgetter(1))
    
names = list(stagefreq.keys())
values = list(stagefreq.values())

plt.bar(range(len(stagefreq)), values, tick_label=names)
plt.show()
                  
                        
    
    
  
import os

strval=["CN","SMC","EMCI","MCI","LMCI","AD"]
inputdatapath="MULTI-VIEW CLUSTER RESULTS"

dir_list = os.listdir(inputdatapath)
num=0
for dirname in dir_list:
    print('Directory name is ',dirname)
    newdirpath=inputdatapath+"//"+dirname 
    sub_dir_list = os.listdir(newdirpath)
    numberofimages=len(sub_dir_list)
   # print("numberofimages ",numberofimages)
    orgvalue=strval[num]
   # print("orgvalue ",orgvalue)
    count=0
    
    for filename in sub_dir_list:
      #  print("File name ",filename)
        st=filename.split(" ")
        tempval=st[1]
        if(orgvalue==tempval):
            count=count+1
            
        
       # print(st[1])
    clusteraccuracy=  (count/ numberofimages) *100
    print("clusteraccuracy ",clusteraccuracy) 
    
    print(" \n ============================\n")  
    num=num+1
    
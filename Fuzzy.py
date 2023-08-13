def getCrispValues(size,n):
    indexlist=[]
    div=int(size/n)
    begin,end=0,0
    for i in range(n):
       
        rangelist=[]
        if(i==(n-1)):
            rangelist.append(begin)
            rangelist.append(size-1)
            indexlist.append(rangelist)
        else:
            rangelist.append(begin)
            end=begin+div-1
            rangelist.append(end)
            indexlist.append(rangelist)
            begin=end+1
            
             
         
    return indexlist           
            
        
        
def getStage(index):
            
    indexlist=getCrispValues(12,6)       
#    print(indexlist)
    pointer=1
    for row in indexlist:
        min=row[0]
        max=row[1]
        if(index>=min and index<=max):
            indexstr=str(pointer)
            stagecluster="STAGE "+indexstr
            break
        else:
            pointer=pointer+1
    return stagecluster       
        


 #val=12
 #for i in range (12):
     
        
#   clustername=getStage(i)
#   print(i,clustername)

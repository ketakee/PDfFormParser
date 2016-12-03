      
def formParse(fileobj,parameters,listoflength):
    if listoflength==None:
        listoflength=len(parameters)*[1,]


    with open(fileobj) as f:
        a=f.readlines()

    for i in range(len(parameters)):
        param=parameters[i]        
        for j in range(len(a)):
             b=(a[j].find(param))
             if (b!=-1):
                s=a[j]
                c=listoflength[i]-1
                print(s[:b+len(param)],":",s[b+len(param):])
                j+=2
                while(c!=0):
                    print(a[j])
                    j+=2
                    c-=1

                    
formParse('C:\\Users\\Ketakee Nimavat\\Documents\\form.txt',["NAME","ROLL NO",],[2,1])
        








# l+=[a.find(i),]  
        
#   l+=[len(a)-1]
#  print(l)
    
#    for i in range(len(l)-1):
#       s=a[l[i]:l[i+1]]
#        print(s)
        

n=input()
count1=0
count2=0
for i in n:
    if(i=='a'):
        count1+=1
    if(i=='b'):
        count2+=1
    
if(count1%2==0 and i=='b'):
    print("Accepted")
else:
     print("not accepted")
    
        
    

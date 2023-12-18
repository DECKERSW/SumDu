f1=0
f2=1
size=8
print (f1,f2,end=' ')
sum =f1+f2
for i in range (2,size):
    f1,f2=f2,f1+f2
    sum+=f2
    print(f2,end=' ')
    
print('\n',sum)
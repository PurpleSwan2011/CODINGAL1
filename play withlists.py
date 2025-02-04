L=[4,5,1,2,9,7,10,8]
print("original list:",L)
count=0
for i in L:
    count+=i
avg=count/len(L)
print("sum=",count)
print("average=",avg)
L.sort()
print("smallest element:",L[0])
print("biggest element:",L[-1])
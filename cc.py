test_dict={'codingal':2,'is':2,'best':2,'for':2,'coding':1}
print("original dict:"+ str(test_dict))
K=int(input("enter the value of k:"))
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1
print("frequency of K :"+str(res))
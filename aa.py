import array as  arr
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("original:"+str(array_num))
print("array"+str(array_num.count(3)))
array_num.reverse()
print("reverse")
print(str(array_num))
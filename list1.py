num=int(input("enter"))
odd_list=[i for i in range(num) if i%2!=0]
print("list of odd nos:",odd_list,"/n")
even_list=[i for i in range(num) if i%2==0]
print("list of even nos:",even_list,"/n")
fruits=['apple','banana','mango','papaya','grapes']
Fruits=[x[0].upper()+x[1:] for x in fruits]
print(("fruits",Fruits))
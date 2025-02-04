def SquaredValues(beg,end):
    lst=[]
    for i in range(beg,end):
        lst.append(i**2)
    lst_even=[]
    lst_odd=[]
    for i in lst:
        if i%2==0:
            lst_even.append(i)
        else:
            lst_odd.append(i)
    print("even",lst_even)
    print("odd",lst_odd)
beg=int(input("enter the starting range:"))
end=int(input("enter the ending range:"))
SquaredValues(beg,end)

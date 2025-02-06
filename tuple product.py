def multiple_tuple(nums):
    temp=list(nums)
    product=1
    for x in temp:
        product*=x
    return product
nums=(4,3,2,2,-1,18)
print("original tuple:")
print(nums)
print("product-multiplying all numbersof said tuple",multiple_tuple(nums))
nums=(2,4,8,8,3,2,9)
print("\n original tuple:")
print(nums)
print("product-multiplying all numbersof said tuple",multiple_tuple(nums))
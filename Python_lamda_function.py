# Noraml define function
# def add_five(num):
#     result=num+5
#     return result
# x=7
# print(add_five(x))
# How to use lamda function
# lambda_add_five=lambda x :x + 5

# y=10
# print(lambda_add_five(y))

# # lambda for two num
# lambda_two_numbersum=lambda x,y: x+y
# a=30
# b=10
# print(lambda_two_numbersum(a,b))

# using lambda function for two number


# lambda_large_number=lambda x,y :x if x>y else y
# num1=20
# num2=10
# print(lambda_large_number(num1,num2))
# how to work with map(),filter(),reduce()

#implement map function
list1=[1,2,3,4,5,6,7]

squre_num=lambda x:x*x
square_list=dict(map(squre_num,list1))
print(square_list)



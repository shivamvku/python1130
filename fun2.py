# # global and local



# # global 
# a = 4
# def f1():
# 	a =3
# 	print(a)
# def f2():
# 	global a
# 	a = 5
# 	print(a)
# def f3():
# 	a =7
# 	print(a)
# def f4():
# 	a =10
# 	print(a)
# f2()
# print(a)
# f1()
# f2()
# f3()
# f4()
# print(a)



# def fact(a):
# 	if a == 1:
# 		return 1
# 	else:
# 		return(a*fact(a-1))
# while True:
# 	a = int(input('enter a number fro faacctorial\n'))
# 	print('the factorial of the number',a,'is',fact(a))
	




# Lambda function

# Anonymous function


# syntax

# var = lambda arg:expression
# function call
# var()

# a = lambda a:a**2
# print(a(45))



# map()----------------->
# filter()

l = [a for a in range(0,50)]
# # print(l) 
# l2 = list(map(lambda a:a%2 == 0,l))
# print(l2)


# l3 = list(filter(lambda a:a%2!=0,l))
# print(l3)

# # reduce()

# import functools
# from functools import reduce


# l4= reduce(lambda x, y: x+y, l)
# print(l4)

# # map()
# # filter()
# # reduce()


# # def add(a,b):
# # 	''' this  is an add function'''
# # 	print(a+b)

# # def main():
# # 	'''This is a main function'''
# # 	print('i am from main function')
# # 	add(4,5)

# # print(__name__)
# # if __name__ == '__main__':
# # 	main()
# # 	print(main.__doc__)
# # 	print(add.__doc__)
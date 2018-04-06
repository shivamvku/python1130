# def add(a,b=3):
# 	print(a+b)

# add(3)


# Default arg

# def avengers(batman,ironman):
# 	print('the address of batman is ',batman)
# 	print('the address of ironmann is ',ironman)

# 	print(type(batman))
# 	print(id(batman))

# avengers(batman = 'usa',ironman = 'pakistan')

# pass by reference

# Arbitary argumnets

# def avengers(*names):
# 	print(names)
# 	print(type(names))
# 	for name in names:
# 		print('hello',name,'welcome to python class')

# 	# for name,address in :
# 	# 	print('The',name,'of this avenger is',address)
# 	# print('the address of batman is ',batman)
# 	# print('the address of ironmann is ',ironman)

# 	# print(type(batman))
# 	# print(id(batman))

# avengers('venkat','yami','deepika','vijaya',1,45.676,56+34j,[a**2 for a in range(0,5)])




def avengers(**greeting):
	# print('the address of batman is ',batman)
	# print('the address of ironmann is ',ironman)

	print(type(greeting))
	print(id(greeting))

	for name,address in greeting.items():
		print('This is ',name,'from',address,'welcome to python program')

avengers(batman = 'usa',ironman = 'pakistan')

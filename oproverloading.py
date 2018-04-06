

# class somthing:
# 	def __init__(self,a,b):
# 		self.a = a
# 		self.b = b

# 	def __repr__(self):
# 		return 'this is a:%s ,b:%s'%(self.a,self.b)

# 	def __str__(self):

# 		return 'this is from str method a:%s and b:%s'%(self.a,self.b)


# valu = somthing(34,45)

# print(valu)

# print([valu])




class PhoneBook:

	def __init__(self ,name ,pages ):
		self.name = name
		self.pages = pages

	def __add__(self,other):

		sumofpages = self.pages+other.pages
		list_of_names = self.name+other.name

		return(sumofpages,list_of_names)
	
	# def __radd__(self,other):
	# 	if other == 0:
	# 		return self
	# 	else:
	# 		return self.__add__(other)

	def __str__(self):
		return 'The list of names is %s and the sum of pages is %d'%(self.name,self.pages)
diray1 = PhoneBook('uppla',400)
diray2 = PhoneBook('Madhapur',4000)

sum = diray1+diray2
# print(diray1)
# print(diray2)
# sum([diray1,diray2])
# print(diray1+diray2)
print(sum)

sun2 = sum(diray1,diray2)
print(sun2)







https://docs.python.org/3/reference/datamodel.html
class Asset(object):
	"""docstring for Asset"""
	a = 90
	b =70
	def __init__(self,name,price,quntity):
		self.name = name
		self.price = price
		self.quntity = quntity

	def details(self):
		print('There are',self.name,'of',self.price,'and in this much',self.quntity,'quntity')

	def addasset(self,inc):
		self.quntity += inc


	def removeasset(self,dec):
		self.quntity -= dec


c1 = Asset('chair',800,45)

# # c2 = Asset('Tables',7000,30)

# c1.details()
# c1.addasset(20)
# c1.details()
# c1.removeasset(65)
# c1.details()

# print(Asset.__dict__)
print(c1.__dict__)

# c2.details()


# print(Asset.a)
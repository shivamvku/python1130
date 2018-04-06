# class Animanl():
# 	def eat(self):
# 		print('aninmal is eating')

# 	def sleep(self):
# 		print('animal is slpeeing')

# class loin(Animanl):
# 	def hunt(self):
# 		print(' loin is hunting')

# class tiger(Animanl):
# 	def running(self):
# 		print('tiger is running')

# task1 = loin()
# task1.eat()


# # multilelvel inhertance

# class Game():
# 	def training(self):
# 		print('sport persons are getting trained')

# 	def scheduling(self):
# 		print('Couch is sechdig the play')

# 	def score(self):
# 		print('the score of the team')

# 	def win(self):
# 		print('The team has won')

# 	def loose(self):
# 		print('the team has lost')



# class batminton(Game):
# 	def Players(self):
# 		print(' This is a list of Players')
# 	def rules(self):
# 		print('This are the rules of batminton')



# class cricket(batminton):
# 	def sponcers(self):
# 		print('these are  the sponcers')
# 	def rules(slef):
# 		print('This are the rules of cricket')
		
# season1 = cricket()
# season1.scheduling()

# batseason1  = batminton()
# crksea1 = cricket()
# crksea1.rules()
# batseason1.rules()

# crksea1.Players()



# class student:
# 	name = ''
# 	roll = 0

# 	def __init__(self,name,roll):
# 		self.name = name
# 		self.roll  = roll

# 	def display(self):
# 		print(self.name)

# 	def showroll(self):
# 		print(self.roll)

# class girl(student):
# 	# Id = ''
# 	def __init__(self,name,roll):
# 		student.__init__(self,name,roll)
# 		self.name = name

# 	def displayid(self):
# 		return self.id


# class boy(student,girl):
# 	def __init__(name,age,roll):
# 		student.__init__(self,name,roll)
# 		girl.__init__(self,id)

# student1 = student('ravi',456)
# student1.showroll()


# girl1 = girl('harsh',45)

# girl1.display()


# boy1 = boy('rahul',23,456765)
# boy1.display()


# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg
		


# class animal():
# 	def __init__(self,name):
# 		print(name,'is an dangeros animal')

# class loin(animal):
# 	def __init__(self):
# 		print('Loin is roaring')
# 		super(animal).__init__('The loin')


# l1 = loin()

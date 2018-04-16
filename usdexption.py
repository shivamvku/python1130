# try:
# 	pass
# except Exception as e:
# 	raise
# else:
# 	pass
# finally:
# 	pass


class Error(Exception):
	'''This is the the base class excption'''
	pass

class UnderageError(Error):
	'''This is raised when the input age is less than the detemned age'''
	pass
class OverageError(Error):
	'''This cass is clalled wen the age of the person is over than the determined age'''
	pass

class NotYetBornError(Error):
	'''This class is cllled when the person enter 0'''

	pass

age = 23

while True:
	try:
		inputage = int(input('Enter the ageg of the person\n'))

		if inputage <= 0:
			raise NotYetBornError
		elif inputage < age:
			raise UnderageError
		elif inputage > age:
			raise OverageError

		break


	except NotYetBornError:
		print('The person is not yet boarn\n')
		print('Try Againg......!\n')


	except UnderageError:
		print('The person age  more than what you think\n')
		print('Try Againg.......!\n')



	except OverageError:
		print('The person age is less than waht you think\n')
		print('Try Againg.......!\n')

	finally:
		print('you have entered some age.....!')

print('You have guessed the age correctly.............!!!!!!\n')




# import threading

# def suqure(nub):
# 	print('The squre of the number is ',nub**2)

# def cube():
# 	print('the cube of the number is ',num**3)

# if __name__ == '__main__':
# 	thrad1 = threading.Thread(target = suqure,args=(2,))
# 	thrad2 = threading.Thread(target = suqure,args=(5,))

# 	thrad1.start()
# 	thrad2.start()

# 	thrad1.join()
# 	thrad2.join()


# 	print('The thrdading have been complted')



import threading
import os


def suqure(nub):
	print('the sure has a thread id of ',threading.current_thread().name)
	print('The process id for the squre thrad is:',os.getpid())
	print('The squre of the number is ',nub**2)

def cube():
	print('the cube has a thread id of ',threading.current_thread().name)
	print('The process id for the cube thrad is:',os.getpid())
	print('the cube of the number is ',num**3)


if __name__ == '__main__':
	print('the Nme of the main  thread is',threading.current_thread().name)
	print('The process id for the main  thread is:',os.getpid())
	thrad1 = threading.Thread(target = suqure,args=(2,))
	thrad2 = threading.Thread(target = suqure,args=(5,))

	thrad1.start()
	thrad2.start()

	thrad1.join()
	thrad2.join()


	print('The thrdading have been complted')




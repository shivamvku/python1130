# # *
# # **
# # ***
# # ****
# # *****
# # for i in range(1, 6):
# 	# print("*"*i)
# # print("*"*2)
# # print("*"*3)
# # print("*"*4)
# # print("*"*5)
# # 1
# # 12
# # 123
# # 1234

# # for i in range(1,6):
# # 	print(i )
# # print("--------")
# for j in range(1 , 6 ):
# 	for i in range(1,j):
# 		print(i )
# 1
# 22
# 333
# 4444
# 55555

# nums -- factors 
num = 12
count = 1
for i in range(1 , num+1 ):
	
	if(num % i == 0 ):
		print(i)
		count = count +1
if(count > 2):
	print("composite")			
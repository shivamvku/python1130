import csv
def readfile(fileobj):
# 	# reader = csv.reader(fileobj)
	reader = csv.DictReader(file,delimiter = ',')
# 	# writer = csv.writer(file,delimiter = ',')

# 	# for a in reader:
# 	# 	print('\n'.join(a))
# 	# 	print()
# 	# S.No,Name ,Contact ,Email ID,Score,Percentage (%),Year,Branch
# 	for a in reader:
# 		listofid = a['S.No']
# 		print()
# 		print([a for a in listofid])
	for line in reader:
		print(line['S.No'])
		print(line['Name'])
		print(line['Contact'])
		print(line['Email ID'])
		print(line['Score'])
		print(line['Percentage(%)'])
		print(line['Year'])
		print(line['Branch'])
		print('\n')
		print('-------------------------------------------------------')


	# for line in ddata:
	# 	writer.writerow(line)

if __name__ == '__main__':
	# output = 'out.csv'
	file = open('testresult.csv','r')

	readfile(file)


	# ddata = ['first_name,last_name,address,city,state,zip_code'.split(','),
	# 	'batman,supermna,usa,somthing,somstae,5006'.split(',')
	# 	]
	# readfile(ddata,output)


# import matplotlib.pyplot as plt
# import csv

# x = []
# y = []

# with open('testresult.csv','r') as csvfile:
#     plots =  csv.DictReader(csvfile,delimiter = ',')
#     for row in plots:
#         x.append(row['Percentage(%)'])
#         y.append(row['Name'])

# plt.plot(x,y, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()
a = {}

print(type(a))


# st1 = {1,2,8,9,4,5,6,7,8,9,5,3,5,7,3,4}
# print(st1)

# # print(st1[0])


# # st1.pop()
# # st1.pop()

# # print(st1)

# st1.add(34)

# print(st1)


# st1.update({1,2,3,4,5,65,67,90,45,23})
# print(st1)


# a = {2,3,4,5}
# b = {2,56,89,90,5,4,3,4}

# # print(st1+st2)
# # print(2*st1)


# # union

# print(a.union(b))
# print(a | b)

# print(a.intersection(b))
# print(a & b )

# print(a-b)
# print(b-a)


# print(a.issubset(b))
# print(a.issuperset(b))







# Frozen set

a = {a**2 for a in range(0,11)}
print(a)


b = frozenset(a)
print(b)

# b.add(45)
# print(b)

b.update({34,56,4})
print(b)
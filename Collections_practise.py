# list is a collection
# tuple is a collection
# dictionary is a collection
# set is a collection

person0_name = 'Voctoria'
person1_name = 'Aisha'
person2_name = 'Anum'
Person3_name = 'Deanne'

# tuple
names_tuples = ('victoria', 'Aisha', 'Anum', 'Deanne')
# class/type is tuple
names_tuples_type = type(names_tuples)
print(names_tuples_type)

print(names_tuples)
print(names_tuples[0])

# tuples are immutable
# names_tuple[0] = 'Dominique'
# print(names_tuples[0])

# list
# lists are mutable
names_list = ['Victoria', 'Aisha', 'Anum', ' Deanne']
names_list_type = type(names_list)
print(names_list_type)
print(names_list)

# tuples and lists are sequences
# they remember the order

names_list[0] = 'Dominique'
print(names_list)

print(names_list[-1])
print(names_list[-2])
print(names_list[-3])
print(names_list[-4])

print(names_list)
names_list
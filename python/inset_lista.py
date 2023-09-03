print("lista original")
numbers = [2342, 34, 64, 23, 5604]
print(len(numbers))
print(numbers)

print("append")
numbers.append(634)
print(len(numbers))
print(numbers)

print("insert")
numbers.insert(3, 1111)
print(len(numbers))
print(numbers)


my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


my_list = []  # Creando una lista vacía.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)

# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

# creation of tuple with my first name, last name and age
tup1 = ('Jidesh', 'Baidya', 25)
# created list
my_list = []
# append tuple to list
my_list.append(tup1)
print(my_list)
# creating few more tuple with similar type of record
tup2 = ('Jhon', 'Doe', 33)
tup3 = ('Darshana', 'Baidya', 16)
tup4 = ('Manish', 'Twayana', 26)
# appending the tuple to the list
my_list.append(tup2)
my_list.append(tup3)
my_list.append(tup4)
print("list with the appened tuple is")
print(my_list)
print("this is my sorted list it is sorted acccrding to fist name of tuple")
print(sorted(my_list))
print("now let me try sorting with last name")
print(sorted(my_list, key=lambda x: x[1]))
print()
print("Yes I learned about sorting now I can  by any field in the tuple, first name, last name or age.")
print("enter first if you want sort by first name")
print("enter last if you want sort by last name")
print("enter age if you want sort by age")
i = input("enter first or last or age to sort accordingly")
if i == "first":
    print("sorted list according to first name is")
    print(sorted(my_list, key=lambda x: x[0]))
if i == "last":
    print("sorted list according to first name is")
    print(sorted(my_list, key=lambda x: x[1]))
if i == "age":
    print("sorted list according to first name is")
    print(sorted(my_list, key=lambda x: x[2]))

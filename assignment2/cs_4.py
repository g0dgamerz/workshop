# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

# creating of list as my_list
my_list = []
# appending names to my_list
my_list.append('jhon')
one = id(my_list)
my_list.append('doe')
two = id(my_list)
my_list.append('aarnav')
three = id(my_list)

if (one == two == three):
    print('id of the list has not changed its normal')
else:
    print('id of the list has changed it annoying')

print('fist item on the list is %s' % my_list[0])
print('second item on the list is %s' % my_list[1])

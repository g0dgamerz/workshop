# Write a Python program to remove an item from a tuple.
# create a tuple
tuplex = "i", "n", ':)', "s", "i", "g", "h", "t"
print(tuplex)
# tuples are immutable, so you can not remove elements
# using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)

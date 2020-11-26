# ​ Write a Python program to get a string made of the first 2 and the last 2 chars 
# from a given a string.
#  If the string length is less than 2, return instead of theempty string.

def string_both_ends(str):
  if len(str) < 2:
    return 'Empty String'

  return str[0:2] + str[-2:]

print(string_both_ends('Python'))
print(string_both_ends('Pyon'))
print(string_both_ends('Py'))
print(string_both_ends('w'))
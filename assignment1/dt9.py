# Write a Python program to change a given string to a new
#  string where the firstand last chars have been exchanged.

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('abcd'))
# Write a Python program to count the number of characters (characterfrequency) in a string. 
# Sample String : google.com

def no_of_each_char(str):
    dict={}
    for n in str:
        keys=dict.keys()
        print(keys)
        if n in keys:
            dict[n] +=1
        else:
            dict[n] =1
    return dict
print(no_of_each_char("google.com"))
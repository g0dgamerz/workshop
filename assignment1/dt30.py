# Write a Python script to check whether a given key already exists in adictionary.
d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}


def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


is_key_present(2)
is_key_present(7)

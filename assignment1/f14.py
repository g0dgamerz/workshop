# Write a Python program to sort a list of dictionaries using Lambda
models = [{'name': 'Jidesh Baidya', 'designation': 'Software Engineer'}, {'name': 'Swarnim Shrestha',
                                                                          'designation': 'Web designer'}, {'name': 'Manisha shrestha', 'designation': 'Graphic Design'}]
print("Original list of dictionaries")
print(models)
sorted_models = sorted(models, key=lambda x: x['name'])
print('\n Sorting the list of dictionary')
print(sorted_models)

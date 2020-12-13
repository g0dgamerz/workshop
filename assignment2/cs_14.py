"""Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]"""

import csv

def reading_csv(filename):
    with open(filename, 'r') as store:
        csv_reader = csv.DictReader(store)

        for line in csv_reader:
            print(line)


filename = 'file.csv'
reading_csv(filename)
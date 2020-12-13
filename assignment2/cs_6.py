# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.


my_list = ['Motu', 'Patlu', 'Gasitaram', 'Dr. Jhakta', 'John']
for i in my_list:
    if i == 'John':
        print("John is busted")
        break
    else:
        print("John banega don john ko pakerne muskil hi nahi namunkin heee")
        print("keep searching...")
else:
    print('Not found')

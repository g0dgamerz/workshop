# Create a list of tuples of first name, last name, and age for your friends
# and colleagues. If you don't know the age, put in None. Calculate the
# average age, skipping over any None values. Print out each name,
# followed by old or young if they are above or below the average age.
lot = [('Jidesh', 'Baidya', 25), ('John', 'Doe', 24),
       ('Manisha', 'Shrestha', None), ('Aarnav', 'Bhattrai', 23)]

size = len(lot)
index = size-1

# print(isinstance((lot[2][2]), int))
total = 0
c = 0
for i in range(size):
    if isinstance(lot[i][2], int):
        c += 1
        total = total+lot[i][2]
# calculation of average age
avg = total/c
print("average age is {}".format(avg))

# Print out each name by old or young if they are above or below the avg age.
for i in lot:
    if isinstance(i[2], int):
        if i[2] > avg:
            print(i[0], "is older than average age")
        else:
            print(i[0], "is younger than average age")

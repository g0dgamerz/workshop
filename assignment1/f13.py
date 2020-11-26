# ​ Write a Python program to sort a list of tuples using Lambda.
subject_marks = [('a', 1), ('b', 2),
                 ('c', 3), ('d', 4)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)

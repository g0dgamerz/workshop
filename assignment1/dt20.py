# .​ Write a Python program to count the number of strings where the
# stringlength is 2 or more and the first and
#  last character are same from a given list ofstrings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def match_words(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr


print(match_words(['abc', 'xyz', 'aba', '1221']))

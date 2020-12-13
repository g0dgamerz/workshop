# Function to group anagrams together from given
# list of words
def groupAnagrams(words):

    # sort each word in the list and store in list as A[]
    A = [''.join(sorted(word)) for word in words]
    print(A)

    # construct a dictionary where key is each sorted word
    # and value is list of indices where it is present
    dict = {}
    for i, e in enumerate(A):
        dict.setdefault(e, []).append(i)
    print(dict)

    # go through dictionary and read indices for each sorted key.
    # The anagrams are present in actual list at those indices
    for index in dict.values():
        print("these are anagrams", [words[i] for i in index])


paragraph = 'ogd cat dog tac atc'


def convert(paragraph):
    return ''.join(paragraph).split()


words = convert(paragraph)
groupAnagrams(words)

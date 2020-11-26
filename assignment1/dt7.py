# ​Write a Python function that takes a list of words 
# and returns the length of the longest one

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
        
    word_len.sort()
    print(word_len)
    return word_len[-1][0]

print(find_longest_word(["short", "long", "longest"]))
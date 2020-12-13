# Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?
checktext = 'gta.exe'
countdot = checktext.count('.')
b = checktext.find('.')
l = list(checktext)
# finding extensions
if countdot == 1:
    s = l[b+1:]
    print('Extension:')
    print(''.join(s))

if countdot == 2:
    c = checktext.find('.', b+1)
    l = list(checktext)
    s = l[b+1:c]
    t = l[c+1:]
    print('Extension:')
    print(''.join(s))
    print(''.join(t))


# finding filename
splitlist = l[0:b]
listjoin = ''.join(splitlist)
print('Filename', listjoin)

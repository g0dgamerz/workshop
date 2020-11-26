
str1='abc'
str2='xyz'
f2o1=str1[0:2]
f2o2=str2[0:2]
print(str1.replace(str1[0:2],f2o2))
print(str2.replace(str2[0:2],f2o1))

#alt
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))
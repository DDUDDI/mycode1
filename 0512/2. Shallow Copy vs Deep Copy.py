# Shallow Copy vs Deep Copy

# Shallow Copy
list_a = ['a', 'b', 'c']
list_b = list_a

print('list_a:', list_a)
print('list_b:', list_b)

list_a[1] = 'f'
print('list_b:', list_b)

'''list_b도 list_a의 주소를 참조하고 있으므로
    list_a[1]의 값을 바꾸면 list_b[1]의 값도 같이 변경됨'''

# Deep Copy
list_c = ['d', 'e', 'f']
list_d = list_c[:]

print('\nlist_c:', list_c)
print('list_d:', list_d)

list_c[1] = 'g'
print('list_d:', list_d)
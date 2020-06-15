t1 = (1, 2, 3)
# t1[1] = 100

# t1->list2 복사
list2 = list(t1) # list(): tuple->list
list2[1] = 100

print(t1)
print(list2)
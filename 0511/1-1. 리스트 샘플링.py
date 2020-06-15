import random

numlist = []
newlist = []

for i in range(0, 100) :
    numlist.append(random.randint(0, 100))
print(sorted(numlist))

# for문을 이용해서 중복 제거하기
for j in numlist :
    if j not in newlist :
        newlist.append(j)
        if len(newlist) == 50 :
            print(sorted(newlist))

# numset = set(numlist) # Set은 중복을 허용하지 않음
# print(numset)


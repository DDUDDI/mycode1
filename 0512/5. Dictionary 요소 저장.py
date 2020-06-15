# 5. Dictionary를 사용하여 키보드에서 이름과 전화번호를 입력하여 저장해보세요.
# 5인의 정보를 위와 같은 방법으로 저장하려고 한다.

# 내 방법: 별개의 변수로 저장받은 후, Dic에 key, value로 저장
Dic = {}
for i in range(5) :
    name, phone = input(f'{i+1}번째 이름, 번호 : ').split(', ')
    Dic[name] = phone
print(Dic)
# 변수1, 변수2 = input().split()


# 선생님 방법: 한번에 리스트로 저장받은 후, index를 사용해 저장
'''
members = {}
for i in range(5) :
    info = input(f'{i+1}번째 이름, 번호 : ')
    inList = info.split()
    members[inList[0]] = inList[1]
print(members)
'''


'''
for key in Dic : # key 출력
    print(key)
for val in Dic.values() :
    print(val) # dic.values(): value 출력
for key, val in Dic.items() : # dic.items(): key, value 출력
    print("key = {key}, value={value}".format(key=key, value=val))
'''
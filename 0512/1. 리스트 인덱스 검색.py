# 1. 100~200까지 순서대로 저장된 리스트를 생성한다
# 키보드에서 검색할 번호를 입력하면
# 해당 숫자가 리스트의 몇번째에 위치하는지 확인하여 그 인덱스를 화면에 출력한다
# 검색하려는 숫자가 리스트의 전반부에 있는지 후반부에 있는지 먼저 확인하여
# 해당 부분을 슬라이싱 적용하여 그 부분에서만 검색하도록 한다

numList = []
# 100~200 리스트 생성
for i in range(100, 201) :
    numList.append(i)
# print(f'원본 리스트 :\n{numList}\n')
# numList = list(range(100, 201)


# 숫자 입력
snum = input('검색할 번호를 입력하세요(100-200) : ')
inum = int(snum) # num은 string이므로 정수로 변환 필요

# 숫자 index 확인
for i in numList :
    if i == inum :
        idx = numList.index(i)
        print(f'\n원본 리스트에서 {inum}의 index는 {idx}입니다.')

# 전반부, 후반부 확인 후, 슬라이싱
front = []
end = []
mid = int(len(numList)/2)
if idx <= mid : # 100~150
    front = numList[:mid+1]
    idx2 = front.index(inum)
    print(f'\n전반부 리스트에서 {inum}의 index는 {idx2}입니다.')
else : # 151~200
    end = numList[mid+1:]
    idx2 = end.index(inum)
    print(f'\n후반부 리스트에서 {inum}의 index는 {idx2}입니다.')

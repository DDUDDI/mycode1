# 1. 100~200까지 순서대로 저장된 리스트를 생성한다
# 키보드에서 검색할 번호를 입력하면
# 해당 숫자가 리스트의 몇번째에 위치하는지 확인하여 그 인덱스를 화면에 출력한다
# 검색하려는 숫자가 리스트의 전반부에 있는지 후반부에 있는지 먼저 확인하여
# 해당 부분을 슬라이싱 적용하여 그 부분에서만 검색하도록 한다

'''코드 고치는 중'''
import random as rd

numList = []
a = rd.randint(0, 10)
b = rd.randint(11, 20)

# 리스트 생성
numList = list(range(a, b+1))

# 숫자 입력
snum = input(f'검색할 번호를 입력하세요({a}-{b}) : ')
inum = int(snum) # num은 string이므로 정수로 변환 필요

# 리스트 슬라이싱
mid = int(len(numList)/2+1)
front = numList[:mid]
end = numList[mid:]


# 숫자 index 출력
if inum in front :
    idx = front.index(inum)
    print('전반부', inum)
elif inum in end :
    idx = end.index(inum)
    idx2 = numList.index(inum)

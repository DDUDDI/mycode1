# 4. 성적 출력 프로그램
# [{'홍길동':[70, 60, 80,...]}]

a = []

name = input('이름 : ')
score = input(f'[{name}]의 4과목 성적 : ')
scoList = score.split()

# 정수 변환
for i in range(len(scoList)):
    scoList[i] = int(scoList[i])

members = {name:scoList}
a.append(members)

print(a)

# 3. 성적 관리 프로그램
# 을 작성하고자 한다.
# 한 학생의 점수는 4과목으로 구성된다(Bigdata, Python, Flask, DB).
# 한 반의 전체 학생수는 5명이다.
# 학생 리스트를 참고하여 다음과 같이 키보드에서 입력할 수 있다.
# 학생명 입력, 학생명의 점수 입력(4과목 공백으로 구분)

# 데이터 구조: [{홍길동:{과목명:점수}]

scoreList = []
subject = ['Bigdata', 'Python', 'Flask', 'DB']
while True:
    func = input(f'\t성적 입력(a) or 확인(s) or 검색(f) or 수정(u) or 삭제(d) or 종료(x) : ')

####### 성적 입력 #######
    if func == 'a':
        name = input(f'\t학생명 : ')
        record = input(f'\t{name}의 4과목 점수 입력(공백으로 구분) : ')
        recordList = record.split() # 4과목의 점수를 list에 저장
        dic1 = {}
        for i in range(4): # 과목 갯수 4개
            dic1[subject[i]] = recordList[i] # {과목명:점수}
        dic2 = {name:dic1} # {이름:{과목명:점수}}
        scoreList.append(dic2) # [{이름:{과목명:점수}}]

####### 성적 확인 #######
    elif func == 's':
        print('\t***********************성적 확인***********************')
        # 열 이름 출력 (이름 점수 평균)
        print('\t이 름', end='\t')
        for i in range(4):
            print(f'{subject[i]}', end='\t')
        print('\t평 균')
        # 열 값 출력
        for a in scoreList:
            for b, c in a.items(): # b: 이름, c: {과목명:점수}
                print(f'\t{b}', end='\t')
                total = 0
                for d in subject: # d: 과목명
                    total += int(c[d])
                    print(f'{c[d]}', end='\t\t') # dic1[s]: 과목명에 해당하는 점수
                avg = total/len(subject)
                print(avg)

####### 성적 검색 #######
    elif func == 'f':
        name = input('\t학생명 : ')
        print('\t***********************검색 결과***********************')
        print(f'\t이름 : {name}')
        for a in scoreList:
            for b, c in a.items(): # b: 이름, c: {과목명:점수}
                if b == name:
                    for d in c.keys(): # d: 과목명
########## 프린트 예쁘게 수정하기 ##############
                        print(f'\t{d} : {c[d]}')

####### 성적 수정 #######
# 반복문 탈출을 위해 boolean 값 사용
    elif func == 'u':
        info = input('\t수정할 학생명 과목명 새점수 : ')
        newInfo = info.split()
        completed = False # 작업 종료 확인 위해서 사용
        for a in scoreList:
            for key, value in a.items(): # key: name, value: {과목명:점수}
                if key == newInfo[0]: # key 값이 입력한 학생명과 같다면
                    value[newInfo[1]] = int(newInfo[2]) # 수정할 과목명의 점수를 수정해라
                    completed = True # 작업 종료
                    print('\t수정 성공')
                    break # 하위 for문 탈출
                if completed:
                    break # 상위 for문 탈출

####### 성적 삭제 #######
    ############### for 문 내에서 삭제하면 오류생김 수정 필요
    elif func == 'd':
        name = input('\t학생명 : ')
        for a in scoreList:
            for b, c in a.items():
                if b == name:
                    msg = input('\t정말 삭제하시겠습니까?(Yes/No) : ')
                    if msg == 'Yes':
                        del a[b]
                        print(f'\t{name}의 정보가 삭제되었습니다.')
                else:
                    print(f'\t일치하는 정보가 없습니다.')
                    continue

####### 프로그램 종료 #######
    elif func == 'x':
        print('\t프로그램을 종료합니다.')
        break
    else:
        print('\t입력 오류')




































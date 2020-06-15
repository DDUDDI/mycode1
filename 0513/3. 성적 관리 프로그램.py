# 3. 성적 관리 프로그램을 작성하고자 한다.
# 한 학생의 점수는 4과목으로 구성된다(Bigdata, Python, Flask, DB).
# 한 반의 전체 학생수는 5명이다.
# 학생 리스트를 참고하여 다음과 같이 키보드에서 입력할 수 있다.
# 학생명 입력, 학생명의 점수 입력(4과목 공백으로 구분)

classA = [] # 반 리스트
subject = ['Bigdata', 'Python', 'Flask', 'DB'] # 과목명 리스트

while True:
    menu = input('\t성젹 입력(a), 목록(s), 종료(x) : ')

    # 성적 입력
    # 학생명, 과목별 성적 입력
    if menu == 'a':
        name = input('\t학생명 : ')
        num = input(f'\t{name}의 4과목 점수입력(공백으로 구분) : ')
        numList = num.split()

        # record{key: 과목명, value: 성적}
        record = {}
        for i in range(4):
            record[subject[i]] = int(numList[i])
        # student{key: 이름, value: {과목명:성적}}
        student = {name:record} # student dictionary 값 저장
        # classA = [{이름:{과목명:성적}}]
        classA.append(student) # classA list 값 저장

    # 목록 조회
    elif menu == 's':
        print('\t***************성적 확인***************')
        print('\t이 름', end='\t') # 이름 출력
        for i in range(4): # 과목명 출력
            print(subject[i], end='\t')
        print('\t평 균')

        for name in classA:
            for key, value in name.items():
                print(f'\t{key}', end='\t') # 학생 이름
                total = 0
                for s in subject: # 과목별 점수, 평균
                    total += value[s]
                    print(f'{value[s]}', end='\t\t')
                avg = total/len(subject)
                print(f'{avg}')
    elif menu == 'x':
        break
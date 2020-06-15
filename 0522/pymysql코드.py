import sys
import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root',
                           password='tjoeun', db='test', charset='utf8')
    # connect: python->mysql 접속 시도
    # host: mysql이 실행되고 있는 컴퓨터 주소, localhost: 현재 컴퓨터
    # utf8 한글이 깨지지 않음

    curs = conn.cursor(pymysql.cursors.DictCursor)
    # cursor type 결정
    # DictCursor: dictionary 형식의 cursor을 생성하겠다

    print('MySQL DB에 접속 성공 !!!')

    # SQL 문장 실행
    curs.execute('select * from student')
    # mysql에 'sql'을 실행하겠다고 전달함
    # 행 수 리턴(가져온 행 수나 변경된 행 수)

    sList = curs.fetchall()
    # ({}): dictionary가 여러 행이므로 tuple로 저장
    for s in sList:
        print(s)

except pymysql.MySQLError as e:
    print(e)
    sys.exit()
finally: # 에러 유무에 상관없이 실행됨
    conn.close()


# ==== SELECT ====
sql = 'select * from student'
curs.execute(sql)
rows = curs.fetchall() # 튜플(Dict) 자료구조 리턴
print(rows) # 전체 행
print(rows[0]) # 첫 행, 한 개의 dict
print(rows[0]['name']) # 첫 행의 name 값

# SELECT 문장에 파라미터를 사용하는 예
sql = 'select * from student where name = %s'
curs.execute(sql, 'Jihee Kim')
rows = curs.fetchall()
print(rows)


# ==== INSERT ====
sql = '''insert into student(num, name, email) values (11, 'Songeun Lim', 'ehdspgkqkznl@hanmail.net')'''
curs.execute(sql, ('','',''))
conn.commit() # 변경사항 저장


# ==== UPDATE ====
sql = '''update customer
         set region = '서울특별시'
         where region = '서울' '''
curs.execute(sql)

# UPDATE 문장에 파라미터를 사용하는 경우
sql = 'update member set phone=%s where name=%s'
curs.execute(sql, ('',''))
conn.commit()


# ==== DELETE ====
sql = 'delete from customer where id=%s'
curs.execute(sql, 6)
conn.commit()
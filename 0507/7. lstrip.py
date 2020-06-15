# 기억된 string의 원본은 바뀌지 않음
# lstrip() 사용하면 새로운 string이 추가됨
lang = '    python'
print(lang)
print(lang.lstrip())
print(lang)

# 할당연산자(=)를 사용하면 객체에 새로운 데이터가 기억됨
# 그러나 기존 데이터가 들어있는 주소는 객체에 저장되어 있음
# 그러나 기존 데이터가 들어있는 주소를 찾을 수 없음
fav = '    python'
fav = fav.lstrip()
print('---------------------------')
print(fav)

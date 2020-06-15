def add(a, b):
    print(a + b)


# positional argument와 key argument를 함께 사용할 때는
# positional argument를 먼저 사용해야 한다

# keyword argument는 위치를 지정하지 않으므로
# 시스템에서 아래의 3은 어느 위치인지 정할 수 없음
# add(a=2, 3) # 오류
# add(b=2, 3) # 오류
add(2, b=3)  # 정상
# add(2, a=3) # 오류
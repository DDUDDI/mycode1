# 모듈명 충돌하면 내 파일에 있는 모듈이 import됨
# 모듈명 지을 때 주의

from car import Car

sonata = Car('SONATA', 2020, 2.0, 'white', 1000)
sonata.printinfo()

# shallow copy
s2 = sonata # sonata instance의 주소가 복사됨
s2.printinfo()

s2.price = 5000 # 동일한 주소를 참조하고 있으므로 sonata의 price값 수정
sonata.printinfo()

# deep copy
# 동일한 객체가 여러개 필요할 때 원본을 유지하기 위해 사용
import copy
s2 = copy.deepcopy(sonata) # s2 instance 생성
s2.price = 7000 # 다른 주소를 참조하고 있으므로 sonata의 price값 수정 X
sonata.printinfo()
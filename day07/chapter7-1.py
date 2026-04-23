
# 모듈 호출하기
# 표준 모듈 : 파이썬 내장 라이브러리
# 외부 모듈 : 설치형 라이브러리
# `import 모듈명`
import math             # import 모듈명
print( math.sin(1) )    # 호출한 모듈에서 sin 함수 호출.  +) `.`(접근연산자)
print( math.cos(1) )
print( math.tan(1) )
print( math.floor(2.5) )    # 올림
print( math.ceil(2.5) )     # 내림

# 특정한 변수/함수 가져오기: `from 모듈명 import 가져오고싶은함수또는변수명`
from math import sin , cos , tan
# 모두 가져오기: `from 모듈명 import *`
from math import *

# 식별자 부여: `import 모듈명 as 식별자명`
import math as m
from math import sin as s , cos as c , tan as t
print( c(1) )

# ================
# p.407
# random 모듈
import random
# random 모듈 기능
print(random.random() )            # `random()` : 0.0 <= x < 1.0 사이의 난수(실수) 생성
print(random.uniform( 10, 20 ))    # `uniform(시작값, 끝값)`: 사이의 난수(실수) 생성
print(random.randrange( 1, 10 ))   # `randtange(시작값, 끝값)`: 지정한 범위의 int(정수)를 리턴
print(random.choice([1, 2, 3]))    # `choice(리스트)`: 리스트 내 요소를 랜덤으로 선택
a = [1,2,3,4,5]
random.shuffle(a)                  # `shuffle(리스트)`: 리스트 내 요소를 랜덤으로 섞음
print(a)                                                # !단점: 원본이 수정된다.
print(random.sample([1,2,3], k=2)) # `sample(리스트, k=숫자)`: 리스트의 요소 중에 k개 선택
    # +) `k=2`: 키워드 매개변수. k라는 이름을 갖는 매개변수에 2 대입.

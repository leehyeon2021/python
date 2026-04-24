
# p.441
# 모듈 만들기: `.py`파일 만들기와 같다.
# 1. test_module.py 생성한다.
# 2. 다른 `.py`파일 내에서 import하여 모듈 호출한다.

import test_module as test
radius = test.number_input()
print( test.get_circumference( radius ) )
print( test.get_circle_area( radius ) )

# 프로그램의 진입점: __name__ == "__main__"
print( __name__ )   # __main__

# ============================================

# 인터넷의 이미지 저장하기
from urllib import request

target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)           # 바이너리 데이터로 반환된다. 앞에 'b'가 붙어있다.

# 바이너리 파일 저장 시 'wb' 사용한다.
file = open('./day08/output.png' , 'wb')
file.write( output )    # 파일 쓰기
file.close()            # 파일 닫기
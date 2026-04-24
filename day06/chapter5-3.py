
# 콜백 함수 : 함수의 매개변수에 사용하는 함수
def call_10_items( func ):      # 매개변수로 받은 함수
    for i in range( 10 ):
        func()

def print_hello():
    print("안녕하세요")

call_10_items( print_hello )    # 함수 자체를 매개변수로 전달
#call_10_items( print_hello() ) # 함수 실행() -> 소괄호 넣지 말기.

# 콜백 원한다면 소괄호 금지 (JS~)

# =====================

# map() , filter() 함수
# - map( 함수 , 리스트 ) : 리스트의 요소를 **하나 씩** 함수매개변수에 대입하여 **새로운 리스트** 반환
# - filter( 함수 , 리스트 ) : 리스트의 요소를 **하나 씩** 함수매개변수에 대입하여 참(True)인 경우

def power( item ) :
    return item * item  # 제곱 반환

def under_3( item ) :
    return item < 3     # 3미만 True 반환

list_input_a = [1, 2, 3, 4, 5]

# JAVA: list_input_a.stream.map( 함수 ).toList();
# JS: list_input_a.map( 함수 )
# PY: map( 함수 , list_input_a )

output_a = map( power , list_input_a )
print( list(output_a) )                     # [1, 4, 9, 16, 25]

output_b = filter( under_3 , list_input_a )
print( list(output_b) )                     # [1, 2]

# =====================

# p.336
# 제너레이터 : 함수 내부에 yield 키워드를 사용하여 next()함수를 외부에서 호출하여 yield 키워드까지 실행한다.
def test() :
    print( "A 지점 통과" )
    yield 1
    print( "B 지점 통과" )
    yield 2

test()              # 함수 호출 시 실행 안 됨
output = test()     # 1. 함수 반환값을 변수에 저장
a = next( output )  # 2. 함수 반환값이 저장된 변수를 next에 대입한다.   # A 지점 통과
print( a )                                                         # 1

b = next( output )                                                 # B 지점 통과
print( b )                                                         # 2

#c = next( output )                                                 # 없음
#print( c )

# 쉽게 말해보자면 yield는 스레드를 관리해주는 것. '기다리라'는 뜻과 같다.
# next를 할 때마다 다음 yield가 실행된다.

# ====================

# 람다: 함수 선언 간단하게 하는 문법
# `lambda 매개변수 : 반환걊`

# JS
# - 선언적 함수로 콜백 가능
# 함수 정의 이후 , <button onClick={함수명}>
# - 람다(화살표) 콜백 가능
# <button onClick={()=>{}}>

# 방법1 : 재사용 가능하다.
power = lambda x : x*x
output_a = map( power , list_input_a )
print( list(output_a) )

# 방법2 : 재사용 안 된다.
output_a = map( lambda x : x*x , list_input_a )
print( list(output_a) )

    # 변수 만드는 이유: 재사용 여부

# ===============================

# 파일 처리
# `open( 파일경로 , 읽기모드 )`
# 읽기모드: w새로쓰기 a이어쓰기 r읽기모드

# 1. `.open()` 함수 이용하여 지정한 경로의 파일 쓰기
file = open( './day06/basic.txt' , 'w' )    # 경로 지정 안 하면 현재 폴더 내 생성

# 2. `.write(출력할내용)` 함수 이용한 내보내기
file.write( '안녕하세요' )

# 3. `.close()` 함수 이용하여 안전한 스트림 닫기
file.close()

# 4. `with` 키워드 이용한 `.close()` 자동 닫기
with open( './day06/basic2.txt', 'w' ) as file:
    file.write( '아니오' )

# 스트림이란?: 데이터가 흐르는 길. 바이트 단위. 프로그래밍 언어가 외부 자료와 연결( 파일, JDBC, 네트워크 연결 )

# 5. `.read()` 함수 이용한 파일 읽어오기
with open('./day06/basic.txt' , 'r') as file:
    contents = file.read()

print( contents )       # 안녕하세요


# p.331
# 텍스트 한 줄씩 읽기
# 랜덤 숫자 생성 위해 가져오기
import random
# 간단한 한글 리스트
hanguls = list("가나다라마바사아자차카타파하")
# 파일을 쓰기 모드로 연다
with open('./day06/info.txt', 'w') as file:
    for i in range(1000):
        # 랜덤한 값 변수 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40 , 100)
        height = random.randrange(140 , 200)
        # 텍스트 쓰기
        file.write('{}, {}, {}\n'.format(name, weight, height))

with open('./day06/info.txt','r') as file:
    for line in file:
        # 변수 선언
        (name, weight, height) = line.strip().split(", ")
        # 데이터가 문제 없는지 확인 (문제 없으면 지나감)
        if(not name) or (not weight) or (not height):
            continue
        # 결과 계산
        bmi = int(weight) / ((int(height)/100) ** 2 )
        result = ''
        if 25 <= bmi:
            result = '과체중'
        elif 18.5 <= bmi:
            result = '정상 체중'
        else:
            result = '저체중'
        # 출력
        print( '\n'.join([
            '이름: {}',
            '몸무게: {}',
            '키: {}',
            'BMI: {}',
            '결과: {}'
        ]).format(name, weight, height, bmi, result))
        print()
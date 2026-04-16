# p.113

# 변수
pi = 3.141592   # '='같다는 의미가 아니라 우변의 값을 좌변에 넣겠다.

print( pi )         # 변수 참조: 변수가 갖는 자료 반환
print( pi + pi )

# 주의할 점
#print( pi + "입니다." )    # 오류가 발생한다: 다른 자료 연산 불가
print( pi , "입니다." )     # 연결은 `,` 쉼표로 하기

# 타입의 유연성 == 동적 타입!
    # 단점: 타입 식별이 어렵다. 변수만 보고 문자인지 숫자인지 구분 어려움. 오류가 발생할 수도 있다.
# 자바 또는 C언어: int pi = 3
# 파이썬: pi = 3

# p.116
# 복합 대입 연산자
number = 100
number += 10
print( number ) # 110
number -= 10
print( number ) # 100
number *= 10
print( number ) # 1000
number /= 10
print( number ) # 100.0
number %= 3
print( number ) # 1.0
number **= 3
print( number ) # 1.0
# 문자열도 가능
String = "안녕"
String += "하세요"
print(String)

# p.118
# 사용자 입력: `input( )`
    # 주의할 점: 콘솔에 입력하는 구조는 무조건 **문자열**로 반환한다.
input( "인사말을 입력하세요 > ")    # 명령 프롬프트에서 사용자로부터 데이터를 입력받을 때 사용
string = input( '인사말을 입력하세요 > ')   # input에 입력받은 말을 변수 string에 저장
print(string)   # 입력받은 말 나옴
# 자바에서는 Scanner vs 파이썬에서는 input
print( type( string ) ) # 입력 받은 값의 타입은: <class 'str'> , 숫자나 true로 입력 받아도 <class 'str'>.

# p. 121
# 문자열을 숫자로 변환하기: int( )
    # 사용처: input( ) , HTTP 문자열 통신
    # 타입 변환을 해야 하는 이유: 자료를 사용할 때 서로 다른 타입 간에 예외가 발생할 수 있다.
string_a = input("입력 A > ")
int_a = int(string_a)
print( type(int_a))         # <class 'int'>

string_b = int( input( "입력 B > "))    # 밥먹기( 공부하기() ) 공부->밥 , input->int
print(type(string_b))       # <class 'int'>

string_c = float( input("입력 C > "))
print( type( string_c ))    # <class 'float'>

# p.124
# 숫자를 문자열로 바꾸기
pi = 3.141592
string_d = str( pi )
print( type( string_d ) )   # <class 'str'>

str_input = input("원의 반지름 입력> ")
num_input = int( str_input )
print("반지름: " , num_input)
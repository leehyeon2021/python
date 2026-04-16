# 문자열의 format( ) 함수 
    # 자바의 System.out.printf("%s", 10)이랑 비슷하다.)
    # {} 개수와 자료의 개수는 일치해야 한다.
string_a = "{}".format( 10 )
print( string_a , type( string_a ) )    # 10 <class 'str'>

format_a = "{}만 원".format( 5000 )
print( format_a )
format_b = "{} {} {}".format( 1, "포켓몬" , True )
print( format_b )

# 특정 칸에 출력하기
    # `{:자릿수d}`
    # `{여기 안에 공백 넣으면 안 됨!}`
output_a = "{:5d}".format( 52 )     # '   52' 다섯 칸 차지, 오른쪽
print(output_a)
output_b = "{:05d}".format( 52 )    # '00052' 공백 0으로 채움.
print(output_b)

# 기호 붙여 출력하기
output_c = "{:+d}".format( 52 )     # '+52'
print( output_c )
output_d = "{:+d}".format( -52 )    # '-52'
print( output_d )

# 부동소수점 출력하기
output_e = "{:15f}".format( 52.273 )    # '      52.273000' 15칸 차지
print( output_e )
output_f = "{:+015}".format( 52.273 )   # '+0000000052.273' 0: 채울 숫자 , 15: 자릿수 , f: 실수
print( output_f )
output_g = "{:15.3f}".format( 52.2731 ) # '         52.273' ``.소수자릿수f`
print( output_g )   # 잘린 부분 자동 반올림 됨!

# 의미없는 소수점 제거하기: `{:g}`
output_h = "{:g}".format( 52.0 )
print( type( output_h ))    # <class 'str'>

# ============================
# p.141
# 대소문자 바꾸기
a = "HelLo pyThOn"
print( a.upper() )  # 대문자로 변경
print( a.lower() )  # 소문자로 변경

# ============================
# p.142
# 공백 제거하기: `strip()`: 양쪽 공백 제거, `lstrip()`: 왼쪽 공백 제거 , `rstrip()`: 오른쪽 공백 제거
b = "    안녕하세요   "
print(b.strip())

# ============================
# p.144
# 문자열 찾기
out_a = "안녕안녕하세요".find("안녕")
print( out_a )      # 0
out_b = "안녕안녕하세요".rfind("안녕")
print( out_b )      # 2

# in 연산자
print( "안녕" in "안녕하세요 ") # True
print( "잘가" in "안녕하세요 ") # False

# 문자열 자르기: `.split( 기준문자 )` 배열로 반환
out_c = "10 20 30 40 50".split(" ")
print( out_c )      # ['10', '20', '30', '40', '50']

# f-문자열 vs. .format()
print( f'{10}' )            # 10 ( `${}`같은 거. )
print( "{}".format(10) )    # 10
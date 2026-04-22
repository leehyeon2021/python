
# p.360
# 예외처리: 예외가 발생할 상황을 예측하고 모두 조건문으로 처리하는 것은 매우 힘들다.
# 예외가 발생하면 프로그램이 강제로 종료되지 않게 흐름 제어 하기 = 예외처리
# try: ~ except : ~

try:
    number_input_a = int( input( '[try] 정수 입력: ') )        # 7->정상 , a->예외

except:
    # 만약에 예외가 발생했을 때
    print('[except] 정수만 입력하세요.')

# pass: 예외처리가 아닌, 일단 생략할 경우
list_input_a = [ "52", "273", "32", "옥의티", "103"]
list_number = [ ]
for item in list_input_a:
    try:
        float( item )           # float(): 실수 변환함수
    except:
        pass                    # 예외 발생 시 아무 것도 하지 않고 일단 통과

# else : 예외가 발생하지 않았을 때 실행 코드
try: 
    number_input_a = int(input('[try] 정수 입력: '))
except:
    print('[except] 정수만 입력하라고.')
else:
    print( number_input_a )

# finally : 무조건 실행할 코드
try:
    number_input_a = int(input('[try] 정수 입력: '))
except:
    print('[except] 정수가 아닙니다.')
else:
    print('[else] 예외가 발생하지 않았습니다!')
finally:
    print('[finally] 끝! (무조건 실행되는 코드)')



# p.292
# 재귀함수: 현재 실행 중인 (자신의)함수를 다시 호출하는 것

# 1. 반복문으로 팩토리얼 구하기
def func1( n ):
    output = 1
    for i in range( 1 , n+1 ):
        output *= i
    return output
print( "5!(팩토리얼):", func1(5) )     # 5!(팩토리얼): 120

# 2. 재귀함수로 팩토리얼 구하기
def func2( n ):
    if n == 0 :     # 만약에 매개변수가 0 이면
        return 1    # 함수 종료
    else:
        return n * func2( n - 1 )   # 재귀함수 호출
print( "5! :", func2(5) )           # 5! : 120
# func2( 5 ) -> 5 * 재귀    (안 끝남)                                                5 * 3 * 2 * 1 * 1
# func2( 4 ) ->     4 * 재귀    (안 끝남)                                        4 * 3 * 2 * 1 * 1
# func2( 3 ) ->         3 * 재귀    (안 끝남)                                3 * 2 * 1 * 1
# func2( 2 ) ->             2 * 재귀    (안 끝남)                        2 * 1 * 1
# func2( 1 ) ->                 1 * 재귀    (안 끝남)                1 * 1
# func2( 0 ) ->                     return 1   ( func2 함수는 총 몇번 호출 ? 6번 호출  , return 6번 되어야한다. )
# 5 * 4 * 3 * 2 * 1 * 1

# 3. 피보나치 수열1
    # 1번째 수열: 1 
    # 2번째 수열: 2 
    # n번째 열: n-1수열 + n-2수열
# func3( 4 )        -> return 재귀(3) + 재귀(2)
    # func3( 3 )        -> return 재귀(2) + 재귀(1)         1 + 1
    # func3( 2 )            -> return 재귀(1) + 재귀(0)     1 + 0
# 문제점: 재귀수가 많아서 계산식이 오래 걸린다.

counter2 = 0                # 함수 밖에 있는 변수
def func3( n ):
    global counter2         # 함수 밖에 있는 변수 호출
    counter2 += 1
    print( '-->' , counter2 )
    if n == 1 :
        return 1
    if n == 2 :
        return 1
    else:
        return func3( n-1 ) + func3( n-2 )
print(func3( 10 ))



# 확인 문제 - 다부수고싶어짐
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람의수 = 100
memo = {}

def 문제( 남은사람수 , 최소사람수 ):
    key = str( [ 남은사람수 , 최소사람수 ] )
    # 종료 조건
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:
        return 0        # 무효하니 0을 리턴
    if 남은사람수 == 0:
        return 1        # 유효하니 수를 세면 되서 1을 리턴
    # 재귀 처리
    count = 0
    for i in range( 최소사람수 , 앉힐수있는최대사람수 +1 ):
        count += 문제( 남은사람수-i , i )
    # 메모화 처리
    memo[key] = count
    #print(memo)
    # 종료
    return count
print( 문제( 전체사람의수 , 앉힐수있는최소사람수 ) )

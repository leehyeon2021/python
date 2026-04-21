# 튜플: `( )` 소괄호 이용하여 여러 자료들을 감싼 자료형. 
    # 단, 수정이 안 된다. 

# 튜플 선언
tuple_test = ( 10 , 20 , 30 )
print( tuple_test )     # (10, 20, 30)

# 요소 호출: 인덱스 사용
print( tuple_test[0] )  # 10


# 주의할 점1: 수정 안 된다.
# tuple_test[0] = 40        # TypeError: 'tuple' object does not support item assignment

# 주의할 점2: 요소가 1개인 경우에는 `,` 쉼표를 넣어준다.
tuple_test2 = ( 273 , )
print(tuple_test2)      # (273,)

# '할당 구문'
[ a , b ] = [ 10 , 20 ]     # 오른쪽에 있는 리스트에 자료들을 왼쪽 변수에 대입
print( a , b )          # 10 20
( c , d ) = ( 10 , 20 )
print( c , d )          # 10 20

# 튜플은 소괄호를 생략해도 된다.
tuple_test = 10 , 20 , 30 , 40
print( tuple_test )     # (10, 20, 30, 40)

# 튜플을 이용한 스왑(교체): 할당 구문을 이용해 대입이 가능하므로 간편한 스왑 가능.
a , b = 10 , 20             # 10 , 20 갖는 튜플을 할당 구문으로 a=10 , b=20 대입한다.
a , b = b , a               # 할당 구문을 이용한 자료 스왑(교체): ( a , b ) = ( b , a ) 괄호만 생략된 것임
print( a , b )          # 20 10

# 함수 리턴 값
def test():
    return 10 , 20      # 튜플(10 , 20) or 리스트[10 , 20] or 딕셔너리{'a':10 , 'b':20}
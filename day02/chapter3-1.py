# 비교 연산자: ==같다 , !=다르다 , >초과 , <미만 , >=이상 , <=이하
# 문자열 비교: 가나다/abc 순으로 앞에 있는 것이 작은 값
print( "가방" == "가방" )   # True
print( "가방" != "하마" )   # True
print( "가방" > "하마" )    # False (아스키코드값, '가'가 '하'보다 숫자가 작음)

# 범위 논리
x = 25
print( 20 < x < 30 )
print( 40 < x < 60 )

# 논리 연산자: and or not (&& || !)
print( not True )       # False
print( True and True )  # True
print( True and False ) # False
print( True or False )  # True

# =========================================

# 파이썬 조건문: `if 조건 :`
number = int(input('정수 입력 > '))

if number > 0 :
    print("양수입니다.")

if number < 0 :
    print('음수입니다.')

if number == 0 :
    print("0 입니다.")
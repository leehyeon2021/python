import numpy as np

# 리스트
print( [1, 2, 3] + [4, 5, 6] )      # [1, 2, 3, 4, 5, 6]

# 배열 연산: 두 배열 간의 동일한 위치끼리 연산 수행
x = np.array( [1, 2, 3] )
y = np.array( [4, 5, 6] )
print( x + y )              # [5 7 9]
print( x - y )              # [-3 -3 -3]
print( x * y )              # [ 4 10 18]
print( x / y )              # [0.25 0.4  0.5 ]
print( x % y )              # [1 2 3]
print( x ** y )             # [  1  32 729]

# 비교 연산: 
print( x > y )          # [False False False]
print( x == y )         # [False False False]

# 배열 +*/% 숫자 : 자동으로 전체에 적용
print( x + 10 )     # [11 12 13]
print( y * 2 )      # [ 8 10 12]

# 논리 연산
x = np.array( [True, False, True] )
y = np.array( [False, True, True] )
# `.logical_and()`: 모두 참이면 참
print( np.logical_and(x, y) )       # [False False  True]
# `.logical_or()`: 하나라도 참이면 참
print( np.logical_or(x, y) )        # [ True  True  True]
# `.logical_not()`: 반대/부정
print( np.logical_not(x, y) )       # [False  True False]

# 루트(√): `.sqrt()`
y = np.array( [1, 4, 9])
print( np.sqrt( y ) )       # [1. 2. 3.]

# 2차원 비교
y = np.array( [ [1, 2, 3] , [4, 5, 6] ] )
print( y > 3 )      # [[False False False] [ True  True  True]]

x = np.array( [ 1, 10, 3] )
print( x > y )      # x 1차원: 행 1개 , y 2차원 행 N개

# `.all( x )`: 모두 참이면 참
# `.any( x )`: 하나라도 참이면 참
x = np.array( [ True , False , True ] )
print( np.all( x ) )    # False
print( np.any( x ) )    # True

# `.equal( x , y )`: 두 배열의 요소들이 모두 같으면 True
x = np.array( [1, 2, 3] )
y = np.array( [1, 2, 3] )
z = np.array( [4, 5, 6] )
print( np.array_equal(x, y) )   # True
print( np.array_equal(x, z) )   # False
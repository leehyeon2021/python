
# 배열 간 병합, 정렬

import numpy as np

# 병합
# `.concatenate( (x, y) , axis = 0 )`
    # axis = 0(행기준) 1(열기준)
x = np.array( [ [1, 2], [3, 4] ] )
y = np.array( [ [5, 6], [7, 8] ] )

# x 아래와 y가 붙는다.
print( np.concatenate( ( x, y ), axis = 0 ) )
# x 오른쪽과 y가 붙는다.
print( np.concatenate( ( x, y ), axis = 1 ) )

# ================

# 정렬
# 오름차순: `.sort( x )`
# 내림차순: `.sort(x[ : : -1])`
x = np.array( [3, 1, 2, 5, 4] )     # [1 2 3 4 5]
print( np.sort( x ) )
print( np.sort( x )[ : : -1] )      # [5 4 3 2 1]

# 2차원 정렬
# `.sort( x , axis = 0)`
# `axis = 0(열기준) 1(행기준) None(1차원 정렬)`
x = np.array( [ [3, 1, 2] , [9, 8, 7] ] )
# 열 기준 오름차순
print( np.sort( x , axis = 0 ) )
# 행 기준 오름차순
print( np.sort( x , axis = 1 ) )
# 1차원 평탄화 후 정렬
print( np.sort( x , axis = None ) )     # [1 2 3 7 8 9]

# 2차원 정렬 내림차순 주의할 점: 2차원 슬라이싱 적용 (`[행슬라이싱, 열슬라이싱]`)
# 열 기준 내림차순
print( np.sort( x , axis = 0 )[ : : -1 , :] )
# 행 기준 내림차순
print( np.sort( x , axis = 1 )[ :, : : -1 ] )

# `np.sort()`          복사본 반환 
# vs. `배열.sort()`    원본 수정 -> 원본 수정 여부 차이
x = np.array( [1, 2, 3] )
print( np.sort( x ) )
print( x.sort() )
print( x )

# 다중 정렬
# : 1차 정렬 후, 만약 **1차 정렬에서 동일한 값이 존재한다면**, 동일한 값끼리 2차 정렬한다.
# 중복값 있을 때 사용
x = np.array( [25, 30, 22, 24] )
y = np.array( [ '철수', '영희', '민수', '영희' ] )
z = np.lexsort( ( x, y ) )
print( y[z] )   # ['민수' '영희' '영희' '철수']    - y 먼저 정렬 후
print( x[z] )   # [22 24 30 25]                  - y 정렬 후 동일한 값끼리 2차 정렬

# ===============================
# 필터링
# 1차원
x = np.array( [10, 20, 30, 40, 50 ] )
print( x > 30 )         # [False False False  True  True]
print( x[ x > 20] )     # [30 40 50]
# 2차원
y = np.array( [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ] )
print( y % 2 == 0 )
print( y[ y%2==0 ] )    # [2 4 6 8]

# 조건부 필터링: `.where( 조건, 참, 거짓 )` (like 삼항연산자)
# 1차원
print( np.where( x > 30 , x , 0 ) )    # 만약 요소값이 30보다 크면 그대로, 아니면 0(False)
# 2차원
print( np.where( y%2==0 , y , 1 ) )    # 만약 요소값이 짝수이면 그대로, 아니면 1(True)

# 마스크 필터링: 조건식에 False만 사용
# `.ma.array( x , mask = 조건식 )`
con1 = x < 30       # 30 이상을 마스크(가린다.)
z = np.ma.array( x, mask = con1 )
print( np.ma.sum( z ) )     # 120

# 다수 조건 필터링
con2 = y % 2 == 0       # 조건1: 짝수
con3 = y % 4 == 0       # 조건2: 짝수
print( y[con2 & con3] )     # [4 8]    -> 비트 연산자
print( y[con2 | con3] )     # [2 4 6 8]
print( y[~con2] )           # [1 3 5 7 9]

# 특정 조건 충족하는 배열 반환
# `.extract( 조건 , x )`: 조건을 충족하는 요소만 추출
print( np.extract( y % 2 == 0 , y ) )   # [2 4 6 8]
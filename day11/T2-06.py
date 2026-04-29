import numpy as np

# 통계
# 파이썬은 시각화 되기 전의 엑셀 같은 것이다.

x = np.array( [1, 2, 3, 4, 5] )

# 최소값
print( np.min( x ) )        # 1
# 최댓값
print( np.max( x ) )        # 5
# 최소값의 (인덱스) 위치 argument
print( np.argmin( x ) )     # 0
# 최댓값의 (인덱스) 위치
print( np.argmax( x ) )     # 4
# 최댓값 - 최소값
print( np.ptp( x ) )        # 4
# 합계
print( np.sum( x ) )        # 15
# 평균
print( np.mean( x ) )       # 3.0
# 중앙값
print( np.median( x ) )     # 3.0
# 분산: 요소들의 흩어짐 정도
print( np.var( x ) )        # 2.0
# 표준편차: 분산의 양의 제곱근
print( np.std( x ) )        # 1.4142135623730951
# 루트
print( np.sqrt( x ) )       # [1.         1.41421356 1.73205081 2.         2.23606798]

# 사분위수: 구역을 4개 구역으로 나눠서 데이터 분포 위치 파악
# q1: 제1사분위수. 1/4 , 25% , 하위 25%
q1 = np.percentile( x , 25 )
# 3/4 , 75% , 하위 75%
q3 = np.percentile( x , 75 )
print( q1 )                 # 2.0
print( q3 )                 # 4.0
# 2/4 , 50% , 중앙값
q2 = np.percentile( x , 50 )
print( q2 )                 # 3.0
q4 = q3 - q1
print( q4 )                 # 2.0

# 2차원 배열 통계
# `통계함수( x , axis = 0 )`   (0=열기준 1=행기준)
y = np.array( [ [1, 2, 3], [4, 10, 6] ] )
print( np.min( y , axis = 0 ) )     # [1 2 3]   -> 열 개수가 3개니까 최솟값이 3개
print( np.min( y , axis = 1 ) )     # [1 4]     -> 행 개수가 2개니까 최솟값이 2개
print( np.max( y ) )            # 10  -> axis 생략하면 2차원 배열 평탄화(1차원으로 변경)해서 통계
print( np.argmax( y ) )         # 4   -> 평탄화 되었음
print( np.argmin( y ) )         # 0
print( np.sum( y ) )            # 26
print( np.mean( y ) )           # 4.333333333333333
print( np.median( y ) )         # 3.5
print( np.var( y ) )            # 8.88888888888889
print( np.std( y ) )            # 2.9814239699997196
print( np.sqrt( y ) )           # [[1.         1.41421356 1.73205081] [2.         3.16227766 2.44948974]]
print( np.())
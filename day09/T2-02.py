
# 넘파이 호출
import numpy as np

# [2] 배열의 주요 속성
# `.shape`: 현재 배열의 크기를 튜플로 반환 (행개수와 열 개수 알려줌)
x = np.array( [ [1, 2, 3] , [4, 5, 6] ] )   # 2차원
print(x.shape)      # (2, 3)
# `.dtype`: 현재 배열 내 데이터 타입 반환
x = np.array( [ 1.0, 2.0, 3.0 ] )
print( x.dtype )    # float64
# `.size`: 현재 배열 내 모든 요소 수
x = np.array( [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ] )
print(x.size)       # 9
# `.ndim`: 현재 배열의 차원 수
x = np.array( [1, 2, 3] )
print(x.ndim)       # 1
x = np.array( [ [ [1], [2] ] , [ [3], [4] ] ] )     # [ 1차원배열 [ 2차원배열 [ 3차원배열 ] ] ]
print(x.ndim)       # 3
# `.flat`: 다차원 배열을 1차원으로 반환
x = np.array( [ [1, 2], [3, 4] , [7, 0] ] )
print( x.flat )     # <numpy.flatiter object at 0x000001C444866E70>
for element in x.flat:
    print( element )# [1 2 3 4 7 0] -> 1차원으로 변경됨


# [3] 배열의 데이터 타입
# bit란?: 0 또는 1로 이루어진 2진수
# 8bit란? 0 또는 1으로 이루어진 2진수가 8개 모이면 -> 1byte
# 즉] bit 많을수록 더 많은 자료를 표현할 수 있다.
# `.array( 자료 , dtype = numpy.타입명 )` (키워드매개변수사용)
# 부호가 있는 실수형
x = np.array( [1, 2, 3] , dtype = np.int32 )
print( x.dtype )    # int32 , 정수형 32bit , bit가 클수록 더 많은 정보를 저장한다.
# 필요에 따라 적절하게 bit를 선택한다.
# 비정밀도 실수형
x = np.array( [1.0 , 2.0 , 3.0] , dtype = np.float64 )
print( x.dtype )    # float64 <- 더 큰 bit이면 더 (정밀하게!) 오차를 최소화한다.
# 논리형
x = np.array( [True, False, True], dtype=np.bool_ )
print( x.dtype )    # bool
# 바이트 문자열
x = np.array( ['apple', 'banana'] , dtype=np.bytes_ )
# 데이터 타입 변환: `.astype( numpy.반환할타입명)`
x = np.array( [1.5, 2.3, 3.7] )     # 실수
print(x.dtype)              # float64
y = x.astype(np.int32)      # float64 -> int32
print(y)                    # [1 2 3] <- int(정수형)은 소수점을 표현할 수 없으므로 소수점 잘림
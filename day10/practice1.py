# 넘파이: 파이썬 언어 기반으로 수치 계산 특화된 라이브러리 (AI)
# 파이썬에 **리스트**가 존재하는데 굳이 **넘파이배열**을 사용하는 이유는?
# : 기능 차이

# 문제 1: ndarray 생성
# 넘파이를 임포트하고, 리스트 [10, 20, 30, 40]를 사용하여 1차원 배열을, 
# [[1, 2], [3, 4]]를 사용하여 2차원 배열을 각각 생성하여 출력하시오.
import numpy as np
array1 = np.array( [10, 20, 30, 40] )
array2 = np.array( [ [1, 2] , [3, 4] ] )
print( array1 )
print( array2 )

# 문제 2: 특정 값으로 채워진 배열
# 다음 조건에 맞는 배열을 생성하는 코드를 작성하시오.
# 1. 모든 요소가 0으로 채워진 3행 4열의 배열
# 2. 모든 요소가 1로 채워진 2행 5열의 배열
# 3. 모든 요소가 9로 채워진 3행 3열의 배열 (힌트: np.full)
print( np.zeros( (3, 4) ) )
print( np.ones( (2, 5) ) )
print( np.full( (3, 3) , 9 ) )

# 문제 3: 연속된 수와 균등 간격 배열
# 1. np.arange를 사용하여 10부터 50까지 5씩 증가하는 배열을 생성하시오.
# 2. np.linspace를 사용하여 0부터 10 사이를 균등하게 5개의 구간으로 나눈 배열을 생성하시오.
print( np.arange( 10 , 51 , 5 ) )
print( np.linspace( 0, 10, 5 ) )

# 문제 4: shape와 size 확인
# x = np.array([[1, 2, 3], [4, 5, 6]]) 배열의 모양(행, 열 크기)과 
# 전체 요소의 개수(size)를 출력하는 코드를 작성하시오.
x = np.array([[1, 2, 3], [4, 5, 6]])
print( x.shape )  # (2, 3)  # shape-> (행개수, 열개수) 알려줌
print( x.size )   # 6       # 배열 내 전체 요소 수 반환

# 문제 5: 차원 확인 (ndim)
# 1차원 배열 [1, 2, 3]과 3차원 배열 [[[1], [2]], [[3], [4]]]를 각각 생성한 후, 
# .ndim 속성을 사용하여 각각 몇 차원인지 출력하시오.
x = np.array([1, 2, 3])
print( x.ndim )     # 1
x = np.array([[[1], [2]] , [[3], [4]]])
print( x.ndim )     # 3

# 문제 6: 데이터 타입(dtype) 확인
# 실수형 데이터 [1.5, 2.5, 3.5]를 가진 배열을 만들고, 
# 이 배열의 요소들이 어떤 데이터 타입으로 저장되어 있는지 출력하시오.
x = np.array([1.5, 2.5, 3.5])
print( x.dtype )    # float64

# 문제 7: 배열 평탄화 순회 (flat)
# 2행 2열의 2차원 배열을 생성한 후, .flat 속성과 반복문(for)을 사용하여 
# 모든 요소를 한 줄씩 차례대로 출력하시오.
x = np.ones( (2, 2))
for i in x.flat:
    print(i)

# 문제 8: 타입 지정 생성
# 배열을 생성할 때 dtype 옵션을 사용하여 다음 조건에 맞는 배열을 만드시오.
# 1. 정수형(int32) 타입의 배열 [1, 2, 3]
# 2. 불리언(bool) 타입의 배열 [True, False, True]
x = np.array([1, 2, 3] , dtype=np.int32)
print(x.dtype)  # int32
x = np.array([True, False, True] , dtype=np.bool_)
print(x.dtype)  # bool

# 문제 9: 형변환 (astype)
# 실수형 배열 x = np.array([1.1, 2.9, 3.5])를 생성한 후, 
# .astype() 메서드를 사용하여 소수점이 제거된 정수형(int32) 배열로 변환하고 출력하시오.
x = np.array([1.1, 2.9, 3.5])
y= x.astype(np.int32)
print(y)        # [1 2 3]

# 문제 10: 바이트 문자열 배열
# 과일 이름 리스트 ['apple', 'banana']를 넘파이 배열로 만들되, 
# 데이터 타입을 np.bytes_로 지정하여 생성하고 결과를 확인하시오.
x = np.array(['apple', 'banana'], dtype=np.bytes_)
print(x.dtype)  # |S6


# numpy: 배열 기반( 위치(인덱스) ). 공학 수치 계산에 용이하다.
    # - 동일한 타입만 저장 가능하다.
# pandas: 테이블 기반( 라벨(인덱스) 포함 ). 전처리/필터링(numpy 포함됨).     -> numpy보다 직관적
    # - 다양한 타입 데이터를 유연하게 병합한다.
    # 1차원: series
    # 2차원: dataframe


# [1] pandas 설치: pip install pandas (py -m pip install pandas)
# [2] import pandas as pd
import pandas as pd
print( pd.__version__)      # 3.0.2

# 1. 생성
# `.Series( 자료 )`: 1차원 한 줄
x = [ 10 , 20 , 30 , 40 ]
x1 = pd.Series( x )
print( x1 )
# 이렇게 출력됨:
# 0    10       -> 0 ~ 4 : 각 요소들의 인덱스
# 1    20       -> 10 ~ 50 : 각 요소들의 값
# 2    30
# 3    40
# dtype: int64  -> 데이터의 타입도 함께 보여준다.

# 2. 각 요소들의 라벨 포함하기
y = [ 'a', 'b', 'c', 'd' ]
y1 = pd.Series( x , index=y )   # index에 라벨(목록) 대입
print(y1)
# a    10                       # a ~ d : 각 요소들의 인덱스(라벨)
# b    20
# c    30
# d    40
# dtype: int64

# 3. 딕셔너리로 생성
z = { 'apple' : 1 , 'banana' : 2 , 'cherry' : 3 }
z1 = pd.Series( z )
print( z1 )
# apple     1
# banana    2
# cherry    3
# dtype: int64

# 4. 주요 속성 확인
# 타입반환
print( z1.dtype )           # int64
# 인덱스 반환   
print( z1.index )           # Index(['apple', 'banana', 'cherry'], dtype='str')
# 값 반환
print( z1.values )          # [1 2 3]
# `.head(n)`: 상위 n개(기본값=5)만 출력. 확인용으로 사용.
print( z1.head(1) )         # apple    1    dtype: int64
# `.tail(n)`: 하위 n개(기본값=5)만 출력
print( z1.tail(1) )         # cherry    3   dtype: int64
# `.iloc[인덱스]`: index location. 라벨이 아닌 위치로 조회. (당연히슬라이싱가능)
print( z1.iloc[0] )         # 1

# Series의 기존 문자 인덱스를 제거하고 0부터 시작하는 숫자 인덱스로 재설정
# `.reset_index( drop=True )`
y = x.reset_index( drop=True )
print(y)

# 5. 인덱싱
# `.iloc[ 인덱스번호 ]`: 라벨이 아닌 위치로 조회
print( z1.iloc[0] )
# `.loc[ 라벨명 ]`: 라벨명으로 조회
print( z1.loc['apple'] )
# `.loc[ 시작라벨 : 끝라벨 ]`
print( z1.loc['apple' : 'cherry'] )

# 6. 데이터 수정
# [ 라벨명 ] = 새로운값
z1['apple'] = 10
print( z1 )         # apple     10  banana     2    cherry     3    dtype: int64

# 7. 데이터 추가
# [ 새로운라벨명 ] = 새로운값
z1[ 'berry' ] = 40
print( z1 )         # apple     10  banana     2    cherry     3    berry     40    dtype: int64

# 8. 병합: `.concat( [ x , y ] )`
x = pd.Series( [ 10 , 20 , 30 ] , index = [ 'a', 'b', 'c' ] )
y = pd.Series( [ 40 , 50 ] , index = [ 'd' , 'e' ] )
z = pd.concat( [ x , y ])
print(z)
    # NumPy로 [이름,값]하겠다고 바보짓한 거 pandas는 한 번에 해버리네 ㅠ.ㅠ

# 9. 라벨 이름 변경
# `.rename( { '기존라벨' : '새로운라벨 } )`
x = z.rename( {'a' : 'apple'} )
print(x)
# +) 파이썬의 문자(리터럴)(문자열은 아스키/유니코드라서 리터럴. 리터럴의 불변 특징 때문에 대입을 다시 받아야 한다.)
test = 'hello java'             # hello java
test = test.replace( ' ' , '_' )
print( test )                   # hello_java

# 10. 필터링: `[조건식]` , `[ ( 조건식 ) | ( 조건식 ) ]`
# 30 초과 필터링
x = z[ z > 30 ]
print( x )              # d    40   e    50 dtype: int64
# 25 보다 작거나 35 보다 크다
x = z[ ( z < 25 ) | ( z > 35 ) ]
print(x)                # a    10   b    20 d    40 e    50 dtype: int64
# 25 보다 크면서 35 보다 작다
x = z[ ( z > 25 ) & ( z < 35 ) ]
# 30 초과한 요소값에 10 더한 후 30 초과한 요소에만 대입
z[ z > 30 ] = z[ z > 30 ] + 10
print( z )              # a    10   b    20 c    30 d    50 e    60 dtype: int64

# 11. 통계
print( '합계:', z.sum() )         # 170
print( '평균:', z.mean() )        # 34.0
print( '최댓값:',z.max() )        # 60
print( '최솟값:', z.min() )       # 10
print( '중앙값:', z.median() )    # 30.0
print( '분산:', z.var() )         # 430.0
print( '표준편차:', z.std() )     # 20.73644135332772
print( '요소 개수:', z.count() )  # 5
# 각 요소별 중복 개수 !!
print( '중복:', z.value_counts() )                  # 20    1   30    1 ... Name: count, dtype: int64
# 각 요소가 전체에서 차지하는 비율( 0 ~ 1 )
print( '비율:', z.value_counts( normalize=True ) )  # 10    0.2 20    0.2 ... Name: proportion, dtype: float64

# 12. 정렬
# 인덱스(라벨) 기준의 정렬: `.sort_index()`
x = z.sort_index()
print( x )
# 값 기준의 정렬: `.sort_values()`
x = z.sort_values()
print( x )
# 내림차순 바꾸기: `.sort_index( ascending= False )` (False-내림차순desc)
x = z.sort_index( ascending= False )    # 내림차순 (desc)
print( x )
x = z.sort_values( ascending= False )   # 내림차순 (desc)
print( x )
# 1차 정렬 후 2차 정렬 유지하기
# 1차 정렬에 `kind='stable'` 추가
x.sort_index().sort_values( ascending=False , kind='stable' )


# 13. 그룹
# `.groupby( level=0 ).집계함수()`: 그룹 이후에 집계가 중요.
z = pd.Series( [ 10, 10, 40, 30, 20, 30] , index=['a', 'c', 'b', 'b', 'c', 'a'] )
# 라벨(인덱스)별 합계
x = z.groupby( level=0 ).sum()
print(x)
# 라벨(인덱스)별 평균
x = z.groupby( level=0 ).mean()
# `.groupby( level=0 ).agg( ['함수명' , '함수명' ] )`: 여러 개 한 번에 묶어서 집계
x = z.groupby( level=0 ).agg( ['sum', 'mean', 'count' ] )

import pandas as pd
# 판다스
# 1차원: `pd.Series()`
# 2차원: `pd.DataFrame()`

# 데이터프레임 생성
# : `pd.DataFrame( 2차원리스트/딕셔너리/넘파이배열 , columns = [ 열이름목록 ] , index = [ 행이름 ] )`

# [1] 데이터프레임 생성 1
# `pd.DataFrame( 2차원리스트 , columns = [ 열이름목록 ] , index = [ 행이름 ] )`
data_list = [ 
    [ 'ant' , 25 , 'seoul' ] , 
    [ 'bee' , 30 , 'busan' ] , 
    [ 'cat' , 35 , 'incheon' ] 
]
x = pd.DataFrame( data_list )
print( x )
print()

# [2] 데이터프레임 생성 2
# `pd.DataFrame( 딕셔너리 )` 대부분의 공공자료는 딕셔너리이기 때문에 자주 사용된다.
data_dict = {
    'name' : [ 'ant' , 'bee' , 'cat' ],
    'age' : [ 25 , 30 , 35 ],
    'city' : [ 'seoul' , 'busan', 'incheon' ]
}
x = pd.DataFrame( data_dict )
print( x )
print()

# [3] 데이터프레임 생성 3
# `pd.DataFrame( 넘파이배열 , columns = [ 열 이름 ] )`
import numpy as np
data_np = np.array( data_list )
x = pd.DataFrame( data_np , columns = [ 'name' , 'age' , 'city' ] , index=['a', 'b', 'c'])
print( x )
print( )

# [4]
# 행/열 크기: `.shape`
print( x.shape )    # (3, 3)
# 컬럼(열) 목록: `.columns`
print( x.columns )  # Index(['name', 'age', 'city'], dtype='str')
# 인덱스(행) 목록: `.index`
print( x.index )
# 값만 2차원으로 반환: `.values`
print( x.values )
# 상위 n개만 반환: `.head( 개수 )` (확인용으로 많이 씀)
print( x.head( 2 ) )
# 하위 n개만 반환: `.tail( 개수 )` (확인용으로 많이 씀)
print( x.tail( 2 ) )
# 전처리(데이터정리) 하기 전 결측치/타입 확인용. (확인용으로 꼭 씀)
x.info()    # 프린트 안 함
print()

# [5] 인덱싱
# iloc[ 인덱스번호 ]
print( x.iloc[1] )
# iloc[ 행, 열 ]
print( x.iloc[1, 2] )
# loc[ 라벨명 ]
print( x.loc['b'])
# loc[ 라벨명 , 컬럼명 ]
print( x.loc['b', 'city'] )
print()

# [6] 슬라이싱: `[ 시작인덱스 : 끝인덱스 , 시작라벨명 : 끝라벨명 ]`
# [ 행슬라이싱 : 열슬라이싱 ]
print( x.iloc[ 0:2 , 0:1 ] )
print( x.loc[ 'a':'b' , 'name':'city' ] )
print()

# [7] 새로운 열 추가: `[ '새로운열' ] = 새로운값` , `.assign( 새로운열 = 새로운값 )`
# 파괴적( 원본 수정 )
x['score'] = [ 100 , 80, 95 ]
print(x)
# 비파괴적( 원본 유지 )
x = x.assign( score2 = [ 87 , 65 , 78 ] )
print(x)
print()

# [8] 특정한 값 수정: `[ 기존 열 ] = 새로운값`
x[ 'age' ] = [ 31 , 52 , 40 ]
print(x)
# b행의 age열 값을 70으로 변경
x.loc['b', 'age'] = 70
print(x)
# 0행의 0열 값을 'apple'로 변경/수정
x.iloc[ 0 , 0 ] = 'apple'
print(x)
print()
# 한 번에 여러 개 수정
# `loc[ [시작라벨 : 끝라벨] , 컬럼라벨 ] = [ 새로운값 ]`
# `iloc[ [시작라벨 : 끝라벨] , 컬럼라벨 ] = [ 새로운값 ]`
x.loc[ ['a', 'b'] , 'score' ] = [ 10 , 20 ]
print(x)
print()

# [9] 필터링: `x[ 조건식 ]` -> `x[ x[열이름] > y ]` 행->열 검색.
cont1 = x['score2'] > 70
print( cont1 )      # True  False   True
print( x[cont1] )   # 데이터프레임[ 조건 ]

cont2 = x[ 'age' ] > 35         # 2번째 조건
print( x[ cont1 & cont2 ] )     # 1번째 조건과 2번째 조건으로 논리 연산 하기
print( x[ cont1 | cont2 ] )
print()

# [10] 필터링 조건으로 새로운 열 추가 또는 수정
# 열 추가
x.loc[ x[ 'score2' ] > 70 , 'passed' ] = True
# 열 수정
x.loc[ x[ 'score2' ] <= 70 , 'passed' ] = False
print(x)

# [11] 열(컬럼) 이름 수정: `.rename( index={ 행 라벨: } , columns={ 열 라벨: } )`
x = x.rename( columns={ 'city' : '도시', 'age' : '나이' } )
print(x)
print()

# [12] 집계: `.describe()` 수치 자료들을 집계해서 요약 (pandas만 됨)
print( x.describe() )
# `x[열이름].집계함수`
print( x['나이'].sum() )        # 141
print( x['score'].mean() )     # 41.666666666666664
# 특정 열의 빈도 확인
print( x['passed'].value_counts() )
print()
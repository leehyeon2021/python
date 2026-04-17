# p.192
# 리스트와 반복문

# 리스트란? : 여러 자료들을 모아 하나의 자료로 구성
# `[ , , , , ]`
# 인덱스란? : 자료가 저장된 순서. 0부터 시작.

# 슬라이싱
list_a = [ 273 , 32 , "문자열" , True ]
print( list_a[ 0 ] )        # 32
print( list_a[ 1 : 3 ] )    # [32, '문자열']

#요소값 변경
list_a[1] = "변경값"
print( list_a )             # [273, '변경값', '문자열', True]

# 뒤에서부터 요소 선택
print( list_a[ -2 ] )       # 문자열

# 리스트 안의 리스트1
print( list_a[ -2 ][0] )    # 문

# 리스트 안의 리스트2
list_a[ 1 ] = [ '변경값1' , '변경값2' ]
print( list_a )             # [273, ['변경값1', '변경값2'], '문자열', True]
print( list_a[1][1] )       # 변경값2

# ================================

# 리스트 연산
list_a = [ 1 , 2 , 3 ]
list_b = [ 4 , 5 , 6 ]

# [1] + 연결
print( list_a + list_b )    # [1, 2, 3, 4, 5, 6]

# [2] * 연결
print( list_a * 3 )         # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# [3] len 길이
print( len(list_a) )        # 3

# 리스트에 요소 추가
# [4] 요소 추가하기: `append( 자료 )`
list_a.append( 4 )
print( list_a )             # [1, 2, 3, 4]

# [5] 중간에 요소 추가하기
list_a.insert( 1 , 1.5 )
print( list_a )             # [1, 1.5, 2, 3, 4]

# ================================
# p.202
# 리스트 요소 제거
list_a = [ 0, 1, 2, 3, 4, 5 ]

# [6] `del 리스트명[인덱스]`
del list_a[1]
print( list_a )             # [0, 2, 3, 4, 5]

# [7] `리스트명.pop( 인덱스 )`
list_a.pop( 2 )
print( list_a )             # [0, 2, 4, 5]
list_a.pop()
print( list_a )             # [0, 2, 4]

# [*] 슬라이싱이란? : 인덱스로 구성된 자료들(문자열/리스트)의 요소 선택 기능
# `리스트명[ 시작인덱스 : 끝인덱스 : 단계 ]`
print( list_a[ : : -1 ] )   # [4, 2, 0]
print( list_a[ 0 : : 2 ] )  # [0, 4]

# [8] `리스트명.remove( 자료 )`
# : 해당 자료가 존재하면 삭제. (인덱스 말고 자료 삭제)
list_a.remove( 0 )
print( list_a )             # [2, 4]
#list_a.remove( 5 )          # 없으면 오류 뜸(ValueError)

# [9] `리스트명.clear()`
# : 모두 삭제
list_a.clear()
print( list_a )             # []

# [10] `.sort()` 리스트 오름차순 정렬
# `.sort( revers=True )` 내림차순 정렬
list_a = [ 52 , 273 , 103 , 32 ]
list_a.sort()
print( list_a )             # [32, 52, 103, 273]

list_a.sort( reverse=True )
print( list_a )             # [273, 103, 52, 32]

# [11] `in` : 내부에 있는지 확인
print( 103 in list_a )      # True
print( 250 in list_a )      # False
print( 103 not in list_a )  # False

# ==========================================

# 리스트와 반복문
# `for 반복변수 in 반복할 수 있는 자료 :`
    # vs. JAVA의 `리스트명.forEach( (요소) => {} )` (for문)
    # vs. JS의 `리스트명.forEach( (요소) -> {} )` (for문)

리스트명 = [ 273 , 32 , 103 , 57 , 52 ]

for 요소 in 리스트명 :
    print( 요소 )

for 요소 in "안녕하세요" :
    print( 요소 )

# 중첩 리스트 , 중첩 반복문 , 2차원 리스트
list_of_list = [
    [ 1 , 2 , 3 ] ,     # 1행 3열
    [ 4 , 5 , 6 , 7 ] , # 2행 4열
    [ 8 , 9 ]           # 3행 2열
]
for row in list_of_list :
    print( row )
    for col in row :
        print( col )

# 전개 연산자: `*`
# 리스트를 해체하여 전개한다.
    # 리스트는 첫 번째 인덱스를 참조한다. 첫 번째 인덱스를 기준으로 찾아옴
list_a = [ 1, 2, 3 ]
print( list_a )         # [1, 2, 3]
print( *list_a )        # 1 2 3

print( [ list_a , list_b ] )     # 2차원 리스트 구성 [[1, 2, 3], [4, 5, 6]]
print( [ *list_a , *list_b ] )   # 1차원 리스트 구성 [1, 2, 3, 4, 5, 6]

#=========================================

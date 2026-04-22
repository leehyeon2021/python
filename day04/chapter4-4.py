# 1. min , max , sum
numbers = [ 103 , 52 , 273 , 32 , 77 ]
# 최솟값
print( min(numbers) )   # 32
# 최댓값
print( max(numbers) )   # 273
# 누적 합계
print( sum(numbers) )   # 537

# 2. `reversed( 리스트 )`: 이터레이터 반환
print( reversed(numbers) )              # <list_reverseiterator object at 0x000001E8C7A47670>
print( list( reversed(numbers) ) )      # [77, 32, 273, 52, 103]

for i in reversed( numbers ):
    print( i )

# 3. `enumerate( 리스트 )`: 인덱스와 자료를 동시에 하나
print( enumerate(numbers) )             # <enumerate object at 0x00000204BC238450>
print( list( enumerate( numbers ) ) )   # [(0, 103), (1, 52), (2, 273), (3, 32), (4, 77)]

# 4. items( )
example_dictionary = { '키A':'값A', '키B':'값B', '키C':'값C' }
print( example_dictionary.items() )     # dict_items([('키A', '값A'), ('키B', '값B'), ('키C', '값C')])

for key , value in example_dictionary.items() :
    print( key , value )                # 키A 값A  키B 값B  키C 값C

# 5. 리스트내 반복문 사용, 반복문 이용한 리스트 생성
# 1) 
array = [ ]
for i in range( 0 , 20 , 2 ):
    array.append( i )
print( array )                  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 2) `[ 계산식 for 반복변수 in 반복할 수 있는 것 if 조건식 ]`
array = [ i for i in range( 0, 20 , 2 ) ]
print( array )                  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
array = [ i for i in range( 0 , 20 , 2 ) if i != 10 ]
print( array )                  # [0, 2, 4, 6, 8, 12, 14, 16, 18]

# 6. 문자열 여러 줄 입력하기
# 1) """ """
print( """안녕하세요1
안녕하세요2""") # 공백 조심!

# 2) \n
print( "안녕하세요1\n안녕하세요2" )

# 3) ( ) 소괄호 안에서 여러 개 문자 연결
print( ( "안녕하세요1\n" "안녕하세요2" ))

# 4) `조합문자열.join( 문자열리스트 )`: 리스트 내 요소 사이에 조합문자열 연결
print( "\n".join( ["안녕하세요1" , "안녕하세요2"] ) )


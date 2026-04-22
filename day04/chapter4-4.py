# 1. min , max , sum
numbers = [ 103 , 52 , 273 , 32 , 77 ]
# 최솟값
print( min(numbers) )   # 32
# 최댓값
print( max(numbers) )   # 273
# 누적 합계
print( sum(numbers) )   # 537

# 2. `reversed( 리스트 )`: 이터레이터 반환
print( reversed(numbers) )          # <list_reverseiterator object at 0x000001E8C7A47670>
print( list( reversed(numbers) ) )  # [77, 32, 273, 52, 103]

# 3. `enumerate( 리스트 )`: 인덱스와 자료를 동시에 하나

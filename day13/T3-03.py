
#
import pandas as pd

# 13. 판다스 병합 (SQL의 join on절)
# `.merge( x, y , on = '공통컬럼명(pk/fk)' , how='inner/outer/left/rigth(join어떻게할건지)' )`
df_info = pd.DataFrame( { 'ID' : [1, 2, 3] , 'Name' : ['Ant','Bee','Cat'] } )   # 그냥 샘플
df_score = pd.DataFrame( { 'ID' : [2, 3, 4] , 'Score' : [88,92,85] } )
# 두 판다스 간에 ID가 같은(교집합) 자료 병합
result = pd.merge( df_info , df_score , on = 'ID' , how = 'inner' )
print( result )
#
result = pd.merge( df_info , df_score , on = 'ID' , how = 'outer' )
print( result )

# 14. 판다스 합치기
# `.concat( [ x , y ] , axis = 0(행)/1(열) , ignore_index = True(0부터 새로 정렬)/False )`
# 세로 연결
result = pd.concat( [ df_info , df_score ] , axis = 0 , ignore_index=True )
print( result )
# 가로 연결
result = pd.concat( [ df_info , df_score ] , axis = 0 , ignore_index=True )
print( result )

# 15. 정렬
# `.sort_value( by='정렬기준' , ascending=True(오름)/False(내림) )`
# `.sort_value( by=['1차정렬', '2차정렬] , ascending=[ 1차정렬 , 2차정렬 ] )`
# `.sort_index( axis = 0(행)/1(열) , ascending=True(오름)/False(내림) )`
x = {
    'Name' : ['Ant', 'Bee', 'Cat', 'Dog' ],
    'Age' : [27 , 27 , 22 , 32] ,
    'Score' : [88, 95, 85, 90]
    }
df = pd.DataFrame( x )
# 점수 기준 내림차순
result = df.sort_values( by='Score' , ascending=False )
print( result )

# 나이 기준 오름차순 -+-> 점수 기준으로 내림차순 (나이 정렬 후 동일한 나이끼리 점수 내림차순)
result = df.sort_values( by=['Age', 'Score'] , ascending=[True, False] )
print( result )

# 열이름(라벨) 내림차순으로 정렬
result = df.sort_index( axis=1 , ascending=False )
print( result )

# 16. 그룹
# `.groupby('그룹기준')['집계기준'].집계함수()`
# `.groupby( [ '1차그룹' , '2차그룹'] )['집계기준'].집계함수()`
df = pd.DataFrame({
    'Category' : [ 'A', 'A', 'B', 'B', 'A', 'B' ],
    'Type' : [ 'X', 'Y', 'X', 'Y', 'X', 'Y' ],
    'Values' : [ 10, 20, 30, 40, 50, 60]
})
# 카테고리별 값의 합게
result = df.groupby('Category')['Values'].sum()
print( result )
# '타입' 별 '값' 평균
result = df.groupby('Type')['Values'].mean()
print( result )

# 다중 그룹
result = df.groupby( ['Category', 'Type'] )['Values'].agg( ['sum', 'mean', 'count'] )
print( result )
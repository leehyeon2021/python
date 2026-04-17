# p.216
# 딕셔너리란? : 키를 기반으로 값을 저장하는 것
# vs. JS(JSON) vs. JAVA(map/dto)

# [1] 선언: `{ "키" : 값 , "키" : 값 }`
dic_a = { "name" : "어벤져스 엔드게임" , "type" : "히어로 무비" }

# [2] 호출
print( dic_a )
# print( dic_a.name ) <- JS 가능하지만 오류 발생
print( dic_a["name"] )
print( dic_a.get("name") ) # JAVA MAP처럼 호출 가능
#print( dic_a["origin"] )  # 없는 키는 오류 발생

# [3] 딕셔너리 값 추가 하기
dic_a[ "price" ] = 21000
print( dic_a )             # {'name': '어벤져스 엔드게임', 'type': '히어로 무비', 'price': 21000}

# 만약에 존재하는 key라면 수정 (키 중복 불가)
dic_a["price"] = 10
print( dic_a )

# [4] 딕셔너리 키/값 제거하기: `del 딕셔너리명[ 'key' ]`
del dic_a[ 'price' ]
print( dic_a )              # {'name': '어벤져스 엔드게임', 'type': '히어로 무비'}

# =================================
# 반복문과 딕셔너리 관계
# for 키 in 딕셔너리명 :

for 키 in dic_a :
    print( 키 , ':' , dic_a[키])

#=====================
# 연습문제
pets = [
    {"name": "구름", "age": 5},
    {"name": "구", "age": 3},
    {"name": "름", "age": 5},
]

for pet in pets:
    print(pet["name"] , pet["age"], '살')


numbers = [1,4,6,3,7,7,4,3,1,2,4,1,2,6]
counter= {}
for number in numbers :
    if number in counter :
        counter[number] += 1
    else:
        counter[number] = 1
print( counter )


character = {
    "name" : "기사",
    "level" : 12 , 
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀블레이드"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type( character[key] ) is dict:          # 딕셔너리 내 key 값이 딕셔너리이면
        for 요소 in character[key]:
            print( 요소 , ":", character[key][요소])
    elif type( character[key] ) is list:        # 딕셔너리 내 key 값이 리스트이면
        for item in character[key]:
            print( key , ":", item )
    else:                                       # 딕셔너리 내 값이 리터릴이면
        print( key , ":" , character[key] )
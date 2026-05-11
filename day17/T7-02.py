import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# 정적페이지 크롤링

# 1. 크롤링할 주소 확인: https://www.yes24.com/product/category/bestseller

# 2. 주소의 매개변수 분석: ?categoryNumber=001&pageNumber=1&pageSize=40&sex=F&age=255&goodsStatGb=03

book_list = []

for page in range(1 , 4):   # 1~3페이지 크롤링 예시
    url = f'https://www.yes24.com/product/category/bestseller?pageNumber={page}'

    # 3. url 요청
    response = requests.get( url )

    # 4. 요청한 URL이 성공했을 때 html로 파싱
    soup = BeautifulSoup( response.text , 'html.parser')

    # 5. 가져올 식별자: 여러 개 선택 `soup.select()`(리스트 반환) , 하나 선택 `soup.select_one()`(객체 반환)
    # - 책 여럿: 여러개책정보 '#uesBestList' , 책 하나 li
    books = soup.select( '#yesBestList > li' )
    # - 책 하나: 책 제목 '.gd_name' , 책 가격 '.yes_b' , 저자 정보 '.info_auth'
    for book in books:  # <li> 여러 개 이므로 반복문 가능
        # 공백과 \n제거하기: `.strip()`, `.split(기준문자)` 사용
        gd_name = book.select_one('.gd_name').get_text().strip()
        yes_b = book.select_one('.yes_b').get_text().strip()
        info_auth = book.select_one('.info_auth').get_text().strip().replace('\n', '')
    
        # 6. 리스트[]에 딕셔너리{} 포함하기
        book_list.append( {'제목': gd_name , '가격': yes_b , '저자정보': info_auth} )
        
    # 7. `import time`: `time.sleep( 초 )` 지정한 초 만큼 코드(스레드)가 대기 상태. 서버 과부하 방지
    time.sleep(2)

# 확인
#print( book_list )

# 8. 판다스에 넣어주기
df = pd.DataFrame( book_list )
print( df )

# 파이썬 크롤링

# 웹 크롤링: 웹페이지에 존재하는 데이터들을 수집하는 기술
# 기초지식: HTML/CSS (식별자) 필요
# 파이썬 크롤링 라이브러리: (정적) request , BeautifulSoup / (동적(JS/대기필요)) Selenium , Playwright
# 크롤링(로봇) 허용 여부 확인: 도메인/robots.txt
# * 크롤링은 윤리적으로 적절히 사용하기

# -----

# 1. HTML/CSS 식별자( <마크업> , `#id` , `.class` , 자손선택자는 띄어쓰기 , 자식선택자는 `>` ) 찾기
# 브라우저 개발자 도구(F12) -> 왼쪽 상단에 마우스아이콘( CTRL+SHIFT+C ) 클릭 -> 크롤링 요소 선택 -> 확인

# -----

# 2. 파이썬 크롤링
# 네이버검색어 -> 안양날씨
# 1) 주소: https://search.daum.net/search?w=tot&q=안양+날씨
# - 쿼리스트링(주소 상의 변수): URL?변수명=값&변수명=값 , 필요한 변수만 정리
# - url에서는 한글 불가능 , 인코딩이 필요하다.
# 2) 크롤링 선택자: `.temperature_text`

# -----

# 3. 정적 라이브러리
import requests                 # URL 요청 라이브러리
from bs4 import BeautifulSoup   # 요청된 URL의 HTML 조작 라이브러리

# 1) `requests.get( url )`
response = requests.get( "https://search.daum.net/search?w=tot&q=안양+날씨" )
#print( response )    # <Response [403]>: 접근 권한 없어서 막힌 것 / <Response [200]>: 잘 된 것

# 2) 요청(200)된 url에서 HTML형식으로 파싱하기: `BeautifulSoup( response.text , "html.parser")`
soup = BeautifulSoup( response.text , "html.parser")
#print( soup )   # 마지막에 </html> 찍히는지 확인

# 3) 가져온 HTML에서 특정한 요소(식별자)만 가져오기: `soup.select_one( 식별자 )`
txt_temp = soup.select_one( '.txt_temp' )
print( txt_temp )

# 4) 가져온 요소에서 텍스트만 추출: `<마크업> *텍스트* </마크업>` , `요소변수.get_text()`
print( txt_temp.get_text() )    # 18.2
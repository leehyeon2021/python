import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# [ YES24 도서 정보 크롤링 기능 ]

# 1. 국내도서 종합 베스트 데이터 수집
#     가. YES24 국내도서 종합 베스트 페이지 접속
#     나. 최소 1000권 이상의 도서 데이터 크롤링
#     다. 페이지 이동 처리 구현
#     라. 수집 데이터 CSV 저장
# 2. 수집 대상 데이터
#     가. 도서 제목
#     나. 가격
#     다. 판매지수
#     라. 출판년월
# 3. CSV 저장
#     저장 파일 예시 : data/books.csv
#     CSV 컬럼 예시 : 제목,가격,판매지수,출판년월

# 주소: https://www.yes24.com/product/category/bestseller?pageNumber=1&pageSize=100
book_list=[]

for page in range ( 1, 11 ):
    url = f'https://www.yes24.com/product/category/bestseller?pageSize=100&pageNumber={page}'
    # url 요청
    response = requests.get( url )
    # 요청한 url -> html 파싱
    soup = BeautifulSoup( response.text , 'html.parser' )
    books = soup.select( '#yesBestList > li' )
    for book in books :
        # 도서 제목: .info_name > .gd_name
        gd_name = book.select_one('.info_name > .gd_name').get_text().strip()
        # 가격: .info_price > .txt_num > .yes_b
        yes_b = book.select_one('.info_price > .txt_num > .yes_b').get_text().replace(',','').strip()
        # 판매지수
        saleNum = book.select_one('.info_rating > .saleNum').get_text().replace('판매지수','').strip().replace(',','')
        # 출판년월
        info_date = book.select_one('.info_pubGrp > .info_date').get_text().replace('년 ','-').replace('월','').strip()
        book_one = ( {'제목': gd_name , '가격': yes_b , '판매지수': saleNum , '출판년월': info_date} )
        print( book_one )
        book_list.append(book_one)
    time.sleep(2)  

df = pd.DataFrame( book_list )
print( df )

df.to_csv(
    './yes24_book_system/data/books.csv',
    index=False,
    encoding='utf-8',
    na_rep='Null',
    header=True
)
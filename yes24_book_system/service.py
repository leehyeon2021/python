import pandas as pd
import matplotlib.pyplot as plt
import korean_font

class BookService:
    # 생성자
    def __init__(self):
    # 데이터 전처리 기능 , 기본 통계 분석 기능
    # [ 데이터 전처리 기능 ]
    # 1. 가격 데이터 전처리
    #     가. 쉼표(,) 제거 및 "원" 문자열 제거
    #     나. 숫자형(int) 변환, 예시: "18,500원" → 18500
    #print(df['가격'])
    # 2. 출판년월 데이터 전처리
    #     가. 연도(year) 컬럼 추출
    #     나. 월(month) 컬럼 추출,
        self.df = pd.read_csv('./yes24_book_system/data/books.csv', header=0, encoding='utf-8' )
        self.df['출판년월'] = pd.to_datetime( self.df['출판년월'] )
        self.df['연도'] = self.df['출판년월'].dt.year
        self.df['월'] = self.df['출판년월'].dt.month

    # [ 기본 통계 분석 기능 ]
    # 1. 가격 통계 분석
    #     가. 평균 가격 계산
    #     나. 최고 가격 계산
    #     다. 최저 가격 계산
    def df_mean( self ):
        return self.df['가격'].mean()
    def df_max( self ):  
        return self.df['가격'].max()
    def df_min ( self ):
        return self.df['가격'].min()

    # 2. 출판년도 분석
    #     가. 연도별 도서 수 계산
    def df_year_count ( self ):
        return self.df['연도'].value_counts()
    
    def result(self):
        a= {
            "평균가격": int(self.df_mean()),
            "최고가격": int(self.df_max()),
            "최저가격": int(self.df_min()),
            "최다출판연도": int(self.df_year_count().index[0])
        }
        print(a)
        return a

book_service = BookService()
import pandas as pd
import matplotlib.pyplot as plt
import korean_font

class BookService:
    def __init__(self):
        self.df = pd.read_csv('./yes24_book_system/data/books.csv', header=0, encoding='utf-8' )
        self.df['출판년월'] = pd.to_datetime( self.df['출판년월'] )
        self.df['연도'] = self.df['출판년월'].dt.year
        self.df['월'] = self.df['출판년월'].dt.month

    def df_mean( self ):
        return self.df['가격'].mean()
    def df_max( self ):  
        return self.df['가격'].max()
    def df_min ( self ):
        return self.df['가격'].min()

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



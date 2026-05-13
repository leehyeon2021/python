import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import korean_font

df = pd.read_csv('./yes24_book_system/data/books.csv', header=0, encoding='utf-8' )

# 데이터 전처리 기능 , 기본 통계 분석 기능 , 데이터 시각화 기능

# ================================

# [ 데이터 전처리 기능 ]
# 1. 가격 데이터 전처리
#     가. 쉼표(,) 제거 및 "원" 문자열 제거
#     나. 숫자형(int) 변환, 예시: "18,500원" → 18500
#print(df['가격'])
# 2. 출판년월 데이터 전처리
#     가. 연도(year) 컬럼 추출
#     나. 월(month) 컬럼 추출,
df['출판년월'] = pd.to_datetime( df['출판년월'] )
df['연도'] = df['출판년월'].dt.year
df['월'] = df['출판년월'].dt.month
print(df)

# ================================

# [ 기본 통계 분석 기능 ]
# 1. 가격 통계 분석
#     가. 평균 가격 계산
#     나. 최고 가격 계산
#     다. 최저 가격 계산
df_mean = df['가격'].mean()
df_max = df['가격'].max()
df_min = df['가격'].min()

# 2. 출판년도 분석
#     가. 연도별 도서 수 계산
df_year_count = df['연도'].value_counts().sort_index()
#print( df_year_count )

# ================================

# [ 데이터 시각화 기능 ]
# 1. 가격 분포 시각화
#     가. 히스토그램 구현
#     나. 가격대별 도서 개수 출력
#     다. 그래프 제목 및 축 이름 출력
plt.hist( df['가격'] , color='skyblue', bins=20 )
plt.title('가격대별 도서 개수')
plt.xlabel('가격')
plt.ylabel('개수')
#plt.show()

# 2. 출판년도별 도서 수 시각화
#     가. 막대그래프 구현
#     나. 연도별 출판 도서 수 출력
#     다. 그래프 제목 및 축 이름 출력

plt.bar(df_year_count.index , df_year_count.values, width=0.6, color="green")
plt.title('출판년도별 도서 수')
plt.xlabel('연도')
plt.ylabel('도서 수')
#plt.show()
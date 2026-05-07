import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import korean_font

# 판다스로 불러오기
df = pd.read_csv('./day15/train_HousePrices.csv')
#print( df.head() )          # 상위 5개 출력하여 데이터 확인
#df.info()                   # 속성 확인
#print( df.isnull().sum() )  # 결측치 확인
#print()

# 4. 데이터 전처리
# 4-1. 수치형 변수 결측치 처리: 'LotFrontage', 'MasVnrArea', 'GarageYrBlt' 등의 수치형 변수의 결측치는 데이터의 중앙값(Median)으로 대체하여 보정한다.
df['GrLivArea'] = df['GrLivArea'].fillna( df['GrLivArea'].median() )
df['SalePrice'] = df['SalePrice'].fillna( df['SalePrice'].median() )
print( df.isnull().sum() )

# 4-2. 범주형 변수 결측치 처리 (정보 부재 명확): 정보 부재가 명확한 범주형 변수('Alley', 'PoolQC', 'Fence' 등)는 결측치를 'NoAlley', 'NoPool', 'NoFence'와 같이 특정 문자열로 대체한다
df['RoofStyle'] = df['RoofStyle'].fillna( 'NoRoofStyle' )
df['HouseStyle'] = df['HouseStyle'].fillna( 'NoHouseStyle' )
print( df.isnull().sum() )

# 4-3. 범주형 변수 결측치 처리 (일반)
df['Exterior1st'] = df['Exterior1st'].fillna( df['Exterior1st'].mode()[0] )
print( df.isnull().sum() )


# 5. 데이터 시각화 및 분석
# 5-1. 주택 판매 가격(SalePrice) 분포 분석
# sns.histplot을 사용하여 주택 판매 가격(SalePrice)의 분포와 치우침(Skewness) 정도를 확인한다. (KDE 포함)
sns.histplot(  df['SalePrice'] , label='치우침 정도', color='#ff0000', kde= True)

plt.title('주택 판매 가격의 분포와 치우침')
plt.xlabel('판매 가격')
plt.ylabel('치우침')
plt.legend()
plt.show()

# 5-2. 주거 면적과 가격 관계 분석 (가설 1 검증)
# 지상 주거 면적 (GrLivArea)이 넓을수록 판매 가격은 정비례하여 상승할 것이다.
# sns.scatterplot을 사용하여 지상 주거 면적(GrLivArea)과 판매 가격(SalePrice) 간의 상관관계를 산점도로 분석한다.
sns.scatterplot(data=df, x=df["GrLivArea"], y=df["SalePrice"])
plt.show()

# 5-3. 주택 스타일별 가격 분포 비교 (가설 2 검증)
# sns.boxplot을 사용하여 주택 스타일(HouseStyle)별 가격 분포와 이상치(Outlier)를 파악한다.
print(df['HouseStyle'].head())
sns.boxplot( x = 'HouseStyle', y = 'SalePrice' , data = df )
plt.show()

# 5-4. 주요 외관 요소별 가격 분포 비교 (가설 2 검증)
# sns.boxplot을 사용하여 지붕 스타일(RoofStyle) 및 외장재(Exterior1st)에 따른 가격 차이를 분석한다.
sns.boxplot( data=df , x='Exterior1st' , y='SalePrice' )
sns.boxplot( data=df , x='RoofStyle' , y='SalePrice' )
plt.xlabel('지붕 스타일(RoofStyle) 및 외장재(Exterior1st)')
plt.ylabel('가격(SalePrice)')
plt.title('주요 외관 요소별 가격 분포 비교')
plt.show()

# 5-5. 상관관계 시각화 및 핵심 인자 도출 (가설 3 검증)
# sns.heatmap을 사용하여 수치형 변수 전체의 상관계수를 시각화하고한다.
matrix=df[["GrLivArea","SalePrice"]].corr()
sns.heatmap(matrix, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("수치형 변수 전체의 상관계수")
plt.show()
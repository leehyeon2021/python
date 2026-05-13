import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import korean_font

# [1. 타이타닉 생존 데이터 분석]
# 출처: Kaggle - Titanic: Machine Learning from Disaster
# https://www.kaggle.com/competitions/titanic/overview

# [2. 가설]
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 원칙)
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

# 판다스로 불러오기
df = pd.read_csv('./day15/train.csv')
print( df.head() )          # 상위 5개 출력하여 데이터 확인
df.info()                   # 속성 확인
print( df.isnull().sum() )  # 결측치 확인
print()


# [3. 데이터 전처리]
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
# `.fillna( 특정값 )`: 만약 결측이면 특정값으로 채우는 함수
df['Age'] = df['Age'].fillna( df['Age'].median() )
#print( df.isnull().sum() )     # 결측치 확인 177->0
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.
df['Embarked'] = df['Embarked'].fillna( df['Embarked'].mode()[0] )
#print( df.isnull().sum() )     # 결측치 확인 2->0

# [4. 데이터 시각화 및 분석]
# 4-1 : 생존 분포 분석: sns.countplot을 사용하여 전체 생존자와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
# `plt.bar()`: 수치값( 남:3 , 여:5 ) vs. `sns.countplot()`: 범주값( 남남남여여여여여 )
sns.countplot( df , x='Survived' )      # 0 = 사망, 1 = 생존
plt.title('생존 여부 분포')
plt.xlabel('생존 여부 (0: 사망 , 1: 생존)')
plt.ylabel('인원 수')
plt.show()

# 4-2 : 연령대별 상세 분석: sns.hisplot을 사용하여 나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
print( df[df['Survived'] == 0]['Age'] ) # 사망한 사람들의 나이만 추출 / 필터링 df[ 조건식 ]
print( df[df['Survived'] == 1]['Age'] ) # 생존한 사람들의 나이만 추출
sns.histplot( df[df['Survived'] == 0]['Age'] , label='사망' , color='black' , kde=True )
sns.histplot( df[df['Survived'] == 1]['Age'] , label='생존' , color='green' , kde=True)
plt.title('나이별 생존 분포')
plt.xlabel('나이')
plt.ylabel('인원 수')
plt.legend()
plt.show()

# 4-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# `sns.countplot( data=df , x='x축레이블' , hue='나누기기준' )`
print( df['Sex'][0] )                                   # 성별은 문자타입으로 구성된 상태 , male
sns.countplot( data=df , x='Sex' , hue='Survived')      # 성별 수
plt.legend( title='범례제목' , labels=['사망', '생존'])
plt.show()

# 4-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
print( df['Pclass'][0] )                                # 1=1st , 2=2nd  , 3=3rd
sns.countplot( data=df , x='Pclass' , hue='Survived')   # 객실 등급 수
plt.legend( title='범례제목' , labels=['사망', '생존'])
plt.show()

# 4-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
print( df['Embarked'][0] )                              # C=Cherbourg , Q=Queenstown , S=Southampton
sns.countplot( data=df , x='Embarked' , hue='Survived') # 승선 항구 수
plt.legend( title='범례제목' , labels=['사망', '생존'])
plt.show()
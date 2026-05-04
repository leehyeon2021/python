import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rc('font', family='Malgun Gothic') # 또는 'Noto Sans CJK JP'
plt.rcParams['axes.unicode_minus'] = False

# 문제 1: 다중 선 그래프와 스타일 설정
# x축 데이터 [0, 1, 2, 3, 4]를 기준으로 다음 두 개의 선을 하나의 그래프에 그리시오.
# - 선 1: y값 [10, 20, 15, 25, 30], 색상 'blue', 선 스타일 점선(':'), 라벨 '매출'
# - 선 2: y값 [5, 15, 10, 20, 25], 색상 'red', 선 스타일 실선('-'), 라벨 '비용'
# 조건: 범례(legend)를 표시하고, 격자(grid)를 활성화하며 제목은 '월별 실적 분석'으로 설정하시오.
x = [0, 1, 2, 3, 4]
plt.plot( x, [10, 20, 15, 25, 30], label='매출', c='blue', linestyle=':')
plt.plot( x, [5, 15, 10, 20, 25], label='비용', c='red', linestyle='-')
plt.legend()
plt.grid(True)
plt.show()

# 문제 2: 비교 막대그래프(Grouped Bar Chart) 생성
# 두 과목의 성적 데이터를 막대그래프로 시각화하시오.
# - 카테고리: ['A', 'B', 'C'], 국어: [80, 90, 70], 수학: [85, 85, 95]
# - 조건: np.arange를 사용하여 막대가 겹치지 않게 배치하고(폭 0.4), 
# x축 눈금을 'A', 'B', 'C'로 표시하며 y축 레이블을 '점수'로 설정하시오.
categories = ['A', 'B', 'C']
kor = [80, 90, 70]
math= [85, 85, 95]
x = np.arange( len(categories))
plt.bar( x-0.2 , kor, width=0.4 , label='국어성적', color='pink' )
plt.bar( x+0.2 , math, width=0.4 , label='수학성적', color='green')
plt.xticks( x, categories)
plt.ylabel('점수')
plt.show()

# 문제 3: 파이 차트(Pie Chart)를 이용한 점유율 시각화
# 아래 데이터를 바탕으로 파이 차트를 생성하시오.
# - 데이터: '스마트폰'(45), '태블릿'(25), '노트북'(20), '기타'(10)
# - 조건: '스마트폰' 조각을 0.1만큼 돌출(explode)시키고, 
# 백분율을 소수점 첫째 자리까지 표시(autopct)하며 시작 각도를 90도로 설정하시오.
labels = ['스마트폰', '태블릿', '노트북', '기타']
sizes = [45, 25, 20, 10]
colors = [ "#ff0000", "#ff53b2", "#f71bff", "#ae00ff"]
explod = [ 0.1 , 0 , 0 , 0]
plt.pie( sizes , labels=labels , colors=colors , explode=explod , startangle=90 , autopct='%1.0f%%') 
plt.show()

# 문제 4: 산점도(Scatter Plot)와 히스토그램(Histogram) 분석
# 1. x=[1, 2, 3, 4], y=[10, 15, 13, 18] 데이터를 사용하여 파란색 점, 크기 100의 산점도를 그리시오.
# 2. data = [1, 2, 2, 3, 3, 3, 4, 4, 5] 데이터를 사용하여 빈(bins)의 개수가 5인 
# 하늘색 히스토그램을 생성하시오. (두 그래프는 각각 별도의 창으로 출력)
x=[1, 2, 3, 4]
y=[10, 15, 13, 18]
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.scatter( x , y , c='blue' , s=100)
plt.show()
plt.hist( data , color='skyblue', bins=5 )
plt.show()

# 문제 5: 서브플롯(Subplots) 구성 및 파일 저장
# 1행 2열 구조의 서브플롯을 생성하여 다음을 수행하시오.
# - 첫 번째 칸: [1, 2, 3] 데이터를 활용한 간단한 선 그래프
# - 두 번째 칸: [1, 2, 3] 데이터를 활용한 간단한 막대그래프
# - 공통 조건: 그래프의 크기를 (10, 5)로 설정하고, 최종 결과물을 'my_analysis.png'로 저장하시오.
fig , axs = plt.subplots( 1 , 2 , figsize=(10, 5) )
axs[0].plot( [1, 2, 3] )
axs[1].bar( [1, 2, 3] ,[1, 2, 3] )
plt.savefig('./day13/my_analysis.png')
plt.show()


# 문제 6: 리스트 데이터를 이용한 히트맵(Heatmap) 생성
# 5행 4열의 리스트 데이터 [[50, 60, 70, 80], [10, 20, 30, 40], [90, 80, 70, 60], [30, 40, 50, 60],[20, 10, 5, 0]]를
# 활용하여 히트맵을 그리시오.
# - 조건 1: 색상 맵(cmap)은 'Blues'를 사용할 것
# - 조건 2: 셀 내부에 정수값(annot=True, fmt='d')을 표시할 것
# - 조건 3: 제목을 '수치 분포 히트맵'으로 설정할 것
data = [[50, 60, 70, 80], [10, 20, 30, 40], [90, 80, 70, 60], [30, 40, 50, 60],[20, 10, 5, 0]]
sns.heatmap( data , cmap='Blues', annot=True, fmt='d')
plt.title('수치 분포 히트맵')
plt.show()

# 문제 7: 데이터프레임 항목 간 분포 비교 (Boxplot)
# '매출'과 '영업이익' 데이터에 대한 분포를 비교하는 박스플롯을 그리시오.
# - 데이터: '매출': [100, 200, 150, 300, 250], '영업이익': [20, 50, 30, 80, 60]
# - 조건 1: 박스 내부를 채우지 않고(fill=False), 박스 간 간격(gap)을 0.1로 설정할 것
# - 조건 2: 제목을 '주요 경영 지표 분포'로 설정할 것
data = {'매출': [100, 200, 150, 300, 250], '영업이익': [20, 50, 30, 80, 60]}
df = pd.DataFrame( data )
sns.boxplot( data=df , fill=False, gap=0.1)
plt.title('주요 경영 지표 분포')
plt.show()

# 문제 8: 특정 컬럼을 인덱스로 활용한 히트맵 분석
# 아래 데이터를 활용하여 '지역'별 '인구 밀도'와 '평균 연령'의 수치를 보여주는 히트맵을 생성하시오.
# - 데이터: 
# '지역': ['서울', '부산', '제주'],
# '인구 밀도': [17000, 12000, 600],
# '평균 연령': [40, 42, 42]
# - 조건 1: '지역' 컬럼을 인덱스로 설정하고 숫자 데이터만 추출하여 분석할 것
# - 조건 2: 색상 맵은 'coolwarm'을 사용하고 칸 사이의 구분선(linewidths)을 0.5로 설정할 것
data={'지역': ['서울', '부산', '제주'],'인구 밀도': [17000, 12000, 600],'평균 연령': [40, 42, 42]}
df = pd.DataFrame(data)
number_df = df.set_index('지역').select_dtypes(include=['number'])
print(number_df)
sns.heatmap(number_df, cmap='coolwarm', linewidths=0.5)
plt.show()

# 문제 9: 범주형 데이터의 빈도 분석 (Countplot)
# 아래 데이터를 바탕으로 '선택 메뉴'별 빈도를 나타내는 카운트플롯을 생성하시오.
# - 데이터: 
# '이름': ['A', 'B', 'C', 'D', 'E', 'F'],
# '선택 메뉴': ['피자', '치킨', '피자', '햄버거', '치킨', '피자']
# - 조건 1: x축을 '선택 메뉴'로 설정할 것
# - 조건 2: 제목을 '메뉴별 주문 빈도', y축 레이블을 '주문 수'로 설정할 것
data={'이름': ['A', 'B', 'C', 'D', 'E', 'F'],'선택 메뉴': ['피자', '치킨', '피자', '햄버거', '치킨', '피자']}
df = pd.DataFrame(data)
sns.countplot( df , x='선택 메뉴' )
plt.title('메뉴별 주문 빈도')
plt.ylabel('주문 수')
plt.show()
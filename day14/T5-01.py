
import matplotlib.pyplot as plt     # 맷플로립( 시각화 라이브러리 )
import pandas as pd                 # 판다스( 데이터 표 관리 )
import korean_font                  # 맷플로립그래프 한글 깨짐 방지
import json                         # JSON 파일 load 용도
import numpy as np

# 1. JSON 파일에서 특정한 열('customer_data')만 가져와서 데이터프레임 구성
# 계속 T5_data.json에서 복붙하기 힘드니 새로 만든 것.
with open('./day14/T5_data.json', 'r', encoding='utf-8' ) as json_file:
    data_json = json.load( json_file )
df_customer = pd.DataFrame( data_json['customer_data'] )
print( df_customer.head() )
print()


# 2. 데이터 분석 / 시각화
# 과제:
# 1) 연령대별(그룹) 총 고객수 막대그래프
# 2) 성별 + 연령대별(그룹) 막대그래프
# 3) 연령대별(그룹) '평균 구매 금액' 가로 막대 그래프

# 과제 수행 단계:
# 1-1) 성별과 연령대로 그룹화 (`df.groupby(['그룹기준','그룹기준'])`)
#df_customer.groupby(['성별', '연령대'])   # groupby로 그룹 만들고 총 고객수 구하기
# 1-2) 다수 통계 (`df.agg({'열이름':'함수명})`)
# 1-3) 여러 개 그룹화할 경우에는 `.reset_index()` 함수 이용하여 행번호 붙인다.
newDf = df_customer.groupby(['성별', '연령대']).agg( {'고객 수':'sum', '평균 구매 금액': 'mean'} ).reset_index()
print( newDf )                                            # 성별 + 연령대별 총고객수(합계)와 평균구매금맥의 평균(평균)
print( newDf['연령대'] )                                   # 남성 여성 포함하여 연령대 (중복)
print( newDf['연령대'].unique() )                          # 남성 여성 포함하여 연령대 (중복 제거)
print( newDf.groupby(['연령대']).agg({'고객 수':'sum'}))    # 연령대별 총고객수
# 1-4) 연령대별(그룹) 총 고객수 막대그래프 (`plt.bar(x,y)`)
plt.bar( 
    newDf['연령대'].unique() , 
    newDf.groupby(['연령대']).agg({'고객 수':'sum'})['고객 수'] , 
    color = 'navy',
    label = '누적 고객 수'
    )
plt.xlabel('연령대')
plt.ylabel('총 고객수')
plt.legend()
plt.title('연령대 별 누적 고객 수')
plt.show()
# 차트 확인: 30대가 비중이 가장 크고, 50대 고객이 가장 적다

# 2-1) 여성/남성 데이터만 추출
male_data = newDf[newDf['성별']=='남성']      # 남성 데이터만 추출(필터링)
female_data = newDf[newDf['성별']=='여성']    # 여성 데이터만 추출(필터링)
plt.bar( 
    male_data['연령대'] , 
    male_data['고객 수'], 
    label = '남성 수', 
    color='yellow'
)
plt.bar( 
    female_data['연령대'] , 
    female_data['고객 수'], 
    label = '여성 수',
    color='skyblue',
    bottom=male_data['고객 수']   # 만약 겹쳐 나오는 경우: 뒤 순서로 변경할 막대에 `bottom=df['열이름']` 앞으로 올릴 자료를 대입.
)
plt.title('성별 및 연령대 별 누적 고객 수')
plt.legend()
plt.xlabel('연령대')
plt.ylabel('총 고객 수')
plt.show()
# 차트 확인: 남성/여성 모두 30대에서 고객 수가 확연히 크다.
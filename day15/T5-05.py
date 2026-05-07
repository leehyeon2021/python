import pandas as pd
import matplotlib.pyplot as plt
import korean_font
import json

# 1. 
with open('./day14/T5_data.json', 'r', encoding='utf-8' ) as json_file:
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['financial_performance_data'] )
print( df.head() )
print()

# 2. 박스 플롯: '수익', '비용', '이익'으로 박스 플롯 표시
# `plt.boxplot()`: 데이터 최솟값, 최댓값, 1사분위, 중앙값 3사분위 시각화
plt.boxplot( [ df['수익'] , df['비용'] , df['이익'] ] , tick_labels=['수익', '비용', '이익'] )
plt.ylabel('금액')
plt.title('항목별 성과 분포')
plt.show()

# 차트확인: 비용 데이터에서 800 부근에 이상치가 존재한다.


# 3. 박스 플롯: 분기별 수익 데이터로 박스플롯 표시 (pandas에서 지원함-안 하려면 groupby나 for문으로 하면 된다.)
# 박스 플롯에서 그룹 만들기: `df.boxplot( column=['값'] , by='그룹기준' )`
df.boxplot( column=['수익'] , by='분기' )
plt.show()

# 차트 확인
    # 2분기는 수익 중앙값이 가장 높다.
    # 1분기는 박스가 길기 때문에 수익이 불안정/불확실하다.
    # 4분기는 박스가 조밀하게 있어서 수익성이 안정되었다.

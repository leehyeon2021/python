
import pandas as pd
import matplotlib.pyplot as plt
import korean_font
import json

# 1. 
with open('./day14/T5_data.json', 'r', encoding='utf-8' ) as json_file:
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['risk_return_data'] )
print( df.head() )
print()

# 2. 산점도: 리스크 대비 수익률. 값에 따른 계산식별로 원형 크기 조정 (=> 버블차트)
# `plt.scatter( x축 , y축 , s=원형크기 )`
plt.scatter( df['리스크'] , df['수익률(%)'] , s=df['수익률(%)']*100 , alpha=0.5 )
plt.xlabel('리스크')
plt.ylabel('수익률')
plt.title('리스크 대비 수익률')
plt.show()

# 3. 산점도: 자산별(그룹) 리스트 대비 수익률
# 1) 중복 제거된 자산 리스트
categories = df['자산'].unique()
print( categories )     # ["자산 A", "자산 B", "자산 C", "자산 D", "자산 E"]
# +) 색상 각각 넣는 법
color = ['red', 'orange', 'yellow', 'green', 'blue']
# 2) `enumerate(리스트)`: 반복순회자. 인덱스와 요소값을 하나씩 반환한다.
for i , category in enumerate( categories ):
    sub = df[ df['자산'] == category ]
    print( sub )
    plt.scatter( sub['리스크'] , sub['수익률(%)'] , label=category )
plt.legend()
plt.show()
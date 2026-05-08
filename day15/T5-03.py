
import pandas as pd
import matplotlib.pyplot as plt
import korean_font
import json

# 1. 
with open('./day14/T5_data.json', 'r', encoding='utf-8' ) as json_file:
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['patient_status_data'] )
print( df.head() )
print()

# 2. 막대 차트: 상태별 환자수 비교
# `plt.bar( x축값 , y축값 )`
plt.bar( df['상태'] , df['환자수'] )
plt.title('상태별 환자 수 비교')
plt.xlabel('상태')
plt.ylabel('환자수')
plt.show()

# 3. 원형차트: 전체 대비 각 상태의 환자수 백분율
# `plt.ple( 값 , labels='' , autopct='%.nf%%' , startangle=시작각도 )`
plt.ple( df['환자 수'] , labels=df['상태'] , autopct='%.2f%%' , startangle=90 )
plt.title('환자 상태 비율')
plt.show()
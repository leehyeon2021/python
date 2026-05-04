
# matplotlib


# 1. 맷플롭릿 설치
# `pip install matplotlib` (`py -m pip install matplotlib`)
# 2. 맷플롭릿 불러오기
# `import matplotlib`
import matplotlib as mpl
print( mpl.__version__ )    # 3.10.9
# 3. 관례적 import 하는 방법
    # 1) import matplotlib as mpl
    # 2) import matplotlib.pyplot as plt

# **시각화**란? : 데이터 분석 결과를 시각적으로 표현하여 인사이트(특징) 도출

# **항상 차트 사용하는 파일 상단에 아래 복붙**
# +) matplotlib은 한글 지원 안 해준다. 폰트 강제 지정 필요 (Mac 사용자는 'AppleGothic' 사용)
mpl.rc('font', family='Malgun Gothic') # 또는 'Noto Sans CJK JP'
# ++) 한글 폰트를 지정하면 음수(-) 기호 깨짐 -> 아래 코드를 항상 함께 작성하는 것이 필수 관례
mpl.rcParams['axes.unicode_minus'] = False

# 1. 선 그래프(1)
import matplotlib.pyplot as plt
# 그래프 데이터 준비
# x축( 가로축의 값 )
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y축( 세로죽의 값 )
y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 그래프 설정: `.title('차트제목')`
# `plt.plot( x값, y값 )`
plt.plot( x, y )
# 차트 제목
plt.title( 'Line Chart Exam' )
# x축 제목 : `plt.xlabel('x축제목')`
plt.xlabel( 'X-axis Title' )
# y축 제목 : `plt.ylabel('y축제목')`
plt.ylabel( 'Y-axis Title' )
# 눈금선 표시: `plt.grid(True)`
plt.grid(True)

# 그래프 출력
plt.show()

# ================

# 2. 선 그래프(2)
y2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
plt.plot( x , y , label = '감소하는 선(범례명)' , color = 'blue' , linestyle = ':' )
plt.plot( x, y2 , label = '증가하는 선(범례명)' , color = "#ffa4d6" , linestyle='-')

# color는 c로 줄여서 써도 됨

# 범례에 항목명 표시
plt.legend()

plt.show()

# ================

# 3. 막대 그래프
categories = [ '학생1', '학생2', '학생3', '학생4' ]
values1 =    [   85  ,   92   ,   78  ,   90   ]
values2 =    [   43  ,   68   ,   70  ,   88   ]

# 막대 겹치지 않게 표시
import numpy as np
x = np.arange( len(categories) )    # 0부터 x축의 값 개수 만큼 생성 (<- 0~3)
# : 아래에 width='막대굵기'를 같게 함
# 막대 만들기: `plt.bar( x축 , y축 , width=선굵기 , label='항목명 , color='색상' )`
plt.bar( x -0.2 , values1 , width=0.4 , label = '국어성적' , color = "#ffb45e" )
plt.bar( x +0.2 , values2 , width=0.4 , label = '수학성적' , color = "#d6ffa7" )
    # x축 자리에 categories 대신 np.arange( len(categories) ) +-0.2(총 거리 0.4) 넣는 이유
    # : 겹지치 않게 하려고

# 마찬가지로 title넣으면 제목 들어감
plt.title('학생 성적 비교')
plt.xlabel('학생 명')
plt.ylabel('성적 점수')
plt.legend()
plt.grid(axis='y', color='#eeeeee')   # y축만 넣기 (색도 설정 가능)

# `plt.xticks( x, y )`: 눈금 이름 설정. 번호 순서대로 라벨 지졍할 때 사용
plt.xticks( x, categories ) # 위치(인덱스.0~3) 순으로 라벨(학생1~학생4) 지정

plt.show()

# ============

# 4. 파이 그래프: 백분율 나타내기
# `plt.pie( 값 , labels='항목명' , colors='색상' , explode='강조' , startangle=시작각도 , autopct='비율표시' )`
labels = ['피자', '햄버거', '샐러드', '파스타']
sizes =  [  40 ,    30  ,    20  ,   10   ]
colors = [ 'gold', 'lightcoral', 'lightskyblue', 'lightgreen' ]
explod = [  0.1  ,   0   ,   0    ,   0   ] # 원형에서 튀어나오는 정도(강조)

plt.pie( sizes , labels=labels , colors=colors , explode=explod , startangle=90 , autopct='%1.0f%%')    # 형식문자
# +) %1.0f%% -> 형식문자 %자릿수.소수자릿수f, f실수 , %%는 형식문자아니고 %문자표시

plt.title('음식 선호도')
plt.legend()

plt.show()

# =============

# 5. 산점도: 밀집도 나타내기
# `plt.scatter( x축값 , y축값 , c(color) = '색상' , s ='점크기' )`
x = [ 1.5 , 2.5 , 3.5 , 4.5 , 5.5 ]
y = [ 50 , 60 , 65 , 70 , 75 ]

plt.scatter( x , y , c = 'red' , s=50 )  # c == color , s == sizes
plt.grid()
plt.show()

# ===============

# 6. 히스토그램: 상관관계 나타내기
# `plt.hist( 값 , c='색상' , alpha=투명도값 , bins=구간개수 )`
data = []   # 샘플데이터 넣기
for i in range(500):
    value = sum([ (i*j)%100/100 for j in range( 1 , 13 ) ])    # 리스트 내포( 1차원 리스트 생성 )
        # +) (i*j)%100 <- 나머지값 계산  ,  /100 <- 0~1 사이 값으로 계산  ,  .sum()   => 13개의 0~1사이의 난수를 만들어서 총합계 (중앙값이 큰 난수 생성될 예정) 
    data.append( value )
print(data)
# 차트 만들기
plt.hist( data , color='skyblue' , alpha=0.7 , bins=20 )
plt.show()

# ===============

# 7. 다중 그래프(서브플롯) 표현: 
# `fig , axs = plt.subplots( 행개수 , 열개수 , figsize = ( 가로 , 세로 ) )`
fig , axs = plt.subplots( 1 , 2 , figsize=(10, 7) )    # 한 줄에 2개 차트
    # fig(figure): 다중 그래프를 가진 전체 그래프
        # figsize: 전체 그래프의 가로inch와 세로inch를 넣어주면 된다.
    # axs: 다중 그래프의 위치. axs[0]은 첫 번째 그래프 , axs[1]은 두 번째 그래프

# 다중그래프의 타이틀, 라벨 등: `axs[인덱스].set_함수명('내용')`

axs[0].plot( [1, 2, 3] , [1 , 4, 9] )
axs[0].set_title('선 그래프')
axs[0].set_xlabel('x축 제목')
axs[0].set_ylabel('y축 제목')
axs[1].bar( [1, 2, 3], [3, 5, 2] )
axs[1].set_title('막대 그래프')
axs[1].set_xlabel('x축 제목')
axs[1].set_ylabel('y축 제목')
# (x) plt.title('전체 그래프 제목') -> 이런 식으로 하면 마지막 그래프 제목이 바뀜(이유는 모르겠음)

# 그래프 이미지(png) 다운로드
# `plt.savefig('파일경로')`
plt.savefig('./day13/save_chart.png')

plt.show()

# 직접 지정하기: 행=2, 열=2, 총 그래프 수=4
# fig , axs = plt.subplots( 2, 2 )
# axs[0][0]
# axs[0][1]
# axs[1][0]
# axs[1][1]
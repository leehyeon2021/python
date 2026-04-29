
# ======= 샘플 데이터 넘파이 배열에 대입 =======
# customer_purchase_data.csv 다운 받아서 현재 py 파일과 같은 폴더에 저장
import numpy as np

# 1. .csv(','쉼표로 구분한 자료의 형식) 파일 가져오기
# `data = np.genfromtxt( "파일경로", delimiter='구분문자', skip_header=제외할헤더(행)수)`
data = np.genfromtxt( 
    "./day11/customer_purchase_data.csv",
    delimiter=',',
    skip_header=1
)
# 2. 가져온 데이터의 넘파이 형식 확인
print(f"데이터 형태: {data.shape}")     # 데이터 형태: (1000, 5)

# ======= 문제 =======
# [ 프로젝트 배경 ]
# 당신은 대형 온라인 쇼핑몰의 데이터 팀에 소속되어 있습니다. 전 세계 고객들의
# [고객ID, 방문 횟수, 평균 체류 시간(분), 장바구니 담은 횟수, 최종 구매 금액($)] 
# 데이터를 분석하여, 우수 고객(VVIP)을 식별하고 마케팅 효율을 높이기 위한 분석 보고서를 작성해야 합니다.

# 1. 데이터 준비 : 데이터 구조 (Columns)
#     [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]
#     [고객ID, 방문횟수, 체류시간, 장바구니횟수, 구매금액]

# 2. 프로젝트 단계별 미션
#     Step 1: 데이터 기초 통계 분석
#         전체 데이터에서 구매 금액(마지막 열)만 추출하여 sales 배열을 만드세요.
#         고객들의 평균 구매 금액과 총 매출액을 계산하여 출력하세요.
sales = data[:, -1]
print(f"평균 구매 금액: {int(np.mean(sales))}달러")
print(f"총 매출액: {int(np.sum(sales))}달러")

#     Step 2: 충성 고객 필터링 (Boolean Indexing)
#         방문 횟수(1번 열)가 20회 이상이거나 구매 금액이 2000달러 이상인 고객을 '충성 고객'으로 분류하세요.
#         충성 고객들의 ID를 추출하여 출력하세요.
# a = data[:,0][sales >= 2000]
# b = data[:,0][data[:,1]>=20] -> 이건 교집합 필요한데 교집합 몰라서 실패 (Set이겠지만)
vip = data[:,0][ (data[:,1]>=20) | (data[:,4]>=2000)]
print(f"충성 고객 ID: {vip}")

#     Step 3: 구매 전환율 및 효율성 계산 (Broadcasting)
#         구매금액 / 방문횟수를 계산하여 방문당 평균 매출(ARPV) 배열을 생성하세요.
#         ARPV가 가장 높은 고객의 ID를 출력하세요.
arpv = data[:,4]/data[:,1]
find_index = np.argmax( arpv )  # 최대 ARPV값이 있는 인덱스: 516  ->  고객 번호 찾아야 함
print(f"ARPV 높은 고객: {int(data[find_index, 0])}번 고객")

#     Step 4: 휴면 고객 및 이탈 위험군 식별 (Logic)
#         방문 횟수가 3회 이하이면서 장바구니에 담은 횟수가 1회 이하인 고객을 '이탈 위험 고객'으로 분류합니다.
#         이 조건에 해당하는 고객들의 데이터를 추출하고, 전체에서 몇 명인지 출력하세요.
# "전체에서 몇 명인지" --> 조건에서 True가 몇 개인가
coust1 = (data[:,3]<=3)&(data[:,3]<=1)
result = (data[coust1])
print(f"이탈 위험 고객 정보: {result}")
print(f"이탈 위험 고객 수: {np.sum(coust1)}명")

#     Step 5: 고객 등급 정규화 및 VVIP 선정 (Normalization)
#         구매 금액 데이터를 0과 1 사이의 값으로 정규화(Min-Max Scaling) 하세요.
#         정규화된 값이 0.9(90%) 이상인 고객을 'VVIP'로 정의하고, 해당 고객들의 모든 정보(Row 전체)를 출력하세요.
# 정규화: `(값-최소값) / (최댓값-최솟값)`
# 어떠한 자료들을 0과 1 사이의 값으로 만들어서 **백분율**로 만들면 비교가 쉽다.
data_min = np.min( data[:,4] )
data_max = np.max( data[:,4] )
norm_data = (sales - data_min) / (data_max - data_min)
vvip = norm_data >= 0.9
print(f'VVIP 명단: {data[vvip]}')   # 참고
# ===================

# 참고(복습)
# True/False 배열을 원본에 넣어주면 True인 것들만 가져올 수 있다.
x = np.array( [ True , False , True ] )
y = np.array( [ 1 , 2 , 3 ] )
print( y[x] )   # [1 3] -> True인 것만.
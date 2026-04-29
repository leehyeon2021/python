import numpy as np

data = np.genfromtxt(
    "./day11/team/layoffs_events.csv",
    delimiter=",",
    filling_values=0,
    invalid_raise=False,
    skip_header=1,
    encoding="utf-8",
    dtype=str,
)
#print(f"데이터 형태: {data.shape}")
#print(data)

# 1. 해고 인원수 (데이터 기초 현황 진단)
fire = data[:,2]
fire = np.where( fire  == '' , '0' ,  fire ).astype(int)    # 0 들어간 건 두고 안 들어간 건 0 넣기
print(f"해고 인원: {fire}")
print(f"총 해고 인원 수: {np.sum(fire)}명")
find_index = np.argmax(fire)
print(f"해고 인원 가장 많은 기업: {data[np.argmax(fire), 0]} ({np.sum(fire)}명)")

# 2. 산업 그룹 (중복 몇 개 (for문?))
industry = data[:,4]
print( industry )
a = np.array(np.unique_counts(industry)[0])
b = np.array(np.unique_counts(industry)[1])

z = np.full( (31,2) , '000000000000' )
z[ : , 1 ] = b
z[ : , 0 ] = a
print(z)
print( f'{z[:0]}: {z[:1]}')




# 3. ai/머신러닝 여부 판단(True/False)


# 4. True/False인 기업 각 해고율
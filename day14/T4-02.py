import pandas as pd

# 1. 외부 파일 판다스 자료로 불러오기
# 1) .csv 파일 불러오기
df = pd.read_csv(
    './day14/data.csv',                         # 파일 경로
    header=0,                                   # 시작할 행 번호 (0부터 시작)
    encoding='utf-8',                           # 인코딩(한글: utf-8 , cp949 , euc-kr ). 파일마다 다를 수 있다.
    usecols=['사번', '이름', '나이', '부서'],      # 특정한 열만 추출
    na_values=[' ', '-', '미응답', 'N/A'],       # 특정 값을 결측치로 변환('N/A'는 엑셀의 결측치 값)
    on_bad_lines='warn',
    dtype={'사번': str},                         # 특정한 열만 타입 지정 (아니면 자동)

)
print( df )
print()

# 2) .excel 파일 불러오기 ( `pip install openpyxl` 설치 필요)
df = pd.read_excel(
    './day14/data.xlsx',
    sheet_name='Sheet1',                # 특정한 시트
    skiprows=0,                         # 시작할 행번호
)
print( df )
print()

# 3) .json 파일 불러오기
df = pd.read_json(
    './day14/data.json'
)
print( df )

# 4) .xml 파일 불러오기 (`pip install lxml`)
# `xpath='.//가져올태그명'`: 가져올 태그명은 웬만하면 `row`
df = pd.read_xml(
    './day14/data.xml',
    xpath='.//row'
)
print( df )

# =====

# 2. 판다스 자료 외부파일 내보내기
# 1) .csv 내보내기
df.to_csv(
    './day14/date_out.csv',     # 파일 경로
    index=False,                # 인덱스 제외
    encoding='utf-8',           # 인코딩 지정
    na_rep='Unknown',           # 결측값 치환(변경)
    header=True                 # 헤더(열이름) 포함 여부
)

# 2) .xlsx 내보내기
df.to_excel(
    './day14/data_out.xlsx',
    sheet_name='회원정보'
)

# 3) .json 내보내기
df.to_json(
    './day14/data_out.json',
    orient='records',           # 레코드(리스트) 형식으로 저장
    force_ascii=False,          # 한글 유니코드 유지
    date_format='iso',          # 날짜 형식: 표준 ISO 방식으로 지정
)

# 4) .xml 내보내기
df.to_xml(
    './day14/data_out.xml',
    index=False
)
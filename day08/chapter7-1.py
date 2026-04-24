
# os 모듈
# os 모듈 호출
import os
# 현재 운영체제
print( os.name )        # nt: '윈도우'라는 뜻.

# 현재 최상위 폴더 위치
print( os.getcwd() )    # C:\Users\sku-102-10\OneDrive\바탕 화면\python
# 현재 최상위 폴더의 내부 요소
print( os.listdir() )   # ['.git', '.vscode', 'day01', 'day02', 'day03', 'day04', 'day05', 'day06', 'day07', 'day08', 'README.md']
# 폴더 생성(make)
os.mkdir( 'hello' )
# 폴더 삭제(remove)
os.rmdir( 'hello' )

# (수정용파일생성)
with open( './day08/original.txt' , 'w' ) as file:
    file.write('hello')
# 파일명 변경
os.rename( './day08/original.txt' , './day08/new.txt' ) 

# 파일 삭제
os.remove( './day08/new.txt' )

# 시스템 명령어: 보안상 위험할 수 있으니 적절하게 사용하기.
#os.system('dir')

# =================================================================

# p.412
# datetime 모듈
from datetime import datetime
print( datetime.now() )         # 2026-04-24 09:55:56.564320
now = datetime.now()
print( now.year )               # 2026
print( now.month )              # 4
print( now.day )                # 24
print( now.hour )               # 9
print( now.minute )             # 57
print( now.second )             # 58

# 형식: Y년 m월 d일 H시 M분 S초
# 형식 만들기
output_a = now.strftime( '%Y - %m - %d , %H : %M : %S' )
print( output_a )     # 2026 - 04 - 24 , 10 : 00 : 03

# 시간 계산        (키워드 매개변수(아래의 year,month)(키워드명=값))
output = now.replace( year = ( now.year + 1 ) , month = ( now.month - 1 ) )
print( output )     # 2027-03-24 10:05:02.194193

# ============================================================

# p.414
# time 모듈
import time
print( '3초간 일시정지' )
time.sleep(3)               # 3초 간 일시정지
    # 스레드 일시정지!
    # 스레드: 코드가 실행되는 흐름단위
print( '땡' )

# ============================================

# p.415
# urllib 모듈
    # 사실 외부 라이브러리 쓰는 것이 낫다! (Jsoup이나 Selenium 같은 거...)
    # 그러나 정적 페이지는 urlib.reaquest가 빠르다.
from urllib import request

# urlopen() 함수로 구글 메인페이지 읽기
target = request.urlopen("https://google.com")
output_b = target.read()

print( output_b )   # html 가져온 듯

# ==========

# P.420
# 확인문제
# 현재 디렉터리를 읽어들이고 파일인지 디렉터리인지 구분하기
import os
output = os.listdir(".")
print( "os.liistdir():", output)
print()
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print('폴더:',path)
    else:
        print('파일:',path)

# 폴더라면 또 탐색하기 재귀 구성
def read_folder(path):
    # 폴더의 요소 읽어들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else:
            print('파일:',item)
read_folder(".")
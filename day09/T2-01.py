
# T2-01.py
# (1) numpy란? : 고성능 수치 계산 라이브러리
# (2) 설치법: 터미널에서 `pip install numpy`
# (3) numpy 불러오기: `import numpy`
import numpy

# 넘파이 버전 확인
print( numpy.__version__ )      # 2.4.4

# [1] 넘파일 배열 생성: `.array( 자료 )`
# 일반 리스트 (쉼표 나옴)
x = [ 1, 2, 3, 4 ]
print( x )
    # [1, 2, 3, 4]
# 넘파일 배열 (쉼표 없음)
x = numpy.array( [1, 2, 3, 4] )
print( x )
    # [1 2 3 4]
# 2차원 리스트: `.array( [ [1차원리스트], [1차원리스트] ] )`
x = numpy.array( [ [1, 2, 3] , [4, 5, 6] ] )
print(x)
    # [[1 2 3]
    #  [4 5 6]]
# `.zeros( (행, 열) )`: 행과 열 만큼의 0으로 배열 초기화
x = numpy.zeros( (2, 3) )
print(x)
    # [[0. 0. 0.]
    #  [0. 0. 0.]]
# `.ones( (행, 열) )`: 행과 열 만큼의 1로 배열 초기화
x = numpy.ones( (2, 3) )
print(x)
    # [[1. 1. 1.]
    #  [1. 1. 1.]]
# `.full( (행, 열) , 값 )`: 행과 열 만큼의 값으로 배열 초기화
x = numpy.full( (2, 3) , 10 )
print(x)
    # [[10 10 10]
    #  [10 10 10]]
# `.arange( 시작 , 끝, 단위 )`: 시작 부터 끝 사이의 단위 만큼 증가한 배열
x = numpy.arange( 0 , 10 , 2 )
print(x)
    # [0 2 4 6 8]
# `.linspace( 시작 , 끝, 개수 )`: 시작 부터 끝 사이의 개수 만큼 균등하게 나눈 배열
x = numpy.linspace( 0 , 10 , 5 )
print(x)
    # [ 0.   2.5  5.   7.5 10. ]
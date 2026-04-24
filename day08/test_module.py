# 변수
PI = 3.141592
# 함수1
def number_input():
    output = input( '숫자 입력>' )
    return float( output )
# 함수2
def get_circumference( radius ):
    return 2 * PI * radius
# 함수3
def get_circle_area( radius ):
    return PI * radius * radius

# 프로그램 진입정
if __name__ == "__main__":
    print( get_circumference(10) )  # 62.83184
    print( get_circle_area(10) )    # 314.1592
# 자바의 main함수처럼?
# 이 파일에서만 실행됨 -> 진입점이 여기니까... 모듈로만쓰면 실행 안 됨
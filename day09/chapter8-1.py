
# p. 467
# 객체: 속성(상태)과 메소드(행동)로 이루어진 추상화된 개념 (논리적인 개념)
# 클래스: 객체를 프로그래밍에서 표현하기 위한 설계도
# 인스턴스: 클래스를 기반으로 생성한 객체                (물리적인 개념)
# 생성자: 인스턴스가 생성될 때 실행되는 함수 = 초기화 함수 역할

# [1] 클래스 만들기 (클래스 첫 글자는 대문자)
class Student :
    # [2] 생성자 선언
    def __init__(self, name , korean, math, english, science):
        # self: 자기 자신
        # self.변수명 = 매개변수명  , self.변수명( 멤버변수 뜻 ) = 매개변수명(인자값)
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    # [4] 메소드 = 멤버함수 = 인스턴스함수 = 함수
        # PY: self , JAVA: this (해당 메소드를 호출한 인스턴스를 가리킨다.)
    def get_sum( self ):
        return self.korean + self.math + self.english + self.science
    def get_average( self ):
        return self.get_sum() / 4
    def to_string( self ):
        return "{}\t{}\t".format( self.name , self.get_sum() , self.get_average() )

# [3] 인스턴스 생성하기
students = [
    # 인스턴스 생성
    # JAVA: new 클래스명( 인자값 )
    # PY: 클래스명( 인자값 )
    Student( "윤인성" , 87 , 98 , 88 , 95 ),
    Student( "연하진" , 87 , 98 , 88 , 95 )
]

# [5] 인스턴스 내 속성값 호출
print( students[0].name )           # 윤인성
# [6] 인스턴스 내 메소드 호출: `인스턴스.메소드명()`
print( students[0].to_string() )    # 윤인성  368

# PY 알아야할 것: 클래스(인스턴스)와 딕셔너리의 차이
# JAVA 알아야할 것: 클래스(DTO/인스턴스)와 MAP<>의 차이
# 클래스는 어떠한 구조를 미리 설계하여 통일되고 상태와 행동 오차를 줄일 수 있다.
students = [
    {'name':'윤인성', 'korean':87, 'math': 98, 'english':88, 'science':95},
    {'name':'연하진', 'korean':87, 'math': 98, 'english':88, 'science':95}
]
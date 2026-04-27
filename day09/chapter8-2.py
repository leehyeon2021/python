
# `isinstance( 객체 , 클래스명 )`: 만약 해당 객체가 그 클래스로 만들어졌다면 True, 아니면 False
# vs. Java: `객체 instanceOf 클래스명`

# [1] 클래스 선언
class Student:
    # [5] 클래스 변수 (Java의 static)
    count = 0
    def func1( self ):
        return Student.count+1    # 클래스변수 호출

    def study( self ):
        print('공부를 합니다.')

    # [4] `__특수 메소드__` : 
    # 예시1) `__str__`: str() 함수가 호출될 때 자동으로 실행되는 함수
    def __str__(self):
        # str() 사용하면 무조건 '학생'이 나옴
        return '학생'
    # 예시2) `__eq__`: == 호출될 때 자동으로 실행되는 함수
    def __eq__(self, value):
        # == 사용하면 무조건 80이랑 같아야만 True가 나옴
        return 80 == value
    
    # [6] 클래스 함수 (Java의 static) @데코레이터
        # `cls`필수: class의 약자. 해당 클래스를 가리킨다.
        # +) `cls`는 클래스(붕어빵기계) , `self`는 인스턴스(기계에서생성된객체)
    @classmethod
    def print( cls ):
        print('클래스 함수 호출')
        print( cls.count )

class Teacher:
    def teach( self ):
        print('학생을 가르칩니다.')

# [2] 인스턴스 생성
classroom = [ Student(), Student(), Teacher(), Student(), Student() ]
# [3] 리스트 내 인스턴스들의 타입 확인
for person in classroom :
    # classroom 리스트 내 인스턴스가 Student이면 study() 실행
    if isinstance( person , Student ):
        person.study()
    # classroom 리스트 내 인스턴스가 Teacher이면 teach() 실행
    elif isinstance( person, Teacher):
        person.teach()
# [4] @Overid(재정의) 오버라이딩이랑 비슷함.
print( str( classroom[0] ) )    # 학생
print( classroom[0] == 90 )     # False
print( classroom[0] == 80 )     # True
# [5] 클래스 변수 호출: `클래스명.변수명`
    # 클래스 변수는 인스턴스 없이 호출 가능
print( Student.count )          # 0
print( classroom[0].func1() )   # 1
# [6] 클래스 함수 호출: `클래스명.함수명`
Student.print()                 # 0

# ==================================

# [7] 프라이빗 변수: `__변수명` (java의 private)
import math
class Circle:
    def __init__(self, radius):
        # 프라이빗 변수에 매개변수 대입
        self.__radius = radius
    def get_circumference( self ):
        # 클래스 내부에서 프라이빗 변수 호출 가능
        return 2 * math.pi * self.__radius
    def get_area( self ):
        return math.pi * (self.__radius ** 2)
    # [8] 게터와 세터: 프라이빗 변수를 외부에서 간접접근 허용 함수
    # getter: `@property`
    @property
    def radius( self ):
        return self.__radius
    # setter: `@게터함수명.setter`
    @radius.setter
    def radius( self , value ):
        self.__radius = value

# [7]
# 인스턴스 생성 후 변수에 저장하지 않았으므로 GC(가비지컬렉터)가 자동으로 인스턴스를 삭제해준다.
Circle( 20 )
# 프라이빗 변수이므로 직접호출 시 오류 발생
circle = Circle( 10 )
#print( circle.radius )

# [8] 간접접근
# getter
print( circle.radius )  # 10
# setter
circle.radius = 20
# 확인
print( circle.radius )  # 20

# ==================================
# 상속
# p.497
class Parent:
    def __init__(self):
        self.value = "테스트"
        print( "부모 클래스의 생성자가 호출되었습니다." )
    def test( self ):
        print( "부모 클래스의 test() 메소드입니다. ")
# class 클래스명( 상위클래스명 ):
class Child( Parent ):
    def __init__(self):
        # 부모의 생성자를 호출한다.
        super().__init__()
        print("자식 클래스의 생성자가 호출되었습니다.")
# 상속된 인스턴스가 생성될 때 -> 자식이 생성되면 부모도 같이 생성된다.
child = Child()
child.test()
# 자식은 부모의 멤버변수와 멤버함수를 사용할 수 있다. <물려받음>
print( child.value )

# p.498
# [10] 상속 이용한 나만의 예외 클래스 만들기
# Exception 클래스로 부터 상속 받는다.
class CustomException( Exception ):
    def __init__(self, message , value ):
        super().__init__()
        self.message = message
        self.value = value
    
    # 오버라이드/재정의 : 부모에 정의되어 있는 함수를 자식이 다시 정의
    def __str__(self):
        return self.message
    def print( self ):
        print("### 오류 정보 ###")
        print("메시지:", self.message)
        print("값:", self.value)

# 강제로 예외 발생시키기
try:
    raise CustomException( "강제예외", 10 )
except CustomException as e:
    print(e)
    e.print()
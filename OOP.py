## 파이썬 class
class User:
    count = 0 # class 변수, 인스턴스가 아닌 class에서 접근하자!

    def __init__(self,name,email,pw): # magic method : 특정 상황에서 자동 호출
        self.name = name
        self.email = email
        self.pw = pw
        User.count += 1 # 인스턴스가 생성될때마다 클래스 변수 count 1씩 증가

    def say_hello(self):
        print(f"안녕! 난 {self.name}!")

    def check_name(self,name):
        return self.name == name
    
    def __str__(self): # print 함수를 호출할때 자동으로 호출됨
        return f'사용자 : {self.name}, 이멜 : {self.email}'

    @classmethod # 데코레이터를 활요해 class method 선언
    def number_of_users(cls): # self 대신 cls, 즉 class를 첫번째 파라미터로 갖는다
        print(f"총 유저 수 : {cls.count}")


user1 = User('이현','chdnjf103@naver.com','478956')
user2 = User('조수연','susie@naver.com','12345')
user1.number_of_users()
User.number_of_users()

# 아래 두 줄은 같은 동작
User.say_hello(user1) # class에서 method 호출
user1.say_hello() # instance에서 method 호출 : 이때 인스턴스가 자동으로 method의 첫번째 파라미터로 들어간다!!


## 데코레이터
def add_print_to(origin): # 데코레이터 : 함수를 파라미터로 받아 데코레이팅 후 데코레이팅 된 함수를 return
    def wrapper():
        print('함수 시작')
        origin()
        print('함수 끝')
    return wrapper

# 데코레이팅 하고자 하는 함수 위에 @데코레이터, 여러 함수에 반복적인 기능을 데코레이터 처리하면 효율적임
@add_print_to     
def print_hello():
    print('안녕')

print_hello()


## ternary expression
sex = True
condition = 'tired' if sex else 'nice'

## list comprehension
lst = [1,2,3,4,5,6]
square = [x**2 for x in lst]

# zfill
print("Hyun".zfill(15))
print("Konkuk".zfill(15))
print("Statistics".zfill(15))

## 시계 프로그램
class Clock:
    def __init__(self,hour,min,sec):
        self.hour = hour
        self.min = min
        self.sec = sec
    def tick(self):
        self.sec += 1
        if self.sec >= 60:
            self.sec = self.sec % 60
            self.min += 1
            if self.min >=60:
                self.min = self.min % 60
                self.hour += 1
                if self.hour > 23:
                    self.hour = 0
    def set(self,hour,min,sec):
        return Clock(hour,min,sec)
    def __str__(self) -> str:
        return f"{self.hour}:".zfill(3) + f"{self.min}:".zfill(3) + f"{self.sec}".zfill(2)

# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)
    
# 13초를 늘린다
for i in range(13):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
    
# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)
    
# 5초를 늘린다
for i in range(5):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
    
# 23시 59분 57초로 세팅
clock.set(23, 59, 57)
    
# 5초를 늘린다
for i in range(5):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)


""" 객체지향 4가지 개념"""
## 1. 추상화
class BankAccount:
    """
    은행 계좌 생성하는 class
    init : 사용자 이름, balance
    """
    iterest = 0.02
    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount

## 2. 캡슐화
class Citzen:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value <0:
            self._age = 0
        else:
            self._age = value


class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000
    def __init__(self,name,password,payment_limit) -> None:
        self.name = name
        self._password = password
        self._payment_limit = payment_limit

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,value):
        self._password = value

    @property
    def payment_limit(self):
        return self._payment_limit
    
    @payment_limit.setter
    def payment_limit(self,value):
        if 0 < value < self.MAX_PAYMENT_LIMIT:
            self._payment_limit = value
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요")
            

## 3. 상속
# 부모 클래스
class Employee:
    company_name = '수민월드'
    raise_pct = 1.03

    def __init__(self,name,wage) -> None:
        self.name = name
        self.wage = wage
    
    def raise_pay(self):
        self.wage *= self.raise_pct

    def __str__(self) -> str:
        return Employee.company_name + f"직원: {self.name}"

# 자식 클래스
class Cashier(Employee):
    raise_pct = 1.05
    price = 4000

    def __init__(self,name,wage,num_sold):
        # super: 자식 클래스에서 부모 클래스의 method를 호출 할 때, self 쓰지 않는다.
        super().__init__(name,wage)
        self.num_sold = num_sold

    def take_order(self,money):
        if Cashier.price > money:
            print(f"{Cashier.price-money}원 부족")
        else:
            self.num_sold += 1
            return money - Cashier.price

    def __str__(self):
        return Cashier.company_name + f"계산대 직원 : {self.name}"

# 다중 상속
class Engineer:
    def __init__(self,language):
        self.language = language
    
    def show(self):
        print(f"활용 가능한 언어: {self.language}")

class Drummer:
    def __init__(self,durm_stick):
        self.durm_stick = durm_stick
    
    def play_drum(self):
        print(f"드럼 스틱: {self.durm_stick}")

class EngineerDrummer(Engineer,Drummer):
    def __init__(self, language,drum_stick):
        Engineer.__init__(self,language)
        Drummer.__init__(self,drum_stick)
    
hyun = EngineerDrummer('python','promark')

hyun.show()



from math import pi,sqrt


## 4. 다형성
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)

    def __str__(self):
        return f"밑변 {self.width} 높이 {self.height}인 직사각형"

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2*pi*self.radius
    
    def __str__(self):
        return f"반지름 {self.radius}인 원"

class Paint:
    def __init__(self):
        self.shapes = []
    
    def add_shape(self,shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum([s.area() for s in self.shapes])

    def total_perimeter(self):
        return sum([s.perimeter() for s in self.shapes])
    
    def __str__(self):
        for s in self.shapes:
            print(s,"\n")

r1 = Rectangle(3,7)
c1 = Circle(4)

# 추상 클래스
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @property
    @abstractmethod
    def x(self):
        pass

class RightTri(Shape):
    def __init__(self,length):
        self.length = length
    
    def area(self):
        return 2/3 * sqrt(self.length)
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value


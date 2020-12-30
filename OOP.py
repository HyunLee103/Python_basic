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

    @classmethod
    def number_of_users(cls):
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

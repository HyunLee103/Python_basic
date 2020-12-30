"""
응용통계학과 이현(201511757)
"""
## 5주차 기본문제

# 3
def check_graduate():
    print('현재까지 이수한 학점 입력하세요 :')
    num = input()
    if int(num) >= 140:
        print('졸업 가능합니다.')
    else:
        print('졸업 이수 학점은 140점입니다. 더 들으세요.')

check_graduate()


# 6
def ring_size():
    print('손가락 둘레 입력(mm) :')
    len = input()
    if 51<float(len)<=52:
        print('9호를 추천합니다.')
    elif 52<float(len)<=53:
        print('10호를 추천합니다.')
    elif 53<float(len)<=54:
        print('11호를 추천합니다.')
    elif 54<float(len)<=55:
        print('12호를 추천합니다.')
    else:
        print('반지 제작이 불가능합니다.')

ring_size()


# 9
def cash():
    print('성별 입력하세요(남/여) :')
    sex = input()
    print('나이를 입력하세요 :')
    age = input()
    if sex == '여':
        if int(age) < 20:
            print('적립 금액의 1.5배를 적립해드립니다.')
        if 20<=int(age)<30:
            print('적립 금액의 2배를 적립해드립니다.')
        if int(age) > 30:
            print('적립 금액의 3배를 적립해드립니다.')
    else:
        print('적립 금액의 2배를 적립해드립니다.')

cash()

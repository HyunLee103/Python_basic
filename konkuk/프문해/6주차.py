"""
응용통계학과 이현(201511757)
"""
## 5주차 도전문제

# 4
def scholarship():
    print('몇 학기를 수료했는지 입력 :')
    sem = int(input())
    print('GPA 입력(4.5만점) :')
    score = float(input())
    if 1<=sem<=8:
        if score >= 4.0:
            print('전액 장학금 지급')
        elif 3.5<=score<4.0:
            print('50% 장학금 지급')
        elif 3.0<=score<3.5:
            print('30% 장학금 지급')
        else:
            print('장학금을 받을 수 없습니다.')
    else:
        print('장학금을 받을 수 없습니다.') 

scholarship()


# 5 
def calc():
    print('두 양의 정수 입력 :')
    n1, n2 = int(input()), int(input())
    sum = n1 + n2
    if (sum % 2 == 0) & (sum % 3 ==0):
        print('두 수의 합은 짝수이자 3의 배수이다.')
    else:
        print('두 수의 합은 홀수이고 3의 배수도 아니다.')

calc()
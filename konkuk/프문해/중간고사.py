# 중간고사 (사칙연산)

def midterm():
    print('첫번째 수 입력 :')
    n1 = float(input())
    print('두번째 수 입력 :')
    n2 = float(input())

    print('원하는 연산 기호 하나 입력(+,-,*,/) :')
    cal = input()

    if cal == '+':
        print(f'{n1}+{n2} = {n1+n2}')
    elif cal == '-':
        print(f'{n1}-{n2} = {n1-n2}')
    elif cal == '*':
        print(f'{n1}*{n2} = {n1*n2}')
    elif cal == "/":
        if n2 != 0:
            print(f'{n1}/{n2} = {n1/n2}')
    else:
        print('잘못 입력하셨습니다.')

if __name__ == "__main__": 
    midterm()
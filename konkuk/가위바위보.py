# 가위바위보
import random

def rcp():
    print('사용자 턴, 가위/바위/보 중 하나를 입력해주세요 :')
    user = input()
    print('컴퓨터 턴(랜덤하게 결정됩니다)')
    lst = ['가위', '바위','보']
    com = random.choice(lst)
    print(f'컴퓨터 : {com}')
    if user == com:
        print('무승부')
    elif user == '가위':
        if com == '바위':
            print('컴퓨터 승!')
        elif com == '보':
            print('사용자 승!')
        else:
            print('입력오류')
    elif user == '바위':
        if com == '가위':
            print('사용자 승!')
        elif com == '보':
            print('컴퓨터 승!')
        else:
            print('입력오류')
    elif user == '보':
        if com == '가위':
            print('컴퓨터 승!')
        elif com == '바위':
            print('사용자 승!')
        else:
            print('입력 오류')
    else:
        print('입력오류')

rcp()
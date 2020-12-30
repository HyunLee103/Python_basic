"""
응용통계학과 이현(201511757)
"""
## 4주차 기본문제
# 1
list1 = ['a','b',['c','d'],1,[2,3],'e']
len(list1)
['b'] in list1
'a' in list1

# 2
list_odd = [1,3,5,7,9]
list_even = [2,4,6,8,10]
list_odd[-3]
list_even[1+3]
list_odd + list_even
2 * list_odd

# 3
list1 = [1,2,3,4,5,6,7,8,9]
list1[:3] # O
list1[0:3] # X
list1[3:5] # O
list1[3:] # O
list1[3:999] # X

# 4
string = ['a', 'b', 'c', 'd', 'e', 'f']
string[:3]
string[2:5]
string[1:3]

# 5
list1=['n', 'e', 'w', 'l', 'i', 's', 't']
list2=['n', 'e', 'w', 's', 't', 'r', 'i', 'n', 'g']
list_new=list1[ :3] + list2[6: ]
print(list_new) # ['n', 'e', 'w', 'i', 'n', 'g']

# 6
title = ['P','r','o','g','r','a','m','m','i','n','g']
title [:7] # ['P', 'r', 'o', 'g', 'r', 'a', 'm']

# 7
student=['철수', '영희', '수지', '길동', '영철']
'수정' in student # False

# 8
introduce=['내', '이', '름', '은', '수', '지', '야']
introduce[4:6] = ['민','지']
introduce[5] = '수'
introduce

# 9
tuple = ('Hello', 'My', 'name', 'is', '예슬')
tuple[4] = '지수' # X , 튜플은 객체 할당 불가
tuple.max() # X, 튜플은 max, min 속성 같고 있지 않음
# X
arr = (35, 45, 2, 10, 11)
arr[3]+arr[1] # X

# 10
def check_winner(name,lst):
    if name in lst:
        return f'{name} 수상했다.'
    else:
        return f'{name} 수상하지 못했다.'

# 10.1
winner=['향단이', '정민호', '김철수', '이영희', '홍길동']
check_winner('김수지',winner)
# 10.2
check_winner('김철수',winner)
# 10.3
check_winner('향단이',winner)
# 10.4
check_winner('성춘향',winner)
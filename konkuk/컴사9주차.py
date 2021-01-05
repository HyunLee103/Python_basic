s = int(input("초 단위의 시간을 입력하세요"))

h = s//3600
s = s%3600
m = s//60
s = s%60
print("hour:",h)
print("min:",m)
print("sec:",s)
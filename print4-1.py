# if

print(type(True))
print(type(False))

if True:
    print('good')

if False:
    print('bad')

if True:
    print('bad!')
else:
    print('good')

# 관계연산자

x = 15
y = 10

print(x == y)

print(x != y)

print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

city = ""
if city:
    print("you are in:", city)
else:
    print("please enter your city")

city1 = "Seoul"
if city1:
    print("you are in:", city)
else:
    print("please enter your city")

a = 75
b = 40
c = 50

print('and', a > b and b > c)
print('or', a > b or b > c)
print('not', not a > b)
print('not', not b > c)
print(not True)
print(not False)

print('e1:', 3+12 > 7+3)
print('e2:', 5+10*3 > 7+3*20)
print('e3:', 5+10 > 3 and 7+3 == 10)
print('e4:', 5+10 > 0 and not 7+3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

num = 90

if num >= 90:
    print('grade : A')
elif num >= 80:
    print('grade : B')
elif num >= 70:
    print('grade : C')
else:
    print('과락')

grade = 'A'
total = 88

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 탈락')

q = [10, 20, 30]
w = [70, 80, 90, 100]
e = {"name": "lee", "city": "seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values())
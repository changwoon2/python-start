# 기본선언

n = 700

print(n)
print(type(n))
print()

# 동시선언

x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75

# 재선언
var = "change value"

# 출력
print(var)
print(type(var))

# object references
print(300)
print(int(300))

# n -> 777
n = 777

print(n, type(n))
print()

m = n

print(m,n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# id

m = 800
n = 655 * 10

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 7
AGE = 7

# # 예약어는 변수명으로 불가능
# False def if raise
# none del import return
# True elif in try
# and else is while
# as except lambda with
# assert finally nonlocal yield
# break for not
# class from or
# continue global pass
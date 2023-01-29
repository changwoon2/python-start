# 파이선 지원 자료형

# int : 정수
# float : 실수
# complex : 복소수
# bool : 불린
# str : 문자열(시퀀스)
# list : 리스트(시퀀스)
# tuple : 튜플(시퀀스)
# set : 집합
# dict : 사전

str1 = "python"
bool = True
str2 = "anaconda"
float_v = 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "machine learning",
    "version": 2.0
}
tuple = {7, 8, 9}
set = {7, 8, 9}

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(set))
print(type(tuple))
print(type(dict))

i = 77
i2 = -14
big_int = 77777777777799999999999999999999

print(i)
print(i2)
print(big_int)
print()

f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산실습

i1 = 39
i2 = 939
big_int1 = 777777777779999999999323
big_int2 = 777777777779999999999323
f1 = 1.234
f2 = 3.939

# +
print(">>>>>>>+")
print("i1 + i2 :", i1 + i2)
print("f1 + f2 :", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print()

# *
print(">>>>>>>*")
print("i1 * i2 :", i1 * i2)
print("f1 * f2 :", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex('3'))
print(complex(3))
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5,3), 5 ** 3)

# 외부 모듈
import math
print(math.ceil(5.1))
print(math.pi)

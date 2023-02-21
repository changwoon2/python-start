# for

for v1 in range(10):
    print('v1 is :', v1)

print()

for v2 in range(1, 11):
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)

sum1 = 0
for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 sum : ', sum1)
print('1 ~ 1000 sum : ', sum(range(1, 1001)))
print('1 ~ 1000 4의 배수의 합 :', sum(range(4, 1001, 4)))

names = ["kim", 'park', 'cho', 'lee', 'choi', 'yoo']

for n in names:
    print('you are : ', n)

lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("current number :", n)

word = "beautiful"

for s in word:
    print('word :', s)

my_info = {
    "name": 'lee',
    "age": 33,
    "city": "seoul"
}

for key in my_info:
    print('key : ', my_info[key])

for v in my_info.values():
    print('value :', v)

name = 'FineApple'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('found : 34!')
        break
    else:
        print('not found :', num)

It = ["1", 2, 5, True, 4.3, complex(4)]

for v in It:
    if type(v) is bool:
        continue
    print("current type:", v, type(v))
    print("multiply by 2", v * 3)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 3:
        print('found : 3')
        break
    else:
        print('not found : 3')

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end="")
        print()

name2 = 'apples'
print('reversed', reversed(name2))
print('list', list(name2))
print('tuple', tuple(name2))
print('set', set(name2))
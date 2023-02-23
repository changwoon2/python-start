# 함수 및 중요성

def first_func(w):
    print("hello", w)


word = "GoodBoy"

first_func(word)


def return_func(w1):
    value = "hello, " + str(w1)
    return value


x = return_func('goodBoy2')
print(x)


def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


x, y, z = func_mul(10)
print(x, y, z)


def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)


q = func_mul2(20)
print(type(q), q, list(q))


def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


p = func_mul2(30)
print(type(p), p, set(q))


def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}


d = func_mul2(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요


def args_func(*args):
    for i, v in enumerate(args):
        print('result : {}' .format(i), v)
        print('----')


args_func('lee')
args_func('lee', 'park')
args_func('lee', 'park', 'kim')


def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-----')


kwargs_func(name1='lee')
kwargs_func(name1='lee', name2='park')
kwargs_func(name1='lee', name2='park', name3='cho')


def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, 'lee', 'kim', 'park', 'cho', age1=20, age2=30, age3=40)


def nested_func(num):
    def func_in_func(num):
        print(num)
    print('in func')
    func_in_func(num + 100)


nested_func(100)


# 람다식
def mul_func(x, y):
    return x*y


mul_func_var = mul_func
print(mul_func(10, 50))


def lambda_mul_func(x, y): return x*y


print(lambda_mul_func(50, 50))


def func_final(x, y, func):
    print(x*y*func(100, 100))


func_final(10, 20, mul_func_var)

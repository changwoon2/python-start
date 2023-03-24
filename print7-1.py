# print('error)
# print('error'))
# if True
#     pass
# a = 10
# b = 15
# print(c)

# ZeroDivisionError

# print(100/ 0)

# x = [50, 70, 90]
# print(x[1])
# print(x[4])

# KeyError

# dic = {'name' : 'Lee', 'Age' : 41, 'City' : 'Bus'}
# print(dic['hobby'])
# print(dic.get('hobby'))

# AttributeError
import time
# print(time.time2())

# x = [10,50,90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError

# f = open('test.txt')

# TypeError
x = [1,2]
y = (1,2)
z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)
print(x + list(y))
print(x + list(z))

name = ['Kim','Lee','Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('Found it! {} in name'.format(z,x+1))
except Exception:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else.')

print()

try: 
    a = 'park'
    if a == 'kim':
        print('ok! Pass')
    else:
        raise ValueError
except ValueError:
    print('Occurred! Exception!')
else:
    print('Ok! else!')

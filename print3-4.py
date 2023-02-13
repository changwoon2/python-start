# 파이썬 튜플

a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('d -', e[-1][1])
print('d -', list(e[-1][1]))
print()
print('d - ', d[0:3])
print('d -', d[2:])
print('d -', e[2][1:3])
print()
print('c + d', c+d)
print('c * d', c*3)

a=(5,2,3,1,4)
print('a -' , a)
print('a -' , a.index(3))
print('a -' , a.count(2))

print()
t = ('foo','bar','baz','qux')
print(t)
print(t[0])
print(t[-1])

print()
(x1, x2, x3, x4) = t
print(type(x1),type(x2),type(x3),type(x4))
print(x1,x2,x3,x4)

print()
t2 = 1,2,3
t3 = 4,
x1, x2, x3, = t2
x4, x5, x6 = 4,5,6

print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)
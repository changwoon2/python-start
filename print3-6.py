a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'pen', 'cap', 'plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a-', type(a), a)
print('a-', type(b), b)
print('a-', type(c), c)
print('a-', type(d), d)
print('a-', type(e), e)
print('a-', type(f), f)

t = tuple(b)
print('t -', type(t), t)
print('t -', t[0], t[1:3])

l = list(c)
l2 = list(e)

print('l -', l)
print('l2 -', l2)

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 :', s1 & s2)
print('s1 & s2 :', s1.intersection(s2))
print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))
print('s1 & s2 : ', s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print('subset : ', s1.issubset(s2))
print('superset : ', s1.issuperset(s2))

s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 -', s1)

s1.remove(2)
print('s1 -', s1)

s1.discard(3)
print('s1 -', s1)

s1.clear()
print('s1 -' , s1)

a = [1,2,3]
a.clear()
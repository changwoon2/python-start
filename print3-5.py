# 파이썬 딕셔너리

a = {'name': 'kim', 'phone': '01099997777', 'birth': '198901'}
b = {0: 'hello python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Man',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Man'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name='Man',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)

print()

print('a -', a['name'])
print('a -', a.get('name'))
print('b -', b[0])
print('a -', b.get(0))
print('a -', f.get('City'))
print('a -', f.get('Age'))

# 추가본

print()

a['address'] = 'seoul'
print('a -', a)

print('a -', len(a))
print('b -', len(b))
print('c -', len(c))
print('d -', len(d))

print('a -', a.keys())
print('b -', b.keys())
print('c -', c.keys())
print('d -', d.keys())
print('d -', list(a.keys()))
print('d -', list(b.keys()))

print()

print('a -', a.values())
print('b -', b.values())
print('c -', c.values())

print('a -', list(a.values()))
print('b -', list(b.values()))

print()

print('a -', a.items())
print('b -', b.items())
print('c -', c.items())

print('a -', list(a.items()))
print('b -', list(b.items()))

print()

print('a -', a.pop('name'))
print('a -', a)
print('c -', c.pop('arr'))
print('c -', c)

print()
print('f -', f.popitem())
print('f -', f)

print()

print('a - ', 'birth' in a)
print('a - ', 'City' in d)

a['test'] = 'test_dict'
print('a-', a)

a['address'] = 'dj'
print('a -', a)

a.update(birth='920407')
print('a-', a)
temp = {'address': 'Bus'}

a.update(temp)
print('a-', a)

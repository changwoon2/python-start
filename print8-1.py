print(abs(-3))

print(all([1,2,3]))
print(any([1,2,0]))

print(chr(67))
print(ord('C'))

for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i,name)

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos,[1,-3,2,0,-5,6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

print(id(int(5)))
print(id(4))

print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))

print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study'))

def conv_abs(x):
    return abs(x)
print(list(map(conv_abs,[1,-3,2,0, -5, 6])))
print(list(map(lambda x:abs(x),[1,-3,2,0, -5, 6])))
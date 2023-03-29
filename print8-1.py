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

print(pow(2,10))

print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

print(round(6.5781, 2))
print(round(5.6))

print(sorted([6,7,4,3,1,2]))

a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))   

# sum : 반복가능한 객체
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))

# type : 자료형 확인

print(type(3))
print(type({}))
print(type(()))
print(type([]))

# zip : 반복가능한 객체
print(list(zip([10,20,30],[40,50,60])))
print(type(list(zip([10,20,30],[40,50,60]))[0]))
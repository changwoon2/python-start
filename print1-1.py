# 기본출력
import sys
print('Python Start')
print()
print("Python Start")
print()

print('p', 'y', 't', 'h', 'o', 'n', sep='   ')
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep="@")
print()

# end 옵션

print('welcome to', end='  ')
print('IT News', end='  ')
print('Web Site')

# file 옵션
print('Learn Python', file=sys.stdout)
print()

# format 사용(a,s,f)
print('%s %s' % ('one', 'two'))
print('{0} {1}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))
print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5s}' .format('pythonstudy'))
print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))
print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f
print('%f' % (3.143333432443))
print('{:f}'.format(3.143333432443))
print('%06.2f' % (3.143333432443))
print('{:06.2f}'.format(3.143333432443))
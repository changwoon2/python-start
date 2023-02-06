str1 = "i am python"
str2 = "python"
str3 = """"how are you?"""
str4 = ''''thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
print("i'm boy")
print("i\'m boy")
print('a\t b')
print('a\"\"b')

escape_str1 = "do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = "what\'s on TV?"
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# row string
raw_s = r'D:\python\test'
print(raw_s)
print()

# 멀티라인
# 역슬래시사용
multi_str = \
    '''
String
Multi line
Test
'''
print(multi_str)

# 문자열 연산
str_01 = "python"
str_02 = "apple"
str_03 = "book kane son deli"
str_04 = "mouse"

print(str_01 * 3)
print(str_01 + str_02)
print('y' in str_01)
print('k' in str_03)
print('e' not in str_02)

# 문자열변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열함수
print("Capitalize:", str_01.capitalize())
print("endswith?:", str_02.endswith("!"))
print("replace", str_01.replace("thon", 'Good'))
print("sorted:", sorted(str_04))
print("split:", str_03.split('!'))

# 반복
im_str = "good boy!"

print(dir(im_str))

# 출력
for i in im_str:
    print(i)

# 슬라이싱 연습
str_s1 = "nice python"

print(str_s1[0:3])  # 0 1 2
print(str_s1[5:])  # 5 [5:11]
print(str_s1[:len(str_s1)])  # str_s1[:11]
print(str_s1[:len(str_s1)-1])
print(str_s1[1:9:2])
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

#아스키 코드
a = 'z'

print(ord(a))
print(chr(122))
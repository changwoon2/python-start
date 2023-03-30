# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기모드 w, 추가모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로 ('../, ./'), 절대 경로('users/omg..')

# 파일 읽기(Read)
# 예제1

f = open('./.ipynb_checkpoints/it_news.txt', 'r', encoding='UTF-8')
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반디스 close
f.close()

# 예제2
with open('./.ipynb_checkpoints/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(iter(c))
print()

# 예제3
# redd() : 전체 읽기, read(10) : 100Byte

with open('./.ipynb_checkpoints/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()

# 예제4
with open('./.ipynb_checkpoints/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# 예제5
with open('./.ipynb_checkpoints/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()
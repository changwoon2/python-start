# csv 파일 읽기 및 쓰기
# csv : MEME - text/csv

import csv

# 예제 1
with open('./.ipynb_checkpoints/it_news.txt', 'r')as f:
    reader = csv.reader(f)
    # next(reader)
    #객체 확인
    print(reader)
    #타입 확인
    print(type(reader))
    #속성 확인
    print(dir(reader))
    print()

    for c in reader:
        # print(c)
        # 타입 확인(리스트)
        # print(type(c))
        # list to str
        print(' : '.join(c))
# 예제2
with open('./.ipynb_checkpoints/it_news.txt', 'r')as f:
    reader = csv.reader(f,delimiter='|')

    for c in reader:
        print(c)

# 예제3
with open('./.ipynb_checkpoints/text.txt', 'r')as f:
    reader = csv.DictReader(f)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('----')


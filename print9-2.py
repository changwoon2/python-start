# csv 파일 읽기 및 쓰기
# csv : MEME - text/csv

import csv

# 예제 1
with open('./.ipynb_checkpoints/test1.csv', 'r')as f:
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
with open('./.ipynb_checkpoints/test2.csv', 'r')as f:
    reader = csv.reader(f,delimiter='|')

    for c in reader:
        print(c)

# 예제3
with open('./.ipynb_checkpoints/test1.csv', 'r')as f:
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
# 예제4
w = [1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]

with open('./.ipynb_checkpoints/write1.csv', 'w', encoding='utf-8')as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    # print(dir(wt))
    # 타입 확인
    # print(type(wt))

    for v in w:
        wt.writerow(v)
# 예제5
with open('./.ipynb_checkpoints/write1.csv', 'w', encoding='utf-8')as f:
    # 필드명
    fields = ['One','Two','Three']
    # Dict Writer
    wt = csv.DictWriter(f, fieldnames=fields)
    # Header Writer
    wt.writeheader()

    for v in w:
        wt.writerow({'One' : v[0], 'Two' : v[1], 'Three' : v[2]})
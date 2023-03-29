# Chapter08-2
# 파이썬 외장함수
# 실제 프로그램 개발 중 자주 사용
# 종류 sys, pickle, stutil, temfile, time, random 등

# 예제1
import sys
print(sys.argv) 

# 예제3
print(sys.path)

# pickle 객체 파일 쓰기
import pickle

# 예제4(쓰기)

f = open("test.obj", 'wb')
obj = {1: 'python', 2:'study', 3:'basic'}
pickle.dump(obj,f)
f.close()

# 예제5(읽기)
f = open('test.obj','rb')
data = pickle.load(f)
print(data, type(data))
f.close()

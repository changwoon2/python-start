# 예외처리
# try:
#     n = int(input("enter a number :"))
#     print('ok your number is : ', n)
# except ValueError:
#     print('this is not a number')

# 올바른 값 입력 완료 까지 지속
while True:
    try:
        n = int(input("enter a number :"))
        print('ok your number is : ', n)
    except ValueError:
        print('this is not a number')
        
print('ok your number is :', n)

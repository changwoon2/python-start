# hang(행맨) 미니 게임 제작(2)
# 기본 프로그램 제작 및 테스트
import time

# csv 처리
import csv
# 랜덤
import random
# 사운드 처리 윈도우용 명령어
# import winsound

# 처음 인사
name = input("What is your name?")

print("Hi, " + name, "Time to play hangman game!")

print()

time.sleep(1)

print("Start Loading...")

print()

time.sleep(0.5)

# csv 단어 리스트
words = []

# 문제 CSV 파일 로드
with open('./.ipynb_checkpoints/word_list.csv', 'r')as f:
    reader = csv.reader(f)
    # Header Skip
    next(reader)
    for c in reader:
        words.append(c)
# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

print(q)

# 정답 단어
word = "secret"

# 추측 단어
guesses = ''

# 기회

turns = 10

# 핵심 while Loop
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수
    failed = 0
    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')
            failed += 1
        else:
            # 틀린 경우 대시로 처리
            print("_", end=" ")
            failed += 1
    # 단어 추측이 성공 한 경우
    if failed == 0:
        print()
        print()
        print('congratulations! The Guesses is correct.')
    # while 구문 중단
        break
    # 추측 단어 문자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a charater.")

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1
        # 오류 메시지
        print("Oops! Wrong")
        # 남은 기회 출력
        print("You have", turns, 'more guesses!')

    if turns == 0:
        # 실패 메시지
        print("You hangman game failed. Bye!")

import random
minimum = input('請輸入隨機數的最小值: ')
minimum = int(minimum)
maximum = input('請輸入隨機數的最大值: ')
maximum = int(maximum)
answer = random.randint(minimum, maximum)
guess_times = 0
while True:
    guess_times = guess_times + 1
    guess = input('請輸入要猜的數字: ')
    guess = int(guess)
    if guess > answer:
        print('太大了，請輸入小一點')
    elif guess < answer:
        print('太小了，輸入大一點')
    else:
        print('你終於猜對了!!!')
        break
print('你猜了',guess_times,'次')
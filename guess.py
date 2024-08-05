import random
minimum = input('請輸入隨機數的最小值: ')
minimum = int(minimum)
maximum = input('請輸入隨機數的最大值: ')
maximum = int(maximum)
answer = random.randint(minimum, maximum)
guess_max = maximum
guess_min = minimum
guess_times = 0
while True:
    guess = input('請輸入要猜的數字: ')
    guess = int(guess)
    if guess < guess_max and guess > guess_min:
        guess_times = guess_times + 1
    else:
        print('請不要亂輸入，不然就扣分喔!!!')
        continue
    if guess > answer:
        print('太大了，請輸入小一點')
        guess_max = guess
    elif guess < answer:
        print('太小了，請輸入大一點')
        guess_min = guess
    else:
        print('你終於猜對了!!!')
        break
print('你猜了',guess_times,'次')
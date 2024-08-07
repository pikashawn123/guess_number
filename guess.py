

import random
minimum = input('請輸入隨機數的最小值: ')
minimum = int(minimum)
maximum = input('請輸入隨機數的最大值: ')
maximum = int(maximum)
answer = random.randint(minimum, maximum)
guess_max = maximum
guess_min = minimum
guess_times = 0
punish = False #punishment

while True:
    guess = input('請輸入要猜的數字: ')
    guess = int(guess)
    if guess <= guess_max and guess >= guess_min:
        guess_times = guess_times + 1
    else:
        if punish == True:
            guess_times += 2
            print('你已被增加兩次猜測次數，別鬧了，你要輸給對手了(你有對手嗎?)')
        elif punish == False:
            print('請不要亂輸入，不然下一次就要扣分囉(增加兩次猜測次數)!!!')    
        punish = True
        continue #不管後面的程式，從頭開始跑迴圈!
    if guess > answer:
        print('太大了，請輸入小一點')
        guess_max = guess
    elif guess < answer:
        print('太小了，請輸入大一點')
        guess_min = guess
    elif guess_times == 1:
        print('你竟然一次就猜對了!!!太強了!!!')
        break
    else:
        print('你終於猜對了')
        print('你猜了',guess_times,'次')
        break
